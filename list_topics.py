import requests

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def list_all_topics():
    print('')
    print('=' * 60)
    print('  All Available AI Security Topics')
    print('=' * 60)
    print('  Difficulty: [B]=Beginner [I]=Intermediate [A]=Advanced')
    print('=' * 60)

    categories = [
        ('ATTACKS',  'SELECT name, severity, difficulty FROM Attack'),
        ('DEFENSES', 'SELECT name, difficulty FROM Defense'),
        ('TOOLS',    'SELECT name, difficulty FROM Tool'),
        ('DATASETS', 'SELECT name, difficulty FROM Dataset'),
    ]

    for category, sql in categories:
        results = run(sql)
        print('')
        print('  [' + category + ']')
        for item in results:
            name = item.get('name', '')
            severity = item.get('severity', '')
            difficulty = item.get('difficulty', '')

            if difficulty == 'Beginner':
                dlabel = '[B]'
            elif difficulty == 'Intermediate':
                dlabel = '[I]'
            elif difficulty == 'Advanced':
                dlabel = '[A]'
            else:
                dlabel = '   '

            if severity and severity != 'NA':
                print('    ' + dlabel + ' ' + name + ' (Severity: ' + severity + ')')
            else:
                print('    ' + dlabel + ' ' + name)

    print('')
    print('=' * 60)
    print('  Tip: Start with [B] Beginner topics first!')
    print('  Then [I] Intermediate -> [A] Advanced')
    print('  Search any topic using option 5!')
    print('=' * 60)

if __name__ == '__main__':
    list_all_topics()
