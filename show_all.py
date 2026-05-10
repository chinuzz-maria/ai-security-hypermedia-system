import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def query(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

print('')
print('=' * 60)
print('  AISecurityDB - Complete Database Contents')
print('=' * 60)

categories = [
    ('ATTACKS',  'SELECT * FROM Attack'),
    ('DEFENSES', 'SELECT * FROM Defense'),
    ('TOOLS',    'SELECT * FROM Tool'),
    ('DATASETS', 'SELECT * FROM Dataset'),
]

for category, sql in categories:
    results = query(sql)
    print('')
    print('  [' + category + '] - ' + str(len(results)) + ' records')
    print('  ' + '-' * 50)
    for item in results:
        print('')
        print('  Name        : ' + str(item.get('name','')))
        print('  Description : ' + str(item.get('description','')))
        print('  Severity    : ' + str(item.get('severity','')))
        print('  Video       : ' + str(item.get('video','')))
        print('  Paper 1     : ' + str(item.get('pdf','')))
        print('  Paper 2     : ' + str(item.get('pdf2','')))
        print('  Paper 3     : ' + str(item.get('pdf3','')))

print('')
print('=' * 60)
print('  [RELATIONSHIPS/EDGES]')
print('  ' + '-' * 50)
edges = query('SELECT expand(edges()) FROM V')
relationships = query("SELECT out().name as from_node, @class as type, in().name as to_node FROM E")
for rel in relationships:
    from_node = str(rel.get('from_node',''))
    rel_type  = str(rel.get('type',''))
    to_node   = str(rel.get('to_node',''))
    print('  ' + from_node + ' --' + rel_type + '--> ' + to_node)

print('')
print('=' * 60)
total = sum(len(query('SELECT * FROM ' + c)) for c in ['Attack','Defense','Tool','Dataset'])
print('  Total Nodes : ' + str(total))
print('  Total Edges : ' + str(len(relationships)))
print('=' * 60)
