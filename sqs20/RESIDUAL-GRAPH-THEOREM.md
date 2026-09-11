# Residual graph equivalence for partial large sets of SQS

Let `X` have `v` points and let

`P={S_1,...,S_m}`

be pairwise block-disjoint Steiner quadruple systems on `X`.

A large set contains `v-3` systems: every triple lies in exactly `v-3` four-subsets, while each SQS selects exactly one containing block for each triple.

Set

`q=v-3-m`.

Let `U` be the uncovered four-subsets of `X`. Define the residual graph `R(P)` by

- vertices: blocks `B in U`;
- edge `BC`: `B` and `C` contain a common triple.

Two distinct four-subsets share at most one triple.

## Fibre structure

Fix a triple `T`. Exactly `m` of the `v-3` four-subsets containing `T` have been used by the `m` disjoint SQS. Hence exactly `q` uncovered blocks contain `T`, and they form a clique `K_q` in `R(P)`.

Conversely every uncovered block contains four triples, so it belongs to four such cliques. Double counting gives

`|U| = q*C(v,3)/4`.

Each residual block is adjacent to the other `q-1` choices over each of its four triples, so

`deg R(P)=4(q-1)`.

Each triple contributes a complete graph on its `q` uncovered alternatives; because two blocks share at most one triple,

`|E(R(P))| = C(v,3) C(q,2)`.

## Completion theorem

Suppose `P` extends by `q` disjoint SQS `T_1,...,T_q`. Color each uncovered block by the `T_i` containing it. Two blocks sharing a triple cannot belong to the same SQS, so this is a proper `q`-coloring of `R(P)`.

Conversely, suppose `R(P)` has a proper `q`-coloring. Every triple fibre is a `K_q`; with only `q` colors, each color appears exactly once on that fibre. For each color `i`, collect all uncovered blocks of color `i`. Every triple occurs in exactly one such block, so that color class is an SQS(v). The `q` color classes are disjoint and fill every uncovered block.

Therefore

> **`P` extends to a large set iff `chi(R(P))=q`.**

For `q=2` this reduces to ordinary bipartiteness.

## Evidence and provenance

This is an elementary proof extracted from the 2026-09-11 public estate release. The original intake copy remains in `jaredwilder/unpublished-math-papers/erdos835-sqs20/` for provenance. Historical novelty is a separate design-theory literature question.
