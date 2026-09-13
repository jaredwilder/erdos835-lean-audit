# Exact rigidity and trade geometry of the explicit SQS(20) 15-pack

Let `P={S_0,...,S_14}` be the explicit reconstructed 15-pack of pairwise-disjoint SQS(20), and let `R` denote the 570 four-subsets outside its 4,275-block union.

## Theorem A — one-coordinate rigidity

Fix `i` and freeze the other fourteen systems. Any alternative SQS(20) disjoint from those fourteen must use only blocks from `S_i union R`.

For each triple `t` there is one old block `s(t) in S_i` and exactly two hole blocks `r_1(t),r_2(t) in R`, producing the homogeneous trade equation

`x_{r_1(t)} + x_{r_2(t)} - y_{s(t)} = 0`.

For every one of the 15 choices of `i`, the resulting `1140 x 855` matrix has, over `GF(5)`, rank `849` and nullity `6`. All `5^6=15625` nullspace coefficient combinations were exhaustively checked. None gives a nonzero vector whose 855 coordinates all lie in `{0,1}`.

> **For every `i`, the only SQS(20) disjoint from `P\{S_i}` is `S_i` itself.**

Equivalently, every 14-subpack of this explicit 15-pack uniquely forces its fifteenth constituent. This is an exact finite algebraic certificate, not a search timeout.

## Theorem B — complete pair-trade geometry

For any pair `S_i,S_j`, form the block graph on their 570 blocks, joining blocks when they share a triple. Every triple occurs once in each SQS, so this graph is bipartite and 4-regular. Its connected components are exactly the indecomposable Steiner 3-trades between the two systems.

Exact enumeration of all `C(15,2)=105` pairs yields only two profiles:

- **30 same-construction-row pairs:** per-side component volumes `(30,30,225)`;
- **75 cross-construction-row pairs:** one indecomposable per-side volume-285 component.

Thus the 105 pair unions have exactly two Steiner-trade geometries, determined by whether the pair lies in the same reconstruction row.

Same-row pairs admit two independent volume-30 switches plus one volume-225 component. Every cross-row pair is indecomposable within its own union.

## Gauge versus physical trades

A trade that only redistributes blocks among existing constituents while preserving the total 4,275-block union leaves the same 570 holes. Such a trade cannot remove the `K5` obstruction in the original `q=2` residual graph.

Any route from this 15-pack toward a full large set must instead perform a physical trade that imports at least one of the 570 holes and changes the union itself. Combined with the repair-radius theorem (`m<=12` for retained members), any full-large-set escape from this basin must alter at least three old constituents simultaneously.

## Incidence / spectral identity and trade space

For a representative `q=5` repair graph, let `M` be the `1140 x 1425` triple-versus-uncovered-block incidence matrix and let `A` be the residual adjacency matrix. Then

`M^T M = A + 4I`.

Since `M` has more columns than rows, `-4` is automatically an eigenvalue of `A`; this kills a naive Hoffman-bound discriminator. More importantly, `ker(M)` consists exactly of signed block weights summing to zero over every triple: the linear Steiner 3-trade space. Thus the `-4` eigenspace is precisely the design-preserving mutation space.

## Open frontier

The natural `AGL(1,5) x S4` coordinate actions were tested against the indexed 15-pack; only identity survived. That does not determine the full automorphism group. No physical three-system trade touching the hole set was certified, no representative `q=5` repair graph was proved 5-colorable or non-5-colorable, and the 455 three-system sacrifices were not exhaustively classified.

## Provenance and literature status

General Steiner-trade theory is classical. The source's targeted search did not locate the exact one-coordinate rigidity theorem or the complete `(30,30,225)` versus `(285)` profile for this explicit 15-pack. Priority is not claimed without specialist design-theory review.

Original intake copy: `jaredwilder/unpublished-math-papers/erdos835-sqs20/P15-RIGIDITY-AND-TRADES.md`.

## Recovered computational authority

The exact pack and original verifiers are now public in
[p15-certificate/](p15-certificate/). The
[source manifest](P15-SOURCE-MANIFEST.json) preserves ZIP provenance and file
hashes. The [fresh replay](../verification/P15-REPLAY-2026-09-13.json) checks
all 15 rigidity cases, all 105 pair profiles, the incidence identity and an
independent reconstruction of the four residual `K5` obstructions.
Run `python verification/replay_p15.py` from the repository root.
