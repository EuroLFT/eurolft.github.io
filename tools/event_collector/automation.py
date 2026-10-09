"""Prepare a public review package from bounded INSPIRE discovery; never approve."""

import argparse
import json
from pathlib import Path

from .extract import private_directory
from .extraction import ROOT
from .inspire import Client, discover
from .reconcile import prepare as reconcile
from .review_changes import prepare as changes


def run(root=ROOT, offline=False):
    bundle, report = discover(Client(root, offline), root)
    plan, routing, reused = reconcile(bundle, root)
    package, manifest = changes(plan, root)
    return package, report, manifest


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=ROOT)
    parser.add_argument("--offline", action="store_true")
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args(argv)
    try:
        package, report, manifest = run(args.root, args.offline)
        if args.github_output:
            with args.github_output.open("a") as handle:
                handle.write("package=" + str(package) + "\n")
                handle.write("count=" + str(len(manifest["record_ids"])) + "\n")
        print(json.dumps({"status": report["status"], "records": len(manifest["record_ids"]),
                          "package": str(package), "automatic_approval": False}))
        return 0 if report["status"] == "success" else 1
    except Exception as exc:
        print(json.dumps({"status": "review_run_failed", "failure_type": type(exc).__name__}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
