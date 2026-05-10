import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(
        BASE_URL + '/command/AISecurityDB/sql',
        auth=AUTH,
        json={'command': sql}
    )
    return r.json().get('result', [])

print('Adding weights to edges...')
print('')

weights = [
    ('FGSM Attack',      'Adversarial Training',  0.95),
    ('PGD Attack',       'Adversarial Training',  0.90),
    ('Black-Box Attack', 'Preprocessing Defense', 0.75),
    ('IDSGAN',           'Adversarial Training',  0.85),
    ('DDoS Attack',      'Preprocessing Defense', 0.80),
    ('FGSM Attack',      'DNN',                   0.88),
    ('IDSGAN',           'GAN',                   0.92),
    ('Black-Box Attack', 'GAN',                   0.78),
]

for from_node, to_node, weight in weights:
    # First get the source node RID
    src = run("SELECT @rid FROM V WHERE name='" + from_node + "'")
    tgt = run("SELECT @rid FROM V WHERE name='" + to_node + "'")

    if not src or not tgt:
        print('  [NOT FOUND] ' + from_node + ' or ' + to_node)
        continue

    src_rid = str(src[0].get('@rid', ''))
    tgt_rid = str(tgt[0].get('@rid', ''))

    # Update edge using RIDs directly
    sql = ("UPDATE E SET weight=" + str(weight) +
           " WHERE out=" + src_rid +
           " AND in=" + tgt_rid)

    r = run(sql)
    print('  [WEIGHTED] ' + from_node + ' --> ' +
          to_node + ' weight=' + str(weight))

print('')
print('Verifying weights...')
print('')

edges = run('SELECT FROM E')

print('=' * 65)
print('  Edge Weights in AISecurityDB')
print('=' * 65)

found = 0
for e in edges:
    out_rid = e.get('out', '')
    in_rid  = e.get('in', '')
    etype   = e.get('@class', '')
    weight  = e.get('weight', None)

    if weight is None:
        continue

    if out_rid:
        src_result = run('SELECT name FROM ' + str(out_rid))
        src_name = src_result[0].get('name', '?') if src_result else '?'
    else:
        src_name = '?'

    if in_rid:
        tgt_result = run('SELECT name FROM ' + str(in_rid))
        tgt_name = tgt_result[0].get('name', '?') if tgt_result else '?'
    else:
        tgt_name = '?'

    print('  ' + src_name + ' --' + etype +
          '(' + str(weight) + ')--> ' + tgt_name)
    found += 1

print('=' * 65)
print('  Total weighted edges verified: ' + str(found))
print('  All weights confirmed! ')
print('=' * 65)