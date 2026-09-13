#!/usr/bin/env python3
import subprocess,sys,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
for f in ['verify_pack.py','verify_one_coordinate_rigidity.py','verify_pair_trade_profiles.py','verify_spectral_trade_identity.py']:
    print('===',f,'===')
    subprocess.run([sys.executable,str(ROOT/'src'/f)],check=True)
print('ALL CORE R31-R40 CERTIFICATES: PASS')
