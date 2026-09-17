# Erdős #835 — SQS(20) completion and Johnson-graph formalization

Two complementary pieces of work around Erdős #835: an exact finite program for completing a 15-pack of Steiner quadruple systems on 20 points, and an audit of a Lean route through the Johnson graph `J(32,16)`.

## Residual-graph completion theorem

Let

\[
P=\{S_1,\ldots,S_m\}
\]

be pairwise block-disjoint Steiner quadruple systems on `v` points and set

\[
q=v-3-m.
\]

Construct the residual graph `R(P)` whose vertices are the uncovered 4-subsets, with two residual blocks adjacent when they share a triple.

Then

> `P` extends to a large set of `SQS(v)` if and only if `χ(R(P))=q`.

Moreover,

\[
|V(R)|=q\binom v3/4,
\]

\[
\deg R=4(q-1),
\]

and

\[
|E(R)|=\binom v3\binom q2.
\]

The proof is in [`sqs20/RESIDUAL-GRAPH-THEOREM.md`](sqs20/RESIDUAL-GRAPH-THEOREM.md).

## Exact results for the reconstructed 15-pack

The explicit pack contains

```text
15 systems × 285 blocks = 4,275 covered 4-sets.
```

Exactly 570 four-sets remain uncovered. For the corresponding `q=2` residual graph:

- the graph is 4-regular;
- component sizes are `250, 25×12, 5×4`;
- the four `K5` components show that this particular 15-pack cannot be completed merely by adding two further systems.

Any large set retaining systems from this pack can retain at most 12 of the 15; at least three constituents must change.

## Rigidity and pair trades

Every 14-subpack uniquely forces the fifteenth system. The associated `1140×855` linear systems have GF(5) rank 849 and nullity 6; all `5^6=15,625` nullspace coefficient combinations were checked with no nonzero binary trade.

All

\[
\binom{15}{2}=105
\]

pair unions fall into two exact trade profiles:

- 30 same-row pairs with per-side volumes `(30,30,225)`;
- 75 cross-row pairs with one indecomposable per-side volume-285 component.

For the `q=5` repair graph, the incidence identity

\[
M^TM=A+4I
\]

identifies the `-4` eigenspace with the linear Steiner 3-trade space.

## Verification

The explicit 15-system pack, four original verifiers, receipts, and source notes are preserved under `sqs20/`.

```sh
python verification/verify_p15_source.py
python verification/replay_p15.py
```

The replay checks the pack, all 15 GF(5) rigidity systems, all 105 pair-trade profiles, the representative spectral identity, and the residual graph reconstruction.

## Johnson-graph Lean audit

Ten Lean attempts around `J(32,16)` were inspected under Lean 4.31.0-rc1.

The proposed lower bound

\[
17\le\chi(J(32,16))
\]

is not completed by the current formal files because it depends on upstream theorems containing `sorryAx`, including `indepNum_johnson_le_johnsonBound`.

The audit does recover several clean finite statements, including

```text
johnsonBound 32 4 16 = 35357670
Nat.choose 32 16 = 601080390.
```

The formal sources are under [`JS835-LEAN-RESULTS/`](JS835-LEAN-RESULTS/).

## Remaining finite problem

The next unresolved SQS(20) case is the `q=5` repair regime: determine whether changing three systems can make the residual graph 5-colorable, or prove that no such repair exists.

The Johnson-graph route has a separate task: replace the upstream `sorryAx` dependencies before using it as a formal proof of the chromatic lower bound.

Author: Jared Wilder. License: Apache-2.0.
