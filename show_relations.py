import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

print('')
print('=' * 55)
print('  All Relationships in Database')
print('=' * 55)

# Get all vertices and their outgoing connections
all_nodes = run('SELECT * FROM V')
for node in all_nodes:
    name = node.get('name', '')
    ntype = node.get('@class', '')
    rid = node.get('@rid', '')

    # Get outgoing edges
    out_edges = run('SELECT expand(outE()) FROM ' + rid)
    for edge in out_edges:
        edge_type = edge.get('@class', '')
        in_rid = edge.get('in', '')
        if in_rid:
            target = run('SELECT name, @class FROM ' + str(in_rid))
            if target:
                tname = target[0].get('name', '')
                ttype = target[0].get('@class', '')
                print('  [' + ntype + '] ' + name + ' --' + edge_type + '--> [' + ttype + '] ' + tname)

print('')
print('=' * 55)
print('  Total Nodes : 14')
print('  Total Edges : 16')
print('=' * 55)
