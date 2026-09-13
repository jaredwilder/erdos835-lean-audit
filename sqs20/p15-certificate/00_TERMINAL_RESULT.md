# J-SPACE v0.7 — Erdős #835 — Rounds 31–40 Terminal Result

## Verdict

**Erdős #835 is not closed.** The k=16 prime-regime case survives.

The ten-round block did, however, produce two exact finite rigidity results about the explicit reconstructed 15-pack of pairwise-disjoint SQS(20), plus a sharper description of the only kind of move that can possibly escape its basin.

## Gold theorem A — one-coordinate rigidity

Let `P={S_0,...,S_14}` be the explicit reconstructed 15-pack contained in this release, and let `R` be the 570 4-sets outside its union.

For every i, freeze the other fourteen systems. Any SQS(20) disjoint from those fourteen must lie in `S_i ∪ R`. Write `y_s=1` when an old block `s∈S_i` is removed and `x_r=1` when a hole `r∈R` is inserted. For each triple t there is one old block `s(t)∈S_i` and exactly two hole blocks `r_1(t),r_2(t)∈R`, giving

`x_{r_1(t)} + x_{r_2(t)} - y_{s(t)} = 0`.

For each of all 15 choices of i, the resulting 1140×855 matrix has rank 849 over GF(5), hence nullity 6. Exhaustion of all 5^6 nullspace coefficient vectors finds no nonzero vector whose 855 coordinates all lie in {0,1}.

Therefore the only binary trade is zero.

> **Theorem A.** For every i, the only SQS(20) disjoint from the fourteen systems `P\{S_i}` is `S_i` itself.

Equivalently: **every 14-subpack of this explicit P15 uniquely forces its fifteenth constituent.**

This is stronger than a failed search for a local mutation; it is an exact finite algebraic certificate.

## Gold theorem B — complete pair-trade geometry

For any two constituent SQS `S_i,S_j`, make the block graph on their 570 blocks, joining two blocks when they share a triple. Because each triple occurs once in each system, the graph is bipartite and 4-regular. Its connected components are precisely indecomposable Steiner 3-trades between the two systems.

Exact enumeration of all C(15,2)=105 pairs yields only two component profiles:

- **30 same-construction-row pairs:** per-side trade volumes `(30,30,225)`.
- **75 cross-construction-row pairs:** one indecomposable component of per-side volume `(285)`.

Thus same-row pairs admit two small independent volume-30 switches plus one volume-225 component, whereas every cross-row pair is indecomposable inside its own union.

> **Theorem B.** The 105 pair unions in this explicit P15 have exactly two Steiner-trade geometries, determined by whether the pair lies in the same reconstruction row.

## Gold structural interpretation — gauge vs physical trades

A trade that only redistributes blocks between existing constituents while preserving the total 4275-block union leaves the same 570 holes. Such a move cannot remove the K5 obstruction in the original q=2 residual graph. We call these **gauge trades**.

Any path from this P15 toward a full large set must therefore perform a **physical trade**: it must import blocks from the 570-hole set and change the union itself.

Combined with the Round-28/30 repair-radius theorem, a full large set retaining members of this P15 can retain at most 12 of them. Thus any physical escape requires simultaneous surgery at depth at least 3.

## Gold reinterpretation of the dead spectral lane

For a q=5 repair instance, let M be the 1140×1425 triple-vs-uncovered-block incidence matrix and A the 1425-vertex residual block graph. Combinatorially,

`M^T M = A + 4 I`.

Hence `ker(M)` is exactly the `-4` eigenspace of A. But `Mz=0` is precisely the signed Steiner 3-trade condition. Thus the automatic Hoffman equality is not a mystery or a useful filter: the spectral slack is exactly the trade space in which design-preserving repairs live.

This converts a killed spectral attack into the correct mutation space for future J-SPACE rounds.

## What did not close

- No physical three-system trade importing holes was certified.
- No 5-coloring of the representative 1425-vertex q=5 repair graph was found or ruled out.
- No exhaustive proof over all 455 three-system sacrifices was completed.
- No global impossibility or construction of LS(SQS(20)) was obtained.
- Therefore Erdős #835 remains open.

## Recommended next attack

Do **not** return to naked 5-color search. Parameterize physical trades directly in `ker(M)` and optimize for support intersecting the 570 holes, with the one-coordinate rigidity and pair-component classification as hard pruning rules. The first decisive target is:

> Find or rule out the minimum-support physical trade touching the hole set and at least three constituent systems.

That is the smallest mutation capable of changing the known obstruction.
