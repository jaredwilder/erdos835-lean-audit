# Rounds 31–40 Ledger

## Round 31 — Hoffman knife-edge; killed

Hypothesis: 5-colorability of a q=5 repair graph might be filtered by its least eigenvalue.

Result: the filter is automatic. For triple-block incidence M and residual adjacency A,

`M^T M = A + 4I`.

Since M is 1140×1425, nullity(M)≥285, so -4 is automatically an eigenvalue of A. Ordinary Hoffman equality cannot distinguish repair instances.

**Disposition:** KILL as discriminator; inherit incidence identity.

## Round 32 — hypergraph factorization lens

The q=5 residual graph is the line graph of a 5-regular, 4-uniform linear hypergraph on the 1140 triples. A 5-coloring is exactly a 5-edge-coloring/factorization into five perfect matchings, each matching being an SQS(20).

The three sacrificed classical systems already supply three factors; the task is a refactorization problem, not a cold construction.

**Disposition:** PASS; inherit refactorization lens.

## Round 33 — spectral kernel becomes trade space

`ker(M)` consists of signed block weights with zero sum over every triple, exactly the linear Steiner 3-trade condition. Therefore the -4 eigenspace from Round 31 is the trade space.

**Disposition:** PASS; trade basis becomes the mutation space.

## Round 34 — one-coordinate rigidity discovered

Freeze 14 of the explicit 15 SQS. Solve exactly for any alternative fifteenth system in the freed constituent plus the 570 holes.

Binary MILP excluding the zero trade returned infeasible for every constituent.

**Disposition:** provisional PASS; demanded independent certificate.

## Round 35 — one-coordinate rigidity independently certified

For each of all 15 constituents, reduce the 1140×855 homogeneous trade matrix modulo 5.

Uniform result:

- rank = 849
- nullity = 6
- all 5^6=15625 nullspace combinations exhaustively checked
- nonzero binary nullvectors = 0

**Disposition:** CLOSED finite theorem for this explicit P15.

## Round 36 — symmetry-compression attempt; killed

Tested the natural `AGL(1,5) × S4` coordinate actions coming from the reconstruction. Only identity preserved the full indexed 15-pack.

This does **not** prove the full automorphism group is trivial; it only kills the hoped-for obvious compression of 455 three-sacrifice cases.

**Disposition:** KILL shortcut.

## Round 37 — two-coordinate surgery splits

Exact affine GF(5) enumeration on selected low-nullity two-system residuals found only the two original systems for several cross-row pairs. But same-row pair (0,1) yielded a different SQS in the same pair union, exposing an internal Steiner trade.

**Disposition:** mixed; promoted pair-component analysis.

## Round 38 — all 105 pair trade profiles closed

Enumerated the block-sharing components of every constituent pair.

Exactly two profiles:

- 30 same-row pairs: `(30,30,225)` per side
- 75 cross-row pairs: `(285)` per side

Thus pairwise internal switching is completely classified for the explicit pack.

**Disposition:** CLOSED finite theorem for this P15.

## Round 39 — physical escape search

Defined gauge trades (preserve the 4275-block union) versus physical trades (import one or more of the 570 holes). One-coordinate rigidity proves no physical move can involve only one old constituent. Earlier repair-radius result forces a full large-set escape to replace at least three old constituents.

A capped q=5 search for a new SQS touching holes did not certify a solution or impossibility.

**Disposition:** INCONCLUSIVE search; inherit physical/gauge distinction.

## Round 40 — gold sweep / prior-art boundary

Targeted searches were run across large-set SQS literature, disjoint SQS constructions, intersections, and Steiner-trade literature.

Known/standard pieces were demoted from novelty:

- the Etzion–Hartman D(20)≥15 construction/lower bound;
- general Steiner trade theory and its linear incidence formulation;
- general SQS intersection/trade literature;
- the open status of a nontrivial explicit large set of SQS.

No targeted hit was found for the exact one-coordinate rigidity theorem, the complete `(30,30,225)` vs `(285)` pair-trade profile of this explicit pack, or the particular residual-completion/repair-radius packaging. These are therefore labeled **apparently new / novelty unclaimed pending specialist prior-art review**.

**Disposition:** preserve claims with explicit boundaries.
