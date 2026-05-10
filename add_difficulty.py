import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

print('Adding difficulty levels...')

updates = [
    # TOOLS - Beginner
    "UPDATE Tool SET difficulty='Beginner' WHERE name='SVM'",
    "UPDATE Tool SET difficulty='Beginner' WHERE name='MLP'",
    "UPDATE Tool SET difficulty='Beginner' WHERE name='DNN'",

    # DATASETS - Beginner
    "UPDATE Dataset SET difficulty='Beginner' WHERE name='NSL-KDD'",
    "UPDATE Dataset SET difficulty='Beginner' WHERE name='CICIDS2017'",

    # TOOLS - Intermediate
    "UPDATE Tool SET difficulty='Intermediate' WHERE name='GAN'",

    # DEFENSES - Intermediate
    "UPDATE Defense SET difficulty='Intermediate' WHERE name='Preprocessing Defense'",
    "UPDATE Defense SET difficulty='Intermediate' WHERE name='Adversarial Training'",
    "UPDATE Defense SET difficulty='Intermediate' WHERE name='Defensive Distillation'",

    # ATTACKS - Advanced
    "UPDATE Attack SET difficulty='Advanced' WHERE name='FGSM Attack'",
    "UPDATE Attack SET difficulty='Advanced' WHERE name='PGD Attack'",
    "UPDATE Attack SET difficulty='Advanced' WHERE name='Black-Box Attack'",
    "UPDATE Attack SET difficulty='Advanced' WHERE name='IDSGAN'",
    "UPDATE Attack SET difficulty='Advanced' WHERE name='DDoS Attack'",
]

for sql in updates:
    r = run(sql)
    topic = sql.split("name='")[1].split("'")[0]
    level = sql.split("difficulty='")[1].split("'")[0]
    print('  [UPDATED] ' + topic + ' -> ' + level)

print('')
print('All difficulty levels added!')
