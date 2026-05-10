import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

# Check if datasets exist
existing = run("SELECT name FROM Dataset")
existing_names = [d.get('name','') for d in existing]
print('Existing datasets: ' + str(existing_names))

# Add only if missing
if 'NSL-KDD' not in existing_names:
    run("CREATE VERTEX Dataset SET name='NSL-KDD', description='Network-based dataset for IDS testing with labeled attack and normal traffic', video='https://www.youtube.com/watch?v=dfVAi87BSEs', pdf='https://www.mdpi.com/1999-5903/15/2/62/pdf', pdf2='https://doi.org/10.1080/10494820.2019.1674881', pdf3='http://www.warse.org/IJETER/static/pdf/file/ijeter04852020.pdf', severity='NA'")
    print('  [ADDED] NSL-KDD')
else:
    print('  [EXISTS] NSL-KDD')

if 'CICIDS2017' not in existing_names:
    run("CREATE VERTEX Dataset SET name='CICIDS2017', description='Canadian Institute Cybersecurity dataset with realistic 2017 network traffic and attack types', video='https://www.youtube.com/watch?v=dfVAi87BSEs', pdf='https://www.mdpi.com/1999-5903/15/2/62/pdf', pdf2='https://doi.org/10.1080/10494820.2019.1674881', pdf3='http://www.warse.org/IJETER/static/pdf/file/ijeter04852020.pdf', severity='NA'")
    print('  [ADDED] CICIDS2017')
else:
    print('  [EXISTS] CICIDS2017')

# Final count
nodes = run('SELECT count(*) as total FROM V')
edges = run('SELECT count(*) as total FROM E')
print('')
print('=' * 40)
print('  Total Nodes : ' + str(nodes[0].get('total',0)))
print('  Total Edges : ' + str(edges[0].get('total',0)))
print('  Expected    : 14 nodes, 8 edges')
print('=' * 40)
