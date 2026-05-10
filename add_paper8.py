import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

P8 = 'https://doi.org/10.1109/ACCESS.2025.3583759'

updates = [
    "UPDATE Attack SET pdf2='" + P8 + "' WHERE name='Black-Box Attack'",
    "UPDATE Tool SET pdf3='" + P8 + "' WHERE name='DNN'",
    "UPDATE Tool SET pdf3='" + P8 + "' WHERE name='GAN'",
]

for sql in updates:
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    print('Updated: ' + str(r.status_code))

print('Paper 8 added successfully!')
