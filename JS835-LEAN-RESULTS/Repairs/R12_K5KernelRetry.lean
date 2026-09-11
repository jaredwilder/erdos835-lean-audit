import Mathlib
import JSpace835.Compute

set_option maxRecDepth 40000000

namespace JSpace835KC2
open JSpace835

/- The packet proves its finite facts with `native_decide`, which does NOT go through the
   Lean kernel: it compiles the decision procedure to C, runs it, and trusts the answer via
   a generated `ofReduceBool`-style axiom. Here we retry the cheapest ones with plain
   `decide`, which the KERNEL evaluates. A green result here is a strictly stronger claim
   than the packet's. Anything that does not fit is reported as not-attempted, never as passed. -/

-- Shot 4 substrate: only 4 cliques of 5 blocks each. Smallest target, tried first.
set_option maxHeartbeats 0 in
theorem K04_k5_kernel : knownK5sValid = true := by decide

-- Shot 2 substrate: pure 17-element list arithmetic, no P15 data.
theorem K02_fiber_kernel : List.zipWith (fun a b => a + 16*b)
    [1,0,8,32,108,256,472,672,758,672,472,256,108,32,8,0,1]
    [0,1,7,33,107,257,471,673,757,673,471,257,107,33,7,1,0] =
    (List.range 17).map (Nat.choose 16) := by decide

theorem K02_diff_kernel : List.zipWith (fun a b => (a:ℤ) - (b:ℤ))
    [1,0,8,32,108,256,472,672,758,672,472,256,108,32,8,0,1]
    [0,1,7,33,107,257,471,673,757,673,471,257,107,33,7,1,0] =
    [1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1,-1,1] := by decide

#print axioms K04_k5_kernel
#print axioms K02_fiber_kernel
#print axioms K02_diff_kernel

end JSpace835KC2
