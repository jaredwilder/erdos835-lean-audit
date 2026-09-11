import Mathlib
import FormalConjectures.ErdosProblems.«835»
import JSpace835.Compute

set_option maxRecDepth 1000000

open Finset SimpleGraph
open scoped Nat

namespace JSpace835Audit
open JSpace835

-- The packet uses anonymous `example`s, which cannot be inspected by `#print axioms`.
-- Restated here as NAMED theorems with the SAME statements and SAME proofs, so the
-- axiom footprint of every green claim is visible.

theorem A02_fiber : List.zipWith (fun a b => a + 16*b)
    [1,0,8,32,108,256,472,672,758,672,472,256,108,32,8,0,1]
    [0,1,7,33,107,257,471,673,757,673,471,257,107,33,7,1,0] =
    (List.range 17).map (Nat.choose 16) := by native_decide

theorem A02_mod17 : (List.range 17).map
    (fun d => ((-1 : ZMod 17)^d) * (Nat.choose 16 d : ZMod 17)) =
    List.replicate 17 1 := by native_decide

theorem A03_allSQS : p15AllSQS = true := by native_decide
theorem A03_disjoint : p15PairwiseDisjoint = true := by native_decide
theorem A03_remainder : remainder.length = 570 := by native_decide
theorem A04_k5 : knownK5sValid = true := by native_decide

theorem A04_pigeonhole : ¬ ∃ f : Fin 5 → Fin 4, Function.Injective f := by
  intro h
  rcases h with ⟨f,hf⟩
  have hcard := Fintype.card_le_of_injective f hf
  norm_num at hcard

theorem A05_repair : ∀ m : Nat, 13 ≤ m → m ≤ 15 → 17 - m < 5 := by omega
theorem A05_exact : 17 - 12 = 5 := by omega

theorem A01_jb : Erdos835.johnsonBound 32 4 16 = 35357670 := by native_decide
theorem A01_choose : Nat.choose 32 16 = 601080390 := by native_decide
theorem A01_ratio : Nat.choose 32 16 / 17 = 35357670 := by native_decide

#print axioms A02_fiber
#print axioms A02_mod17
#print axioms A03_allSQS
#print axioms A03_disjoint
#print axioms A03_remainder
#print axioms A04_k5
#print axioms A04_pigeonhole
#print axioms A05_repair
#print axioms A05_exact
#print axioms A01_jb
#print axioms A01_choose
#print axioms A01_ratio

-- THE LOAD-BEARING UPSTREAM LEMMAS that shots 01 and 10 lean on.
#print axioms Erdos835.div_johnsonBound_le_chromaticNum_johnson
#print axioms Erdos835.indepNum_johnson_le_johnsonBound
#print axioms Erdos835.property_iff_chromaticNumber

end JSpace835Audit
