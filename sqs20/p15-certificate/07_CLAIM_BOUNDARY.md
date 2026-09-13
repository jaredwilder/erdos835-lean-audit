# Claim Boundary

## Closed by deterministic finite replay in this release

1. The shipped data are 15 pairwise-disjoint SQS(20), 285 blocks each, with a 570-block complement and exactly two hole blocks above every triple.
2. One-coordinate rigidity for all 15 constituents via GF(5) rank/nullspace exhaustion.
3. Complete pair-trade component classification for all 105 pairs.
4. The representative q=5 residual counts and the combinatorial identity `M^T M=A+4I`.

## Closed in previous J-SPACE release and inherited

1. Original q=2 residual graph has four K5 components.
2. That explicit 15-pack cannot be completed merely by adding two systems.
3. A full large set retaining constituents of this pack can retain at most 12, so repair radius is at least three.

## Not closed

1. Existence or nonexistence of a large set of SQS(20).
2. 5-colorability of any/all q=5 three-sacrifice residual graphs.
3. Existence of a physical three-system trade importing hole blocks.
4. Erdős #835.

## Formal-verification status

The Python certificates are deterministic finite computations and replay identically. They are **not yet kernel-checked in Lean**. The release includes a formalization plan, not a false claim of Lean closure.

## Novelty status

No theorem in this release is claimed publication-novel solely from web searching. The pack-specific rigidity and pair-profile results are labeled **apparently new** because targeted prior-art searches found no exact match. Specialist literature review and/or author contact is required before a novelty claim.
