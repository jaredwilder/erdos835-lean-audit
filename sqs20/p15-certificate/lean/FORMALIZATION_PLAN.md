# Lean Formalization Plan

Lean was not available in the execution environment used to build this release. Do not treat the Python certificates as kernel proofs yet.

## Lane 1 — data definitions

- Define `Point := Fin 20`.
- Define `Block := Finset Point` with card 4.
- Import the 15×285 block lists from `data/eh15_sqs20.json` as generated Lean literals.
- Define `IsSQS` as: every 3-subset lies in exactly one block.
- Use `native_decide`/finite reflection to certify all 15 systems and pairwise disjointness.

## Lane 2 — one-coordinate rigidity

Avoid formalizing Gaussian elimination first if speed matters.

Generate, for each i, the finite set of 6 GF(5) nullspace basis vectors as data plus a row-reduction certificate. Then prove:

1. every binary trade satisfying the 1140 equations maps into their span;
2. exhaustive `Fin 5 ^ Fin 6` enumeration has only zero with all coordinates in `{0,1}`;
3. therefore replacement SQS equals original `S_i`.

The final public theorem should quantify over all 15 indices.

## Lane 3 — pair trade profiles

For every pair i<j, construct the 570-vertex block-sharing graph. Use reflected connected-component computation to certify the per-side component sizes. Then prove the generic lemma that connected bipartite components correspond to indecomposable trades and side-swaps preserve SQS triple incidence.

## Lane 4 — generic residual graph theorem

This part should be human-proved, not native-decided:

- an m-pack leaves exactly q=v-3-m blocks above every triple;
- these q blocks form a clique in the residual graph;
- a proper q-coloring assigns all q colors exactly once above each triple;
- each color class is an SQS;
- converse immediate.

This theorem is reusable beyond v=20.

## Desired formal theorem names

- `eh15_is_pack`
- `eh15_one_coordinate_rigid`
- `eh15_pair_trade_profile`
- `sqs_pack_completion_iff_residual_coloring`
- `eh15_repair_radius_ge_three`
