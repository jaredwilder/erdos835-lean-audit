# Why the Hoffman Lane Dies: Spectral Slack = Trade Space

For the representative q=5 repair instance (retain 12 of the 15 systems), let U be the 1425 uncovered blocks.

Let M be the 1140×1425 incidence matrix:

`M[t,B]=1` iff triple t is contained in block B.

Let A be the adjacency matrix on U with `A[B,C]=1` iff B and C share a triple.

Distinct 4-sets share at most one triple, while every 4-set contains exactly four triples. Hence

`M^T M = A + 4I`.

Therefore:

`Az=-4z  <=>  M^T M z=0  <=>  Mz=0`.

The last equivalence holds over the reals because `z^T M^T M z = ||Mz||^2`.

But `Mz=0` says exactly that the signed multiplicity over blocks is zero above every triple: this is the linear Steiner 3-trade condition.

So:

> **The -4 Johnson/Hoffman eigenspace on the residual graph is exactly the real Steiner-trade space.**

This explains why the spectral bound is automatically tight for these repair graphs: the degrees of freedom needed to refactor designs are precisely the eigenvectors creating equality.

This identity is elementary incidence linear algebra; novelty is not claimed. Its value here is architectural: it tells J-SPACE to search the trade kernel rather than rerun spectral tests that are forced to be silent.
