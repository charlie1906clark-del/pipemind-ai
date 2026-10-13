import unittest
from pathlib import Path

from pipemind.evidence import load_evidence, retrieve_verified
from pipemind.agents import compose_review
from pipemind.finance import CostInputs
from pipemind.optimization import OptimisationStudy, optimise
from pipemind.reports import draft_report
from pipemind.route import Segment, best_route


class ResearchAndAgents(unittest.TestCase):
    def test_source_manifest_unique_https(self):
        cards=load_evidence()
        self.assertGreaterEqual(len(cards),4)
        self.assertEqual(len({x.id for x in cards}),len(cards))
        self.assertTrue(retrieve_verified("cryogenics hydrogen EOS"))

    def test_agent_review_abstains_on_invalid_status(self):
        with self.assertRaises(ValueError):
            compose_review("tank",{"status":"CERTIFIED"})
        result=compose_review("tank",{"status":"SIMULATED_NOT_VALIDATED_FOR_OPERATIONS","limitations":["no vent model"]},"hydrogen model")
        self.assertTrue(result["human_review_required"])
        self.assertFalse(result["industrial_actuation"])
        self.assertTrue(result["checks"])
        self.assertTrue(result["input_payload_sha256"])

    def test_report_is_traceable_and_unsigned(self):
        model={"status":"SIMULATED_NOT_VALIDATED_FOR_OPERATIONS","limitations":["test only"]}
        review=compose_review("tank",model,"Leachman hydrogen")
        report=draft_report("abc123","tank",model,review)
        self.assertIn("NOT SIGNED",report)
        self.assertIn("abc123",report)
        self.assertIn("SHA256",report)

    def test_optimizer_abstains_without_full_costs(self):
        result=optimise(OptimisationStudy(CostInputs()))
        self.assertEqual(result["status"],"ABSTAIN_COST_DATA_MISSING")

    def test_optimizer_compares_with_provided_costs(self):
        result=optimise(OptimisationStudy(
            CostInputs(),cooling_capital_annual_gbp=1000,
            recovery_capital_annual_gbp=100,
            recovery_aux_electricity_kwh_per_kg=0.2,
        ))
        self.assertEqual(result["status"],"RESEARCH_RANKING_NOT_OPERATING_ADVICE")
        self.assertEqual(len(result["candidates"]),20)
        self.assertTrue(result["advisory_only"])

    def test_synthetic_route_avoids_protected_area(self):
        route=best_route(["a","b","c"],[
            Segment("a","c",1,protected_area=True),
            Segment("a","b",100),
            Segment("b","c",100)
        ],"a","c")
        self.assertEqual(route["nodes"],["a","b","c"])
        self.assertEqual(route["status"],"SYNTHETIC_ROUTING_SCREENING")


if __name__=="__main__":
    unittest.main()
