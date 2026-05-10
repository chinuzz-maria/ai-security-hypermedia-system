import requests
import json
import os

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql',
                      auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def node_exists(name):
    result = run("SELECT FROM V WHERE name='" + name + "'")
    return len(result) > 0

def store_all():
    print('Loading classified data...')
    with open('data/processed/classified_data.json', 'r') as f:
        data = json.load(f)

    print('Storing nodes in OrientDB...')
    for item in data:
        name  = item['name']
        itype = item['type']
        desc  = item.get('description', '')
        sev   = item.get('severity', 'NA')
        vid   = item.get('video', '')
        pdf   = item.get('pdf', '')
        diff  = item.get('difficulty', '')
        desc  = desc.replace("'", "")

        if node_exists(name):
            print('  [EXISTS] ' + itype + ': ' + name)
            continue

        sql = ("CREATE VERTEX " + itype +
               " SET name='" + name +
               "', description='" + desc +
               "', severity='" + sev +
               "', video='" + vid +
               "', pdf='" + pdf +
               "', difficulty='" + diff + "'")
        run(sql)
        print('  [STORED] ' + itype + ': ' + name)

    print('Fixing edges - deleting old ones first...')
    run('DELETE EDGE mitigated_by')
    run('DELETE EDGE uses')

    print('Creating relationships (edges) with weights...')
    edges = [
        ('FGSM Attack',     'Adversarial Training',  'mitigated_by', 0.95),
        ('PGD Attack',      'Adversarial Training',  'mitigated_by', 0.90),
        ('Black-Box Attack','Preprocessing Defense', 'mitigated_by', 0.75),
        ('IDSGAN',          'Adversarial Training',  'mitigated_by', 0.85),
        ('DDoS Attack',     'Preprocessing Defense', 'mitigated_by', 0.80),
        ('FGSM Attack',     'DNN',                   'uses',         0.88),
        ('IDSGAN',          'GAN',                   'uses',         0.92),
        ('Black-Box Attack','GAN',                   'uses',         0.78),
    ]

    for from_node, to_node, edge_type, weight in edges:
        sql = ("CREATE EDGE " + edge_type +
               " FROM (SELECT FROM V WHERE name='" + from_node +
               "') TO (SELECT FROM V WHERE name='" + to_node +
               "') SET weight=" + str(weight))
        run(sql)
        print('  [EDGE] ' + from_node + ' --' + edge_type +
              '--> ' + to_node + ' [weight=' + str(weight) + ']')

    total_v = run('SELECT count(*) as total FROM V')
    total_e = run('SELECT count(*) as total FROM E')
    print('')
    print('All data stored in OrientDB!')
    print('Total Nodes : ' + str(total_v[0].get('total', 0)))
    print('Total Edges : ' + str(total_e[0].get('total', 0)))

if __name__ == '__main__':
    store_all()
