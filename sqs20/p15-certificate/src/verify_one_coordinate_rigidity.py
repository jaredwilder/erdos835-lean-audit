#!/usr/bin/env python3
"""Exact finite certificate for one-coordinate rigidity of the explicit P15.

For each constituent S_i, keeping the other 14 systems fixed leaves exactly
S_i plus the original 570 holes available. Any alternative SQS differs from
S_i by a binary trade vector (x_holes,y_removed) satisfying, for every triple t,
    x_r1(t)+x_r2(t)-y_s(t)=0.
We reduce this homogeneous system mod 5, compute sparse RREF, and enumerate the
5^6 nullspace combinations. If no nonzero null vector has every coordinate in
{0,1}, then no nonzero binary integer trade exists.
"""
import json,itertools,collections,pathlib
ROOT=pathlib.Path(__file__).resolve().parents[1]
systems=[[tuple(b) for b in S] for S in json.load(open(ROOT/'data/eh15_sqs20.json'))['systems']]
all4=set(itertools.combinations(range(20),4)); union=set().union(*(set(S) for S in systems)); R=sorted(all4-union); ridx={b:i for i,b in enumerate(R)}
rt=collections.defaultdict(list)
for b in R:
    for t in itertools.combinations(b,3): rt[t].append(b)
triples=list(itertools.combinations(range(20),3))
assert len(R)==570 and all(len(rt[t])==2 for t in triples)

def rref_echelon(si,p=5):
    S=systems[si]; sidx={b:i for i,b in enumerate(S)}; st={}
    for b in S:
        for t in itertools.combinations(b,3): st[t]=b
    rows=[]
    for t in triples:
        b1,b2=rt[t]
        rows.append({ridx[b1]:1,ridx[b2]:1,570+sidx[st[t]]:(p-1)})
    piv={}; inv={a:pow(a,-1,p) for a in range(1,p)}
    for row in rows:
        while row:
            c=min(row)
            if c not in piv:
                a=row[c]; ia=inv[a]
                if a!=1: row={j:(v*ia)%p for j,v in row.items() if (v*ia)%p}
                piv[c]=row; break
            pr=piv[c]; factor=row[c]
            for j,v in pr.items():
                nv=(row.get(j,0)-factor*v)%p
                if nv: row[j]=nv
                elif j in row: del row[j]
    free=[j for j in range(855) if j not in piv]
    return piv,free

def basis_from(piv,free,p=5):
    bs=[]
    for f in free:
        x=[0]*855; x[f]=1
        for c in sorted(piv,reverse=True):
            s=sum(v*x[j] for j,v in piv[c].items() if j!=c)%p
            x[c]=(-s)%p
        bs.append(x)
    return bs

def certify(si,p=5):
    piv,free=rref_echelon(si,p); bs=basis_from(piv,free,p)
    nonzero_binary=[]
    for coeff in itertools.product(range(p),repeat=len(free)):
        if not any(coeff): continue
        ok=True
        for j in range(855):
            v=sum(coeff[i]*bs[i][j] for i in range(len(bs)))%p
            if v not in (0,1): ok=False; break
        if ok:
            nonzero_binary.append(coeff); break
    return {"system":si,"field":p,"variables":855,"equations":1140,"rank":len(piv),"nullity":len(free),"free_coordinates":free,"nonzero_binary_nullvectors":len(nonzero_binary),"rigid":len(nonzero_binary)==0}

out=[certify(i) for i in range(15)]
assert all(x['rank']==849 and x['nullity']==6 and x['rigid'] for x in out)
res={"theorem":"Every 14-subpack of this explicit 15-pack has the original missing constituent as its unique disjoint SQS(20) completion.","method":"GF(5) sparse RREF + exhaustive 5^6 nullspace enumeration for each constituent","systems":out,"status":"PASS"}
json.dump(res,open(ROOT/'results/ONE_COORDINATE_RIGIDITY.json','w'),indent=2)
print(json.dumps(res,indent=2))
