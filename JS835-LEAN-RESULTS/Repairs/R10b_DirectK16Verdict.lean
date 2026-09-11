import Mathlib
import FormalConjectures.ErdosProblems.«835»

set_option maxRecDepth 4000000
open SimpleGraph
namespace JSpace835R10b

/- Shot 10, repaired. The original died on the same NNRat-ceiling gap as shot 01.
   With that gap bridged, we ask what shot 10 actually leaves to prove. -/

theorem jb32 : Erdos835.johnsonBound 32 4 16 = 35357670 := by
  norm_num [Erdos835.johnsonBound]

theorem ch32 : Nat.choose 32 16 = 601080390 := by norm_num [Nat.choose]

/-- The Johnson bound, correctly evaluated, delivers exactly 17 -- never 18. -/
theorem johnson_gives_exactly_17 : (17 : ℕ∞) ≤ J(32,16).chromaticNumber := by
  have h := Erdos835.div_johnsonBound_le_chromaticNum_johnson (n:=32) (k:=16)
  rw [jb32, ch32] at h
  norm_num at h
  exact h

/-- THE VERDICT ON SHOT 10.
    Shot 10 assumes `Property 16` (equivalently chi = k+1 = 17) and then tries to reach
    `18 <= chi`. Under that very assumption `18 <= chi` is FALSE, not merely hard.
    The route is therefore not defeated by weak automation -- it is unsound as a closing
    strategy, and no tactic portfolio could ever have made it green. -/
theorem shot10_route_is_unsound {V : Type} (G : SimpleGraph V)
    (h : G.chromaticNumber = 17) : ¬ ((18 : ℕ∞) ≤ G.chromaticNumber) := by
  rw [h]
  decide

/-- Same fact stripped of all graph theory. -/
theorem seventeen_never_gives_eighteen : ¬ ((18 : ℕ∞) ≤ 17) := by decide

#print axioms jb32
#print axioms ch32
#print axioms johnson_gives_exactly_17
#print axioms shot10_route_is_unsound
#print axioms seventeen_never_gives_eighteen

end JSpace835R10b
