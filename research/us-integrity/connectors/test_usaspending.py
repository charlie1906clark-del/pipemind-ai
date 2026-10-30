"""Offline checks: bounded requests, provenance, and failure preservation."""
import hashlib
from io import BytesIO
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from urllib.error import URLError

import usaspending as connector


class Response(BytesIO):
    status = 200
    headers = {"Content-Type": "application/json", "Date": "Thu, 29 Oct 2026 12:00:00 GMT"}


def valid_payload():
    return {"results": [{"generated_internal_id": "TEST_AWARD_1", "Recipient UEI": "TEST00000001", "PSC": "6515"}], "page_metadata": {"page": 1, "hasNext": True}}


class ConnectorTests(unittest.TestCase):
    def test_all_cohorts_remain_finite_and_no_contacts_requested(self):
        for name in connector.COHORTS:
            request = connector.build_request(name)
            self.assertLessEqual(request["limit"], 25)
            self.assertEqual(request["page"], 1)
            self.assertFalse(any(term in " ".join(request["fields"]).lower() for term in ("phone", "email", "street", "zip5")))

    def test_rejects_unbounded_limit_and_second_page(self):
        for key, value in (("limit", 100000), ("limit", True), ("page", 2)):
            request = connector.build_request("medical-supplies")
            request[key] = value
            with self.assertRaises(connector.AcquisitionError):
                connector.validate_request(request)

    def test_rejects_unexpected_psc_and_incomplete_metadata(self):
        request = connector.build_request("medical-supplies")
        payload = valid_payload()
        payload["results"][0]["PSC"] = "1680"
        with self.assertRaises(connector.AcquisitionError):
            connector.validate_response(payload, request)
        with self.assertRaises(connector.AcquisitionError):
            connector.validate_response({"results": []}, request)

    def test_exact_response_bytes_and_hash_and_sampling_are_preserved(self):
        raw = b' { "results": [{"generated_internal_id":"x","Recipient UEI":"u","PSC":"6515"}], "page_metadata":{"page":1,"hasNext":true}}\n'
        with tempfile.TemporaryDirectory() as temp, patch.object(connector, "urlopen", return_value=Response(raw)) as network:
            result = connector.acquire("medical-supplies", Path(temp))
            self.assertTrue(result["success"])
            self.assertEqual((Path(temp) / "medical-supplies/response.json").read_bytes(), raw)
            self.assertEqual(result["response_sha256"], hashlib.sha256(raw).hexdigest())
            self.assertTrue(result["truncated_sample"])
            self.assertFalse(result["is_fraud_rank"])
            network.assert_called_once()

    def test_network_failure_has_manifest_and_no_retry(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(connector, "urlopen", side_effect=URLError("offline")) as network:
            result = connector.acquire("medical-supplies", Path(temp))
            self.assertFalse(result["success"])
            self.assertTrue((Path(temp) / "medical-supplies/manifest.json").exists())
            network.assert_called_once()

    def test_malformed_response_is_retained_but_not_successful(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(connector, "urlopen", return_value=Response(b'{broken')):
            result = connector.acquire("medical-supplies", Path(temp))
            self.assertFalse(result["success"])
            self.assertEqual((Path(temp) / "medical-supplies/response.json").read_bytes(), b'{broken')

    def test_oversize_response_is_labelled_partial(self):
        with tempfile.TemporaryDirectory() as temp, patch.object(connector, "MAX_RESPONSE_BYTES", 12), patch.object(connector, "urlopen", return_value=Response(b'x' * 30)):
            result = connector.acquire("medical-supplies", Path(temp))
            self.assertFalse(result["success"])
            self.assertNotIn("response_file", result)
            self.assertIn("partial_response_file", result)

    def test_second_run_cannot_overwrite_first_cohort(self):
        raw = connector.json_bytes(valid_payload())
        with tempfile.TemporaryDirectory() as temp, patch.object(connector, "urlopen", return_value=Response(raw)):
            connector.acquire("medical-supplies", Path(temp))
            with self.assertRaises(FileExistsError):
                connector.acquire("medical-supplies", Path(temp))


if __name__ == "__main__":
    unittest.main()
