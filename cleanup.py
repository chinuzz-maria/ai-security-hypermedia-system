import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

# Delete old test nodes that have no video link
sql = "DELETE VERTEX Attack WHERE video IS NULL"
r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
print('Cleaned old test nodes: ' + str(r.status_code))

# Check what remains
r2 = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': 'SELECT name, video FROM Attack'})
data = r2.json().get('result', [])
print('Remaining Attack nodes:')
for item in data:
    print('  ' + item.get('name') + ' | video: ' + str(item.get('video', 'none')))
