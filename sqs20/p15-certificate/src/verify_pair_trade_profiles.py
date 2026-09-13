#!/usr/bin/env python3
"""Classify the Steiner trade-component profile of every pair among 15 SQS(20)."""
import json,itertools,collections,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
systems=[[tuple(b) for b in S] for S in json.load(open(ROOT/'data/eh15_sqs20.json'))['systems']]

def profile(a,b):
    tri=collections.defaultdict(list)
    verts=[(0,x) for x in systems[a]]+[(1,x) for x in systems[b]]
    for i,(side,bl) in enumerate(verts):
        for t in itertools.combinations(bl,3):tri[t].append(i)
    assert len(tri)==1140 and all(len(v)==2 for v in tri.values())
    adj=[[] for _ in verts]
    for x,y in tri.values(): adj[x].append(y); adj[y].append(x)
    assert all(len(v)==4 for v in adj)
    seen=set(); sizes=[]
    for i in range(570):
        if i in seen: continue
        st=[i];seen.add(i);n0=n1=0
        while st:
            x=st.pop();
            if verts[x][0]==0:n0+=1
            else:n1+=1
            for y in adj[x]:
                if y not in seen:seen.add(y);st.append(y)
        assert n0==n1
        sizes.append(n0)
    return tuple(sorted(sizes))

classes=collections.defaultdict(list)
for a,b in itertools.combinations(range(15),2): classes[profile(a,b)].append([a,b])
assert set(classes)=={(285,),(30,30,225)}
assert len(classes[(285,)])==75 and len(classes[(30,30,225)])==30
# Reconstruction indexing has three construction rows 0..4,5..9,10..14.
def same_row(a,b): return a//5==b//5
assert all(same_row(a,b) for a,b in classes[(30,30,225)])
assert all(not same_row(a,b) for a,b in classes[(285,)])
res={"theorem":"All 105 constituent pairs have exactly two trade-component types.","interpretation":{"same_construction_row":"three indecomposable trade components, per-side volumes 30,30,225","cross_construction_row":"one indecomposable trade component, per-side volume 285"},"classes":[{"profile":list(k),"pair_count":len(v),"pairs":v} for k,v in sorted(classes.items())],"status":"PASS"}
json.dump(res,open(ROOT/'results/PAIR_TRADE_PROFILES.json','w'),indent=2)
print(json.dumps(res,indent=2))
