#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import sys
from pathlib import Path

MODULE_ROOT = Path(__file__).resolve().parent.parent
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from src.runner import MozillaOtariGatewayRunner


def run_task() -> None:
    r = MozillaOtariGatewayRunner()
    last = None
    for _ in range(50):
        last = r.execute_cycle({"residual_error": 0.05, "vram_gb": 24.0})
        assert last["status"] == "PASS"
    r_dir = MODULE_ROOT / "assets" / "audit_receipts"
    r_dir.mkdir(parents=True, exist_ok=True)
    (r_dir / f"{last['worm_receipt']}.json").write_text(json.dumps(last, indent=2), encoding="utf-8")
    print(f"[STEP 4 PASS] PG_MOD_30_MOZILLA_OTARI | 50/50 PASS | Receipt={last['worm_receipt']}")


if __name__ == "__main__":
    run_task()
