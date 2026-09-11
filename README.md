# Erdős 835 Lean axiom audit

A formal-methods audit of ten Lean proof attempts around Erdős 835. The central finding is that the apparent `17 ≤ χ(J(32,16))` proof depends on an upstream `sorry`, while several smaller arithmetic statements can be recovered with clean axiom footprints.

Author: Jared Wilder. Run date 2026-08-19. First public timestamp: 2026-09-11.

Erdős 835 concerns the chromatic number of the Johnson graph `J(32,16)`. Ten local proof attempts were tested against Lean 4.31.0-rc1 and a vendored copy of DeepMind's `formal-conjectures` tree. Five compiled and five did not. The axiom audit then examined what the successful files actually depended on.

## 1. Anonymous `example`s hide axiom footprints

The original files stated many claims as anonymous `example`s. `#print axioms` cannot inspect an anonymous example directly, so compilation alone did not expose their dependency footprints.

`Audit/AxiomAudit.lean` restates every successful claim as a named theorem with the same proposition and proof, then prints its axioms.

| claim | footprint | status |
|---|---|---|
| `A02_fiber`, `A03_allSQS`, `A03_remainder`, `A01_jb`, `A01_choose`, `A01_ratio` | `[native_decide ax]` | compiler-evaluated finite check |
| `A02_mod17`, `A03_disjoint`, `A04_k5` | `[..., native_decide ax]` | compiler-evaluated finite check |
| `A04_pigeonhole` | `[propext, Classical.choice, Quot.sound]` | clean classical footprint |
| `A05_repair`, `A05_exact` | `[propext, Quot.sound]` | clean footprint |

Nine of the twelve named claims use `native_decide`. That is a legitimate finite verification method, but it trusts compiled evaluation rather than reducing the result entirely through the Lean kernel.

## 2. The proposed 17 lower bound inherits `sorryAx`

The route to

```text
17 <= χ(J(32,16))
```

uses three lemmas from the vendored source tree whose axiom footprints contain `sorryAx`:

```text
Erdos835.div_johnsonBound_le_chromaticNum_johnson
Erdos835.indepNum_johnson_le_johnsonBound
Erdos835.property_iff_chromaticNumber
```

In particular, `indepNum_johnson_le_johnsonBound` is defined upstream with `:= sorry`.

So the downstream Lean file does **not** constitute a completed proof of the lower bound. Repairing local arithmetic makes the file compile, but it does not remove the unproved imported premise.

The general lesson is straightforward: the axiom footprint must be inspected through the full dependency closure, not only by searching the local file for the literal word `sorry`.

## 3. One proposed route is inconsistent with its own assumption

A later attempt assumes

```text
χ(J(32,16)) = 17
```

and then tries to derive `18 <= χ(J(32,16))`. Under the assumption, that target is false.

`Repairs/R10b_DirectK16Verdict.lean` states the correct result:

```lean
shot10_route_is_unsound : G.chromaticNumber = 17 → ¬ (18 ≤ G.chromaticNumber)
```

with footprint

```text
[propext, Classical.choice, Quot.sound].
```

Thus the issue is mathematical inconsistency in the proposed route, not tactic choice.

## 4. Clean finite arithmetic recovered

Replacing `native_decide` with kernel `decide` recovers two finite list statements with zero axioms:

```text
K02_fiber_kernel : no axioms
K02_diff_kernel  : no axioms
```

Two numerical identities are also recovered cleanly:

```text
johnsonBound 32 4 16 = 35357670
Nat.choose 32 16     = 601080390
```

The equality

```text
601080390 / 17 = 35357670
```

is therefore formally secure. What remains unproved is the imported theorem connecting that numerical Johnson bound to the desired chromatic-number inequality.

## 5. Toolchain and compatibility notes

The vendored source required three compatibility repairs under Lean 4.31.0-rc1:

- `Mathlib.Combinatorics.SimpleGraph.Coloring` had been split and `chromaticNumber` moved;
- `Irreflexive` had become a class, changing simplification behavior;
- a `simpa` no longer normalized `bipartiteBelow` membership automatically.

Two local implementation issues were also repaired: a 4,275-block literal exceeded `maxRecDepth`, and historical use of `List.get!` required restoration of the old semantics.

The requested Lean 4.27.0 environment was not used; these audit results are specifically for **Lean 4.31.0-rc1** with the available Mathlib environment.

## Mathematical conclusion

This repository does not supply a new bound for `χ(J(32,16))`. Its contribution is the formal audit itself:

- the proposed 17-bound derivation inherits an upstream `sorryAx`;
- nine smaller finite claims use `native_decide` rather than pure kernel reduction;
- three smaller claims have clean classical footprints;
- two finite claims can be strengthened to zero-axiom kernel evaluation;
- one proposed route is formally refuted under its own assumption.

That is a concrete dependency and proof-status result for the Erdős 835 formalization lane.

## License

Apache-2.0.