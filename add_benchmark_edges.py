import requests
from requests.auth import HTTPBasicAuth

auth = HTTPBasicAuth('root', 'root')
base = 'http://localhost:2480/command/AISecurityDB/sql'

def run_sql(sql):
    r = requests.post(
        base,
        json={'command': sql},
        auth=auth
    )
    return r.status_code, r.text[:150]

print('='*55)
print('  Step 1: Creating edge class benchmarked_on...')
print('='*55)

# Create the edge class first
status, text = run_sql("CREATE CLASS benchmarked_on EXTENDS E")
if status == 200:
    print('  [OK] Edge class created!')
else:
    print('  [INFO] ' + str(status) + ' — may already exist, continuing...')

print()
print('  Step 2: Adding edges...')
print('='*55)

benchmark_edges = [
    ('Adversarial Training', 'NSL-KDD', 0.88),
    ('Adversarial Training', 'CICIDS2017', 0.85),
    ('Preprocessing Defense', 'CICIDS2017', 0.82),
    ('Preprocessing Defense', 'NSL-KDD', 0.79),
    ('Defensive Distillation', 'NSL-KDD', 0.76),
]

for src, tgt, w in benchmark_edges:
    sql = ("CREATE EDGE benchmarked_on FROM "
           "(SELECT FROM V WHERE name='" + src + "') "
           "TO (SELECT FROM V WHERE name='" + tgt + "') "
           "SET weight=" + str(w))

    status, text = run_sql(sql)

    if status == 200:
        print('  [OK] ' + src + ' --> ' + tgt +
              ' (weight=' + str(w) + ')')
    else:
        print('  [FAIL] ' + src + ' --> ' + tgt +
              ' : ' + str(status))
        print('  Error: ' + text)

print('='*55)
print('  Done!')
print('='*55)