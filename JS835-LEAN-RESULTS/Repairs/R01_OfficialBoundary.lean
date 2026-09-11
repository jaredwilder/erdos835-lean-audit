import Mathlib
import FormalConjectures.ErdosProblems.«835»

open Finset SimpleGraph
open scoped Nat
namespace JSpace835R

-- REPAIR of shot 01. The original failed because `norm_num [johnsonBound]` reduced the
-- bound to 35357670 but left the NNRat ceiling-quotient unevaluated. Bridge it explicitly.

theorem jb32 : Erdos835.johnsonBound 32 4 16 = 35357670 := by norm_num [Erdos835.johnsonBound]
theorem ch32 : Nat.choose 32 16 = 601080390 := by norm_num [Nat.choose]

theorem boundary17 : (17 : ℕ∞) ≤ J(32,16).chromaticNumber := by
  have h := Erdos835.div_johnsonBound_le_chromaticNum_johnson (n:=32) (k:=16)
  rw [jb32, ch32] at h
  norm_num at h
  exact h

#print axioms jb32
#print axioms ch32
#print axioms boundary17

end JSpace835R
