"""CLI entry point: python -m download3d inspect model.glb --out report.json"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from .inspect import inspect_file


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="download3d", description="Offline, safe structural asset inspector")
    commands = parser.add_subparsers(dest="command", required=True)
    check = commands.add_parser("inspect", help="Inspect an already authorized local file; does not download")
    check.add_argument("file", help="File path")
    check.add_argument("--out", help="Write JSON report to path; otherwise print JSON")
    check.add_argument("--expected-count", type=int, help="Expected number of embedded glTF animations")
    check.add_argument("--expected-clip", action="append", default=[], help="Required clip name (repeat)")
    args = parser.parse_args(argv)
    if args.expected_count is not None and args.expected_count < 0:
        parser.error("--expected-count cannot be negative")
    report = inspect_file(args.file, args.expected_count, args.expected_clip)
    data = json.dumps(report, indent=2, sort_keys=True)
    if args.out:
        destination = Path(args.out)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(data + "\n", encoding="utf-8")
    else:
        print(data)
    if report["status"] != "ok":
        print("Inspection failed: " + report["errors"][0]["code"], file=sys.stderr)
    return 0 if report["status"] == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
