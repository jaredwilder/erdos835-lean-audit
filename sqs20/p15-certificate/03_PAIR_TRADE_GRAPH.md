# Complete Pair-Trade Geometry of the Explicit 15-Pack

## Construction

For disjoint SQS(20) systems A and B, construct a graph Γ(A,B):

- vertices are the 570 blocks in A∪B;
- two blocks are adjacent iff they share a triple.

Every triple belongs to exactly one block of A and one block of B, so Γ is bipartite with sides A and B. Every block contains four triples, hence Γ is 4-regular.

A connected component contains equally many A- and B-blocks. Swapping the two sides of a component preserves every triple count. Thus each connected component is an indecomposable Steiner 3-(20,4) trade.

## Exhaustive result

All C(15,2)=105 pairs were enumerated.

### Type I — same reconstruction row

30 pairs, exactly those with both indices in one of

- {0,1,2,3,4}
- {5,6,7,8,9}
- {10,11,12,13,14}

have three components with per-side volumes

`30, 30, 225`.

Consequences:

- the pair union contains `2^3=8` SQS when side choices are counted as labeled choices;
- equivalently four unordered decompositions into two disjoint SQS;
- the two volume-30 components are small internal gauge switches.

### Type II — cross reconstruction row

75 pairs have one connected component of per-side volume

`285`.

Therefore their union is indecomposable as a pair trade; within that fixed union, the only two complementary SQS are the original pair (up to swapping labels).

## Claim boundary

This is an exact exhaustive classification for the explicit bytes in this release. It is not claimed to classify arbitrary pairs of SQS(20).
