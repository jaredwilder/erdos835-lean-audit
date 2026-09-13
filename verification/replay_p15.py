"""Replay exact finite P15 checks in a temporary copy, preserving old receipts."""
import collections,hashlib,itertools,json,shutil,subprocess,sys,tempfile
from pathlib import Path
root=Path(__file__).resolve().parents[1]
source=root/'sqs20/p15-certificate'
with tempfile.TemporaryDirectory(prefix='sqs20-replay-') as work:
    work=Path(work)
    assert work.resolve().parent==Path(tempfile.gettempdir()).resolve()
    packet=work/'packet'
    shutil.copytree(source,packet)
    checks={}
    for name in ['verify_pack','verify_one_coordinate_rigidity','verify_pair_trade_profiles','verify_spectral_trade_identity']:
        print('Running '+name,file=sys.stderr,flush=True)
        out=subprocess.check_output([sys.executable,'-B',str(packet/'src'/f'{name}.py')],encoding='utf-8')
        checks[name]=json.loads(out)
        assert checks[name]['status']=='PASS'
    for name in ['ONE_COORDINATE_RIGIDITY','PAIR_TRADE_PROFILES','SPECTRAL_TRADE_IDENTITY']:
        assert json.loads((packet/'results'/f'{name}.json').read_text())==json.loads((source/'results'/f'{name}.json').read_text()),name

# Independent reconstruction of the residual graph and its K5 obstruction.
systems=json.loads((source/'data/eh15_sqs20.json').read_text())['systems']
assert len(systems)==15
used=set()
for s in systems:
    assert len(s)==285
    for b in s:
        assert len(b)==4 and b==sorted(set(b)) and all(0<=x<20 for x in b)
        assert tuple(b) not in used
        used.add(tuple(b))
holes=sorted(set(itertools.combinations(range(20),4))-used)
incident=collections.defaultdict(list)
for i,b in enumerate(holes):
    for t in itertools.combinations(b,3):incident[t].append(i)
assert len(holes)==570 and len(incident)==1140 and all(len(v)==2 for v in incident.values())
adj=[set() for _ in holes]
for a,b in incident.values():adj[a].add(b);adj[b].add(a)
assert all(len(v)==4 for v in adj)
unseen=set(range(len(holes))); components=[]
while unseen:
    todo=[min(unseen)];unseen.remove(todo[0]);component=[]
    while todo:
        v=todo.pop();component.append(v)
        for w in sorted(adj[v]):
            if w in unseen:unseen.remove(w);todo.append(w)
    components.append(sorted(component))
sizes=sorted(map(len,components))
assert sizes==[5]*4+[25]*12+[250]
cliques=[c for c in components if len(c)==5]
assert all(set(c)-{v} <= adj[v] for c in cliques for v in c)
out={'result':'PASS','scope':'Exact finite P15 only; no global large-set conclusion or fresh Lean build',
     'pack_sha256':hashlib.sha256((source/'data/eh15_sqs20.json').read_bytes()).hexdigest(),
     'checks':checks,'historical_result_objects_match':True,
     'independent_residual':{'vertices':570,'regular_degree':4,'component_sizes':sizes,'K5_count':4,
                             'K5_witnesses':[[list(holes[v]) for v in c] for c in cliques],
                             'max_retained_systems_in_full_large_set':12,'min_replaced_systems':3}}
print(json.dumps(out,indent=2))
