import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

# Fix 1 - Re-add missing datasets
print('Re-adding datasets...')
datasets = [
    "CREATE VERTEX Dataset SET name='NSL-KDD', description='Network-based dataset for IDS testing with labeled attack and normal traffic', video='https://www.youtube.com/watch?v=dfVAi87BSEs', pdf='https://www.mdpi.com/1999-5903/15/2/62/pdf', pdf2='https://doi.org/10.1080/10494820.2019.1674881', pdf3='http://www.warse.org/IJETER/static/pdf/file/ijeter04852020.pdf', severity='NA'",
    "CREATE VERTEX Dataset SET name='CICIDS2017', description='Canadian Institute Cybersecurity dataset with realistic 2017 network traffic and attack types', video='https://www.youtube.com/watch?v=dfVAi87BSEs', pdf='https://www.mdpi.com/1999-5903/15/2/62/pdf', pdf2='https://doi.org/10.1080/10494820.2019.1674881', pdf3='http://www.warse.org/IJETER/static/pdf/file/ijeter04852020.pdf', severity='NA'",
]
for sql in datasets:
    r = run(sql)
    name = sql.split("name='")[1].split("'")[0]
    print('  [ADDED] Dataset: ' + name)

# Fix 2 - Show relationships properly
print('')
print('Checking relationships...')
edges = run('SELECT out().name as from_node, @class as edge_type, in().name as to_node FROM E')
for e in edges:
    fn = str(e.get('from_node','?'))
    et = str(e.get('edge_type','?'))
    tn = str(e.get('to_node','?'))
    print('  ' + fn + ' --' + et + '--> ' + tn)

print('')
print('Done!')
