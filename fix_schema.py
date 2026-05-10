import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

run('CREATE CLASS Dataset EXTENDS V')
print('Dataset class created!')

run("CREATE VERTEX Dataset SET name='NSL-KDD', description='Network-based dataset for IDS testing', video='https://www.youtube.com/watch?v=dfVAi87BSEs', pdf='https://www.mdpi.com/1999-5903/15/2/62/pdf', pdf2='https://doi.org/10.1080/10494820.2019.1674881', pdf3='http://www.warse.org/IJETER/static/pdf/file/ijeter04852020.pdf', severity='NA'")
print('[ADDED] NSL-KDD')

run("CREATE VERTEX Dataset SET name='CICIDS2017', description='Canadian Institute Cybersecurity 2017 network traffic dataset', video='https://www.youtube.com/watch?v=dfVAi87BSEs', pdf='https://www.mdpi.com/1999-5903/15/2/62/pdf', pdf2='https://doi.org/10.1080/10494820.2019.1674881', pdf3='http://www.warse.org/IJETER/static/pdf/file/ijeter04852020.pdf', severity='NA'")
print('[ADDED] CICIDS2017')

nodes = run('SELECT count(*) as total FROM V')
edges = run('SELECT count(*) as total FROM E')
print('Total Nodes : ' + str(nodes[0].get('total',0)))
print('Total Edges : ' + str(edges[0].get('total',0)))
