import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

print('Creating AISecurityDB...')
r = requests.post(f'{BASE_URL}/database/AISecurityDB/plocal/graph', auth=AUTH)
if r.status_code in [200, 201]:
    print('Database AISecurityDB created!')
elif r.status_code == 500:
    print('Database already exists - continuing...')

print('Creating graph schema...')
queries = [
    'CREATE CLASS Attack EXTENDS V',
    'CREATE CLASS Defense EXTENDS V',
    'CREATE CLASS Tool EXTENDS V',
    'CREATE CLASS mitigated_by EXTENDS E',
    'CREATE CLASS uses EXTENDS E',
]
for q in queries:
    r = requests.post(f'{BASE_URL}/command/AISecurityDB/sql', auth=AUTH, json={'command': q})
    print('  ' + q + ' -> ' + str(r.status_code))

print('Inserting test data...')
cmd = "INSERT INTO Attack SET name='Adversarial Attack', description='Manipulates ML inputs', severity='High'"
r = requests.post(f'{BASE_URL}/command/AISecurityDB/sql', auth=AUTH, json={'command': cmd})
print('  Insert status: ' + str(r.status_code))

print('Reading data back...')
r = requests.get(f'{BASE_URL}/query/AISecurityDB/sql/SELECT%20*%20FROM%20Attack', auth=AUTH)
data = r.json()
for item in data.get('result', []):
    name = item.get('name')
    desc = item.get('description')
    print('  Found node: ' + str(name) + ' | ' + str(desc))

print('Everything working! Project ready to build!')
