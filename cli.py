#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import argparse
import json
import sys
from pathlib import Path

MODULE_ROOT = Path(__file__).resolve().parent
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from src.runner import MozillaOtariGatewayRunner


def main() -> None:
    parser = argparse.ArgumentParser(description="PG_MOD_30_MOZILLA_OTARI CLI")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    res = MozillaOtariGatewayRunner().execute_cycle({"residual_error": 0.08, "vram_gb": 28.0})
    print(json.dumps(res, indent=2) if args.json else f"[PASS] {res['module_id']} | {res['worm_receipt']}")


if __name__ == "__main__":
    main()
