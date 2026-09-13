# J-SPACE v0.7 — Erdős #835 — 40-Round Checkpoint + Gold Sweep

This release contains Rounds 31–40 of the J-SPACE/KBK/RSI campaign, building on the previous 30-round checkpoint.

## Fast replay

```bash
python src/replay_all.py
```

Core replay verifies:

- explicit 15-pack validity;
- one-coordinate rigidity for all 15 constituents;
- all 105 pair trade-component profiles;
- representative q=5 residual incidence/spectral identity.

## Best results

1. **One-coordinate rigidity:** freeze any 14 systems; the fifteenth is uniquely forced.
2. **Pair geometry:** 30 same-row pairs have trade volumes `(30,30,225)`; 75 cross-row pairs are indecomposable `(285)`.
3. **Trade-space synthesis:** the automatic `-4` spectral eigenspace is exactly the signed Steiner-trade kernel.
4. **Search consequence:** future progress must use physical trades importing holes and simultaneously disturbing at least three constituents.

## Boundary

Erdős #835 remains open. No large set of SQS(20) is constructed or disproved here. Pack-specific novelty is unclaimed pending specialist prior-art review.
