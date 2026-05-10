import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

print('Fixing duplicate edges...')

# Delete ALL edges first
run('DELETE EDGE mitigated_by')
run('DELETE EDGE uses')
print('  [DELETED] All old edges')

# Recreate edges cleanly - one by one
edges = [
    ('FGSM Attack',    'Adversarial Training',   'mitigated_by'),
    ('PGD Attack',     'Adversarial Training',   'mitigated_by'),
    ('Black-Box Attack','Preprocessing Defense', 'mitigated_by'),
    ('IDSGAN',         'Adversarial Training',   'mitigated_by'),
    ('DDoS Attack',    'Preprocessing Defense',  'mitigated_by'),
    ('FGSM Attack',    'DNN',                    'uses'),
    ('IDSGAN',         'GAN',                    'uses'),
    ('Black-Box Attack','GAN',                   'uses'),
]

print('Recreating edges cleanly...')
for from_node, to_node, edge_type in edges:
    sql = "CREATE EDGE " + edge_type + " FROM (SELECT FROM V WHERE name='" + from_node + "') TO (SELECT FROM V WHERE name='" + to_node + "')"
    run(sql)
    print('  [EDGE] ' + from_node + ' --' + edge_type + '--> ' + to_node)

# Check final count
total_edges = run('SELECT count(*) as total FROM E')
total_nodes = run('SELECT count(*) as total FROM V')
print('')
print('=' * 55)
print('  Total Nodes : ' + str(total_nodes[0].get('total',0)))
print('  Total Edges : ' + str(total_edges[0].get('total',0)))
print('  Expected    : 14 nodes, 8 edges')
print('=' * 55)
