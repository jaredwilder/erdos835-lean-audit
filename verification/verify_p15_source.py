"""Check the exact recovered P15 package against its source manifest."""
import hashlib,json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
m=json.loads((root/'sqs20/P15-SOURCE-MANIFEST.json').read_text())
for f in m['files']:
    data=(root/f['destination']).read_bytes()
    assert len(data)==f['bytes'] and hashlib.sha256(data).hexdigest()==f['sha256'],f['destination']
    assert hashlib.sha1(f'blob {len(data)}\0'.encode()+data).hexdigest()==f['git_blob'],f['destination']
print(json.dumps({'result':'PASS','exact_archive_files':len(m['files']),'source_archive_sha256':m['source_archive_sha256']}))
