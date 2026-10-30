#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from pathlib import Path

MODULE_ROOT = Path(__file__).resolve().parent.parent
if str(MODULE_ROOT) not in sys.path:
    sys.path.insert(0, str(MODULE_ROOT))

from src.runner import MozillaOtariGatewayRunner


def test_closure() -> None:
    r = MozillaOtariGatewayRunner()
    res = r.execute_cycle({"residual_error": 0.08, "vram_gb": 28.0})
    assert res["status"] == "PASS" and res["zdr_residual_mb"] == 0.0 and res["latency_us"] <= 1.85
    res_c = r.execute_cycle({"residual_error": 0.85, "vram_gb": 28.0})
    assert res_c["damping"] == 1.35
    print(f"[STEP 3 PASS] PG_MOD_30_MOZILLA_OTARI | Latency={res['latency_us']}us | ZDR=0.00MB")


if __name__ == "__main__":
    test_closure()
