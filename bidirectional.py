import requests
import time

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql',
                      auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def search(topic):
    sql = ("SELECT * FROM V WHERE name.toLowerCase() LIKE '%" +
           topic.lower() + "%'")
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql',
                      auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def get_outgoing(node_id):
    sql = "SELECT expand(out()) FROM " + node_id
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql',
                      auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def get_incoming(node_id):
    sql = "SELECT expand(in()) FROM " + node_id
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql',
                      auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def get_both(node_id):
    sql = "SELECT expand(both()) FROM " + node_id
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql',
                      auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def directed_bfs(topic):
    print('')
    print('=' * 55)
    print('  DIRECTED BFS (Forward only)')
    print('  Topic: ' + topic)
    print('=' * 55)
    results = search(topic)
    if not results:
        print('  Topic not found!')
        return

    visited = []
    queue   = list(results)
    order   = []

    while queue:
        node    = queue.pop(0)
        node_id = node.get('@rid', '')
        if node_id in visited:
            continue
        visited.append(node_id)
        name  = node.get('name', '')
        ntype = node.get('@class', '')
        diff  = node.get('difficulty', '')
        if name:
            order.append('[' + ntype + '] ' + name +
                         ' (' + diff + ')')
        related = get_outgoing(node_id)
        for r in related:
            if r.get('@rid', '') not in visited:
                queue.append(r)

    print('  Traversal Order (Forward):')
    for i, node in enumerate(order):
        print('    ' + str(i+1) + '. ' + node)
    print('  Total nodes visited: ' + str(len(order)))

def bidirectional_bfs(topic):
    print('')
    print('=' * 55)
    print('  BIDIRECTIONAL BFS (Both directions)')
    print('  Topic: ' + topic)
    print('=' * 55)
    results = search(topic)
    if not results:
        print('  Topic not found!')
        return

    visited = []
    queue   = list(results)
    order   = []

    while queue:
        node    = queue.pop(0)
        node_id = node.get('@rid', '')
        if node_id in visited:
            continue
        visited.append(node_id)
        name  = node.get('name', '')
        ntype = node.get('@class', '')
        diff  = node.get('difficulty', '')
        if name:
            order.append('[' + ntype + '] ' + name +
                         ' (' + diff + ')')
        related = get_both(node_id)
        for r in related:
            if r.get('@rid', '') not in visited:
                queue.append(r)

    print('  Traversal Order (Both directions):')
    for i, node in enumerate(order):
        print('    ' + str(i+1) + '. ' + node)
    print('  Total nodes visited: ' + str(len(order)))

def show_neighbors(topic):
    print('')
    print('=' * 55)
    print('  Neighbors of: ' + topic)
    print('=' * 55)
    results = search(topic)
    if not results:
        print('  Topic not found!')
        return

    node_id   = results[0].get('@rid', '')
    node_name = results[0].get('name', '')
    node_type = results[0].get('@class', '')

    print('  Node: [' + node_type + '] ' + node_name)
    print('')

    outgoing = get_outgoing(node_id)
    if outgoing:
        print('  OUTGOING (this topic connects TO):')
        for n in outgoing:
            name  = n.get('name', '')
            ntype = n.get('@class', '')
            diff  = n.get('difficulty', '')
            if name:
                print('    --> [' + ntype + '] ' + name +
                      ' (' + diff + ')')

    incoming = get_incoming(node_id)
    if incoming:
        print('')
        print('  INCOMING (topics that connect TO this):')
        for n in incoming:
            name  = n.get('name', '')
            ntype = n.get('@class', '')
            diff  = n.get('difficulty', '')
            if name:
                print('    <-- [' + ntype + '] ' + name +
                      ' (' + diff + ')')

def compare_directed_vs_bidirectional(topic):
    print('')
    print('=' * 55)
    print('  Directed vs Bidirectional Comparison')
    print('  Topic: ' + topic)
    print('=' * 55)

    results = search(topic)
    if not results:
        print('  Topic not found!')
        return

    # Directed
    start   = time.time()
    visited_d = []
    queue     = list(results)
    count_d   = 0
    while queue:
        node    = queue.pop(0)
        node_id = node.get('@rid', '')
        if node_id in visited_d:
            continue
        visited_d.append(node_id)
        count_d += 1
        related = get_outgoing(node_id)
        for r in related:
            if r.get('@rid', '') not in visited_d:
                queue.append(r)
    time_d = round(time.time() - start, 4)

    # Bidirectional
    start   = time.time()
    visited_b = []
    queue     = list(results)
    count_b   = 0
    while queue:
        node    = queue.pop(0)
        node_id = node.get('@rid', '')
        if node_id in visited_b:
            continue
        visited_b.append(node_id)
        count_b += 1
        related = get_both(node_id)
        for r in related:
            if r.get('@rid', '') not in visited_b:
                queue.append(r)
    time_b = round(time.time() - start, 4)

    print('')
    print('  Mode          Nodes Visited   Time')
    print('  Directed      ' + str(count_d).ljust(16) +
          str(time_d) + 's')
    print('  Bidirectional ' + str(count_b).ljust(16) +
          str(time_b) + 's')
    print('')
    if count_b > count_d:
        print('  [RESULT] Bidirectional visits MORE nodes!')
        print('  [REASON] Traverses both incoming and outgoing edges')
    else:
        print('  [RESULT] Same nodes visited in both modes')
    print('=' * 55)

def run_bidirectional():
    while True:
        print('')
        print('=' * 55)
        print('  Bidirectional Graph Options')
        print('=' * 55)
        print('  1. Directed BFS (forward only)')
        print('  2. Bidirectional BFS (both directions)')
        print('  3. Show all neighbors (in + out)')
        print('  4. Compare Directed vs Bidirectional')
        print('  5. Back to main menu')
        print('=' * 55)
        choice = input('  Enter choice (1-5): ')

        if choice == '1':
            topic = input('  Enter topic: ')
            directed_bfs(topic)
        elif choice == '2':
            topic = input('  Enter topic: ')
            bidirectional_bfs(topic)
        elif choice == '3':
            topic = input('  Enter topic: ')
            show_neighbors(topic)
        elif choice == '4':
            topic = input('  Enter topic: ')
            compare_directed_vs_bidirectional(topic)
        elif choice == '5':
            break
        else:
            print('  Invalid choice!')

if __name__ == '__main__':
    run_bidirectional()
