# Erdős #835 — Johnson graph and SQS(20) research

A focused public home for Jared Wilder's work around Erdős Problem #835, including the Johnson-graph formalization audit and an independent SQS(20) completion/rigidity program.

The useful mathematics here now has **two distinct evidence lanes**. Keeping them together makes the problem easier to follow than scattering one lane through a Lean-audit repo and the other through a general archive.

## 1. SQS(20) completion and rigidity

The design-theory route starts from an explicit reconstructed 15-pack of pairwise-disjoint Steiner quadruple systems on 20 points.

### Residual completion theorem

For a partial large set `P={S_1,...,S_m}` of pairwise block-disjoint SQS on `v` points, set `q=v-3-m`. Let `R(P)` have the uncovered 4-subsets as vertices, with adjacency when two blocks share a triple.

Then

> **`P` completes to a large set of SQS(v) iff `chi(R(P))=q`.**

Moreover

- `|V(R)| = q*C(v,3)/4`;
- `deg R = 4(q-1)`;
- `|E(R)| = C(v,3) C(q,2)`.

Full proof: [`sqs20/RESIDUAL-GRAPH-THEOREM.md`](sqs20/RESIDUAL-GRAPH-THEOREM.md).

### Exact 15-pack results

For the reconstructed 15-pack on 20 points:

- 15 systems × 285 blocks = 4,275 covered four-sets;
- 570 four-sets remain uncovered;
- the `q=2` residual graph is 4-regular with component sizes `250, 25×12, 5×4`;
- the four `K5` components rule out completing **this specific 15-pack** by merely adding two systems;
- any large set retaining members of this pack can retain at most 12 of the 15, so at least three constituents must change.

Two further exact finite results are recorded in [`sqs20/P15-RIGIDITY-AND-TRADES.md`](sqs20/P15-RIGIDITY-AND-TRADES.md):

1. **One-coordinate rigidity:** every 14-subpack uniquely forces its fifteenth constituent. The relevant `1140×855` systems have GF(5) rank 849/nullity 6, and all `5^6=15,625` nullspace coefficient combinations were checked with no nonzero binary trade.
2. **Pair-trade classification:** all `C(15,2)=105` pair unions have exactly two Steiner 3-trade profiles: 30 same-row pairs with per-side volumes `(30,30,225)`, and 75 cross-row pairs with one indecomposable per-side volume-285 component.

For the `q=5` repair graph, the incidence identity `M^T M=A+4I` identifies the `-4` eigenspace with the linear Steiner 3-trade space.

## 2. Lean axiom audit

Ten Lean proof attempts around the Johnson graph `J(32,16)` were audited under Lean 4.31.0-rc1 with the available Mathlib environment.

The central result is a proof-status correction: the apparent derivation of

`17 <= chi(J(32,16))`

inherits upstream `sorryAx` through imported lemmas, including an `indepNum_johnson_le_johnsonBound` theorem defined upstream with `:= sorry`. Local compilation therefore does **not** constitute a completed proof of that lower bound.

The audit also found:

- nine smaller finite claims using `native_decide`;
- three smaller claims with clean classical axiom footprints;
- two finite list statements recoverable with zero-axiom kernel `decide`;
- clean numerical identities `johnsonBound 32 4 16 = 35357670` and `Nat.choose 32 16 = 601080390`;
- one proposed route that is inconsistent with its own assumption `chi(J(32,16))=17` while attempting to derive `18 <= chi(J(32,16))`.

The formal artifacts are under [`JS835-LEAN-RESULTS/`](JS835-LEAN-RESULTS/).

## Current frontier

The SQS(20) program has converted large-set completion into exact residual graph coloring and established a repair radius and finite rigidity/trade structure for one explicit 15-pack. The unresolved high-value branch is the `q=5` repair regime: determine whether suitable three-system sacrifices produce a 5-colorable residual graph, or certify obstruction.

The Johnson-graph formalization lane has a different frontier: replace or independently prove the upstream `sorryAx` dependencies before treating the proposed chromatic lower bound as formally established.

## Provenance

The SQS(20) material was first released in the general intake archive at `jaredwilder/unpublished-math-papers/erdos835-sqs20/`. It is promoted here because #835 now has a coherent multi-artifact research surface. The archive copy remains useful for provenance; this repository is the preferred problem-level home.

Author: Jared Wilder. First public timestamp: 2026-09-11.

## License

Apache-2.0.
