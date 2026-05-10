import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.status_code

P1 = 'http://www.warse.org/IJETER/static/pdf/file/ijeter04852020.pdf'
P2 = 'https://www.mdpi.com/1999-5903/15/2/62/pdf'
P3 = 'https://www.mdpi.com/1999-5903/13/3/73/pdf'
P4 = 'https://doi.org/10.1016/j.neucom.2020.07.133'
P5 = 'https://doi.org/10.1016/j.array.2025.100546'
P6 = 'https://doi.org/10.1145/3769694.3771166'
P7 = 'https://doi.org/10.1080/10494820.2019.1674881'

updates = [
    # ATTACKS
    ("UPDATE Attack SET pdf='" + P2 + "', pdf2='" + P5 + "', pdf3='" + P1 + "' WHERE name='FGSM Attack'"),
    ("UPDATE Attack SET pdf='" + P2 + "', pdf2='" + P5 + "', pdf3='" + P1 + "' WHERE name='PGD Attack'"),
    ("UPDATE Attack SET pdf='" + P2 + "', pdf2='" + P6 + "', pdf3='" + P1 + "' WHERE name='Black-Box Attack'"),
    ("UPDATE Attack SET pdf='" + P2 + "', pdf2='" + P6 + "', pdf3='" + P1 + "' WHERE name='IDSGAN'"),
    ("UPDATE Attack SET pdf='" + P2 + "', pdf2='" + P6 + "', pdf3='" + P1 + "' WHERE name='DDoS Attack'"),
    # DEFENSES
    ("UPDATE Defense SET pdf='" + P5 + "', pdf2='" + P2 + "', pdf3='" + P1 + "' WHERE name='Adversarial Training'"),
    ("UPDATE Defense SET pdf='" + P5 + "', pdf2='" + P2 + "', pdf3='" + P1 + "' WHERE name='Preprocessing Defense'"),
    ("UPDATE Defense SET pdf='" + P4 + "', pdf2='" + P3 + "', pdf3='" + P1 + "' WHERE name='Defensive Distillation'"),
    # TOOLS
    ("UPDATE Tool SET pdf='" + P3 + "', pdf2='" + P6 + "', pdf3='" + P1 + "' WHERE name='GAN'"),
    ("UPDATE Tool SET pdf='" + P3 + "', pdf2='" + P4 + "', pdf3='" + P1 + "' WHERE name='DNN'"),
    ("UPDATE Tool SET pdf='" + P2 + "', pdf2='" + P6 + "', pdf3='" + P1 + "' WHERE name='SVM'"),
    ("UPDATE Tool SET pdf='" + P2 + "', pdf2='" + P6 + "', pdf3='" + P1 + "' WHERE name='MLP'"),
    # DATASETS
    ("UPDATE Dataset SET pdf='" + P2 + "', pdf2='" + P7 + "', pdf3='" + P1 + "' WHERE name='NSL-KDD'"),
    ("UPDATE Dataset SET pdf='" + P2 + "', pdf2='" + P7 + "', pdf3='" + P1 + "' WHERE name='CICIDS2017'"),
]

print('Updating all PDF links in OrientDB...')
print('')
for sql in updates:
    status = run(sql)
    topic = sql.split("name='")[1].split("'")[0]
    print('  [UPDATED] ' + topic + ' -> ' + str(status))

print('')
print('All 7 paper links updated successfully!')
print('Note: Paper 8 pending - add later')
