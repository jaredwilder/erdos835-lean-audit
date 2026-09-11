import Mathlib
import FormalConjectures.ErdosProblems.«835»
import JSpace835.Shadows
set_option maxRecDepth 4000000

namespace JSpace835Rep
open JSpace835

/- Shot 9: independent derived-design bridge. Fix 11 points; a Property-16
   coloring should induce a 17-color large set of S(4,5,21).  Different target,
   different Finset geometry, same possible global kill. -/
set_option maxHeartbeats 4000000 in
theorem property16_implies_largeS451 : Erdos835.Property 16 → LargeS451 := by
  intro h
  classical
  unfold Erdos835.Property at h
  rcases h with ⟨c,hc⟩
  unfold LargeS451 ExtensionRainbow KSubsets
  simp_all only [Nat.reduceMul, Nat.reduceAdd]
  aesop

end JSpace835Rep
