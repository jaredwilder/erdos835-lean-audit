# One-Coordinate Rigidity of the Explicit 15-Pack

## Statement

Let `P={S_0,...,S_14}` be the explicit 15 pairwise-disjoint SQS(20) in `data/eh15_sqs20.json`.

For every index i:

> `S_i` is the unique SQS(20) disjoint from all fourteen systems `S_j` with `j≠i`.

This is a theorem about this explicit finite object, certified by exhaustive finite algebra over GF(5).

## Why the variables are only 855

The fourteen frozen systems occupy 3990 blocks. The only blocks available to a replacement SQS are:

- the 285 blocks of the removed system `S_i`, and
- the 570 blocks in the original hole set R.

An alternative system has the form `(S_i \ Y) ∪ X`, with `Y⊆S_i`, `X⊆R`.

For each triple t:

- exactly one `s(t)∈S_i` contains t;
- exactly two `r_1(t),r_2(t)∈R` contain t.

Therefore the SQS condition after replacement is equivalent to

`x_{r_1(t)} + x_{r_2(t)} = y_{s(t)}`

for all 1140 triples.

The zero vector is the original S_i. A distinct replacement is exactly a nonzero binary solution.

## Certificate

For each i:

1. Reduce the homogeneous system modulo 5.
2. Sparse row reduction yields rank 849 of 855 variables.
3. Hence the nullspace is 6-dimensional.
4. Enumerate all 5^6=15625 coefficient vectors in that nullspace.
5. Check whether all 855 coordinates land in `{0,1}`.
6. Only the zero vector passes.

Every integer binary solution would reduce to such a GF(5) binary solution, so absence modulo 5 proves absence over the integers.

See `results/ONE_COORDINATE_RIGIDITY.json` and `src/verify_one_coordinate_rigidity.py`.

## Claim boundary

- **Closed:** the finite rigidity statement for the exact P15 bytes shipped here.
- **Not claimed:** a theorem about all maximum/near-maximum 15-packs of SQS(20).
- **Novelty:** targeted search found no exact prior statement; novelty remains unclaimed pending specialist review.
