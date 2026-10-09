"""Prepare clearly labelled private Jekyll previews without approving any events."""

import argparse
import json
from pathlib import Path
import shutil

from .extract import save_json
from .extraction import ROOT
from .reconcile import validate_record
from .registry import validator


def prepare(plan, root=ROOT):
    manifest = json.loads((plan / "plan.json").read_text())
    records = [json.loads((plan / (event_id + ".json")).read_text()) for event_id in manifest["record_ids"]]
    for record in records:
        validate_record(record, validator(root))
    data = root / "local/preview-data"
    shutil.copytree(root.parent / "_data", data, dirs_exist_ok=True)
    events = [{"id": record["id"], **record["facts"],
               "sources": [source["url"] for source in record["sources"] if source["url"]],
               "related_events": record["related_events"]} for record in records]
    events.sort(key=lambda value: (value["start_date"] or "9999", value["id"]))
    save_json(data / "community_events.json", {"schema_version": 1, "last_editorial_update": None, "events": events})
    configuration = root / "local/preview.yml"
    save_json(configuration, {"community_preview": True,
                             "data_dir": str(data.relative_to(root.parent)),
                             "destination": str((root / "local/site-preview").relative_to(root.parent))})
    return configuration


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("plan", type=Path)
    parser.add_argument("--root", type=Path, default=ROOT)
    args = parser.parse_args(argv)
    try:
        print("Prepared private preview config: " + str(prepare(args.plan, args.root)))
        print("Build with: bundle exec jekyll build --config _config.yml,_event_collector/local/preview.yml")
        return 0
    except Exception as exc:
        print("Preview preparation failed: " + type(exc).__name__)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
