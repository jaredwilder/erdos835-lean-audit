import Mathlib
import FormalConjectures.ErdosProblems.«835»
set_option maxRecDepth 4000000

open SimpleGraph

namespace JSpace835Rep
open JSpace835

/- Shot 10: the naked kernel close target.  This asks the current mathlib /
   FormalConjectures stack to bridge the ONE missing chromatic unit at k=16.
   No proof placeholders.  If it fails, the final goal is the exact formal frontier. -/
set_option maxHeartbeats 8000000 in
theorem k16_close_probe : ¬ Erdos835.Property 16 := by
  rw [← Erdos835.property_iff_chromaticNumber 16 (by omega)]
  intro hchi
  have hj := Erdos835.div_johnsonBound_le_chromaticNum_johnson (n:=32) (k:=16)
  have hbound : 17 ≤ J(32,16).chromaticNumber := by
    norm_num [Erdos835.johnsonBound] at hj ⊢
    exact hj
  -- If automation finds any hidden strictness theorem, this closes immediately.
  have : 18 ≤ J(32,16).chromaticNumber := by
    first | omega | aesop | exact?
  omega

end JSpace835Rep
