#!/usr/bin/env python3
import json,itertools,collections,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
D=json.load(open(ROOT/'data/eh15_sqs20.json'))
systems=[[tuple(b) for b in S] for S in D['systems']]
assert len(systems)==15
triples=list(itertools.combinations(range(20),3))
all4=set(itertools.combinations(range(20),4))
seen=set(); triple_counts=collections.Counter()
for i,S in enumerate(systems):
    assert len(S)==285, (i,len(S))
    assert len(set(S))==285
    assert not (seen & set(S)), i
    seen |= set(S)
    c=collections.Counter(t for b in S for t in itertools.combinations(b,3))
    assert set(c)==set(triples)
    assert all(v==1 for v in c.values())
    triple_counts.update(c)
R=all4-seen
assert len(seen)==4275 and len(R)==570
assert all(triple_counts[t]==15 for t in triples)
rt=collections.Counter(t for b in R for t in itertools.combinations(b,3))
assert all(rt[t]==2 for t in triples)
print(json.dumps({"systems":15,"blocks_per_system":285,"union_blocks":len(seen),"remainder_blocks":len(R),"triples":len(triples),"coverage_per_triple":15,"remainder_blocks_per_triple":2,"status":"PASS"},indent=2))
