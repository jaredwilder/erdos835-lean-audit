# erdos835-lean-audit

**A ten-shot Lean run at Erdős 835, and the axiom audit that found the headline bound rests on a
`sorry` one import away.**

Author: Jared Wilder. Run date 2026-08-19. First public timestamp: 2026-09-11.

Erdős 835 asks about the chromatic number of the Johnson graph J(32,16). Ten proof attempts were
run locally against Lean 4.31.0-rc1 and a vendored copy of DeepMind's `formal-conjectures` tree.
**Five passed, five failed.** Then every green claim was audited, and the pass rate stopped being
the interesting number.

---

## Finding 0: "kernel-checked" is the wrong word for most of this packet

The packet states its claims as anonymous `example`s. **`#print axioms` cannot inspect an
`example`.** So a packet full of `example`s can compile green and tell you nothing at all about its
axiom footprint.

Every green claim was therefore restated as a **named theorem with the same statement and the same
proof** (`Audit/AxiomAudit.lean`) and its footprint printed. Result:

| claim | footprint | verdict |
|---|---|---|
| A02_fiber, A03_allSQS, A03_remainder, A01_jb, A01_choose, A01_ratio | `[native_decide ax]` | **not kernel** |
| A02_mod17, A03_disjoint, A04_k5 | `[..., native_decide ax]` | **not kernel** |
| A04_pigeonhole | `[propext, Classical.choice, Quot.sound]` | clean |
| A05_repair, A05_exact | `[propext, Quot.sound]` | clean |

**Nine of twelve are not kernel proofs.** `native_decide` does not run the kernel — it compiles the
decision procedure to C, runs the binary, and admits the answer through a generated axiom. It trusts
the Lean compiler and the CPU. The three clean ones are the arithmetically trivial claims.

## Finding 1: the 17 bound is not proved

Shot 01's headline `17 ≤ χ(J(32,16))` and shot 10's entire route both pass through three lemmas in
the vendored tree whose footprints contain **`sorryAx`**:

```
Erdos835.div_johnsonBound_le_chromaticNum_johnson  -> [propext, sorryAx, ...]
Erdos835.indepNum_johnson_le_johnsonBound          -> [propext, sorryAx, ...]
Erdos835.property_iff_chromaticNumber              -> [propext, sorryAx, ...]
```

`indepNum_johnson_le_johnsonBound` is **literally `:= sorry`** upstream. The premise that existing
machinery reaches 17 is an unproved premise.

Shot 01's arithmetic was repaired and it then **compiles green** — and its footprint still contains
`sorryAx`. A green exit here would have been a facade.

The packet's own contract, *"no sorry in the ten attempt files"*, is true and irrelevant. **The
sorry is one import away, in the dependency closure.** That is the general lesson and it is why this
repository exists.

## Finding 3: shot 10 is not hard, it is unsound — and that is now a theorem

Shot 10 assumes Property 16, i.e. χ = k+1 = 17, and then tries to derive 18 ≤ χ. Under its own
assumption the goal is false. Lean showed the residual goal literally as

```
hbound : 17 <= 16 + 1
|- 18 <= 16 + 1
```

`Repairs/R10b_DirectK16Verdict.lean` proves it properly:

```lean
shot10_route_is_unsound : G.chromaticNumber = 17 → ¬ (18 ≤ G.chromaticNumber)
```

footprint `[propext, Classical.choice, Quot.sound]` — **clean, no sorry, no native_decide.**

No tactic portfolio could ever have made shot 10 green. Any refutation of Property 16 needs strictly
more than the Johnson bound.

## Finding 4: two claims upgraded to zero axioms, and a real knife edge

Retrying shot 02's list arithmetic with plain `decide` (kernel evaluation) instead of
`native_decide`:

```
K02_fiber_kernel : does not depend on any axioms
K02_diff_kernel  : does not depend on any axioms
```

And recovered kernel-clean by `norm_num`:

```
johnsonBound 32 4 16 = 35357670      [propext, Classical.choice, Quot.sound]
Nat.choose 32 16     = 601080390     [propext]
```

**The 601080390 / 17 = 35357670 knife edge is real and kernel-certified.** What is *not* certified is
that this bound implies anything about χ — see Finding 1.

## What was fixed to make it run, recorded rather than hidden

Three genuine version-drift breaks in the vendored tree, all upstream changes rather than packet
faults: `Mathlib.Combinatorics.SimpleGraph.Coloring` was split and `chromaticNumber` moved;
`Irreflexive` became a class so a `simp +contextual` left metavariables; and a `simpa` no longer
normalised `bipartiteBelow` membership. Each was replaced with an explicit proof of the same fact.

Two packet defects were also worked around: a 4,275-block literal blew `maxRecDepth`, and
`List.get!` was removed from core Lean after v4.29 and had to be restored with its exact original
semantics.

**The requested toolchain was not used.** Lean 4.27.0 would have meant a ~5 GB Mathlib download and
the run used the Mathlib already on the machine. **These are 4.31.0-rc1 results, not 4.27.0
results**, and every claim above should be read with that attached.

## What this is not

This does not resolve Erdős 835, does not bound χ(J(32,16)), and does not claim the vendored
corpus is wrong — a `sorry` in a research formalization corpus is an ordinary, honest placeholder.
The finding is narrower and more useful: **a downstream proof that imports one inherits it, and an
anonymous `example` will never tell you.**

## License

Apache-2.0.
