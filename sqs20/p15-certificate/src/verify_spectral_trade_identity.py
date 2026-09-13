#!/usr/bin/env python3
"""Verify the generic incidence identity for the representative q=5 residual instance.
M is triple-by-uncovered-block incidence. A is the residual block graph joining blocks sharing a triple.
Then M^T M = A + 4I, hence ker(M) is exactly the (-4)-eigenspace of A.
"""
import json,itertools,pathlib,collections
ROOT=pathlib.Path(__file__).resolve().parents[1]
systems=[[tuple(b) for b in S] for S in json.load(open(ROOT/'data/eh15_sqs20.json'))['systems']]
keep=[i for i in range(15) if i not in (0,1,2)]
used=set().union(*(set(systems[i]) for i in keep))
U=sorted(set(itertools.combinations(range(20),4))-used)
assert len(U)==1425
tr=collections.defaultdict(list)
for j,b in enumerate(U):
    for t in itertools.combinations(b,3): tr[t].append(j)
assert len(tr)==1140 and all(len(v)==5 for v in tr.values())
# Check every block has four incident triples; every adjacent pair arises from one shared triple.
deg=[0]*len(U); edges=set()
for vs in tr.values():
    for a,b in itertools.combinations(vs,2):
        if a>b:a,b=b,a
        assert (a,b) not in edges
        edges.add((a,b));deg[a]+=1;deg[b]+=1
assert all(d==16 for d in deg) and len(edges)==11400
# M has 1140 rows and 1425 cols => nullity >= 285 over every field / over R by rank-nullity.
res={"instance":"sacrifice systems 0,1,2","M_shape":[1140,1425],"residual_vertices":1425,"residual_edges":11400,"regular_degree":16,"identity":"M^T M = A + 4 I (verified combinatorially)","forced_nullity_lower_bound":285,"consequence":"A has eigenvalue -4; ker(M) equals the signed Steiner-trade space and the -4 eigenspace.","status":"PASS"}
json.dump(res,open(ROOT/'results/SPECTRAL_TRADE_IDENTITY.json','w'),indent=2)
print(json.dumps(res,indent=2))
