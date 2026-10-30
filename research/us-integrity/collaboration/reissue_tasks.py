#!/usr/bin/env python3
"""Reissue queued tasks against a real, already-published local Git commit.

Default is a read-only preview. --apply updates queued packets and preserves
their prior versions. No fetch, authentication, dispatch or remote write occurs.
The coordinator must confirm publication; local Git alone cannot prove a remote
branch points to this commit.
"""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import subprocess

from validate_result import COMMIT, canonical, digest, require

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[2]


def git(*args):
    return subprocess.check_output(["git", "-C", str(REPO), *args], stderr=subprocess.PIPE)


def committed_blob(commit, path):
    location = Path(path)
    require(not location.is_absolute() and ".." not in location.parts, "Input path escapes repository")
    return git("show", commit + ":" + location.as_posix())


def prepare(commit):
    require(COMMIT.fullmatch(commit), "Supply an exact 40-character commit SHA")
    require(git("cat-file", "-t", commit).decode().strip() == "commit", "Input object must be a commit")
    plan = json.loads((HERE / "reissue-plan-v2.json").read_text())
    queue = json.loads((HERE / "QUEUE.json").read_text())
    target_version = plan["target_task_version"]
    changes = []
    for assignment in queue["tasks"]:
        require(assignment["state"] == "queued_not_dispatched", "Cannot replace a dispatched assignment")
        task_path = HERE / "tasks" / (assignment["task_id"] + ".json")
        old = json.loads(task_path.read_text())
        require(assignment["task_spec_sha256"] == digest(old), "Current queue/task digest mismatch")
        require(old["task_version"] < target_version, "Task is already at or beyond target version")
        task_plan = plan["tasks"][old["task_id"]]
        paths = {item["path"] for item in old["input_files"]}
        paths.update(plan["common_required_files"])
        paths.update(task_plan["additional_required_files"])
        expanded = {}
        for prefix in task_plan["required_directory_prefixes"]:
            found = git("ls-tree", "-r", "--name-only", commit, "--", prefix).decode().splitlines()
            require(found and all(path.startswith(prefix) for path in found), "Committed capture directory missing")
            paths.update(found)
            expanded[prefix] = found
        pinned = []
        for path in sorted(paths):
            # Missing committed evidence fails here before any task file changes.
            blob = committed_blob(commit, path)
            pinned.append({"path": path, "sha256": hashlib.sha256(blob).hexdigest()})
        task = copy.deepcopy(old)
        task.update(task_version=target_version, input_commit=commit,
                    supersedes_task_spec_sha256=digest(old),
                    supersedes_input_commit=old["input_commit"],
                    input_files=pinned, question=task_plan["question"],
                    evidence_snapshot_date="2026-10-30",
                    input_manifest_expanded_prefixes=expanded)
        task["work_steps"] = task_plan["new_first_steps"] + old["work_steps"]
        task["resource_budget"]["boundary_detail"] = (
            "The external search/read budget applies to new retrieval, not local verification of pinned input blobs. "
            "Inspect summaries first and reproduce scripts locally; do not paste all raw captures into a model prompt."
        )
        changes.append((task_path, old, task))
    return queue, changes


def apply(queue, changes, commit):
    archive = HERE / "tasks" / "archive"
    archive.mkdir(parents=True, exist_ok=True)
    # Keep old canonical specifications available for stale-result diagnostics.
    for path, old, new in changes:
        destination = archive / (old["task_id"] + ".v" + str(old["task_version"]) + "." + digest(old) + ".json")
        body = (canonical(old) + "\n").encode()
        if destination.exists():
            require(destination.read_bytes() == body, "Archived task specification was modified")
        else:
            with destination.open("xb") as stream:
                stream.write(body)
    for path, old, new in changes:
        path.write_text(json.dumps(new, indent=2, ensure_ascii=False) + "\n")
        assignment = next(item for item in queue["tasks"] if item["task_id"] == new["task_id"])
        assignment.update(task_spec_sha256=digest(new), task_version=new["task_version"],
                          input_commit=commit, supersedes_task_spec_sha256=digest(old))
    # Queue is written last. Until it matches the packets, validation refuses use.
    queue["input_commit"] = commit
    (HERE / "QUEUE.json").write_text(json.dumps(queue, indent=2) + "\n")
    status_path = HERE / "CONNECTION-STATUS.json"
    status = json.loads(status_path.read_text())
    status["verified_input_commit"] = commit
    status["task_input_version"] = 2
    status["task_input_note"] = "30 October evidence blobs pinned after coordinator-confirmed research publication; no new model execution."
    status_path.write_text(json.dumps(status, indent=2) + "\n")
    for path in [HERE / "README.md", HERE.parent / "CLAUDE.md", HERE.parent / "GROK.md"]:
        text = path.read_text()
        for old_sha in {old["input_commit"] for _, old, _ in changes}:
            text = text.replace(old_sha, commit)
        text = text.replace("its seven source-file hashes", "its pinned source-file hashes")
        text = text.replace("its seven input-file hashes", "its pinned input-file hashes")
        text = text.replace("Read the seven pinned input files", "Read the pinned input files")
        path.write_text(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-commit", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    queue, changes = prepare(args.input_commit)
    if args.apply:
        apply(queue, changes, args.input_commit)
    print(json.dumps({"applied": args.apply, "input_commit": args.input_commit,
                     "remote_publication_verified_by_script": False,
                     "tasks": [{"task_id": task["task_id"], "version": task["task_version"],
                                "input_files": len(task["input_files"]), "task_spec_sha256": digest(task)}
                               for _, _, task in changes]}, indent=2))


if __name__ == "__main__":
    main()
