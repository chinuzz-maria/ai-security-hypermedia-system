import requests
import time

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def search(topic):
    sql = "SELECT * FROM V WHERE name.toLowerCase() LIKE '%" + topic.lower() + "%'"
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def get_related(node_id):
    sql = "SELECT expand(both()) FROM " + node_id
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def bfs(topic):
    results = search(topic)
    if not results:
        return [], 0

    visited = []
    queue = list(results)
    order = []

    while queue:
        node = queue.pop(0)
        node_id = node.get('@rid', '')
        if node_id in visited:
            continue
        visited.append(node_id)
        name = node.get('name', '')
        ntype = node.get('@class', '')
        if name:
            order.append('[' + ntype + '] ' + name)
        related = get_related(node_id)
        for r in related:
            if r.get('@rid', '') not in visited:
                queue.append(r)

    return order, len(visited)

def dfs(topic):
    results = search(topic)
    if not results:
        return [], 0

    visited = []
    stack = list(results)
    order = []

    while stack:
        node = stack.pop()
        node_id = node.get('@rid', '')
        if node_id in visited:
            continue
        visited.append(node_id)
        name = node.get('name', '')
        ntype = node.get('@class', '')
        if name:
            order.append('[' + ntype + '] ' + name)
        related = get_related(node_id)
        for r in related:
            if r.get('@rid', '') not in visited:
                stack.append(r)

    return order, len(visited)

def shortest_path(from_topic, to_topic):
    from_results = search(from_topic)
    to_results = search(to_topic)

    if not from_results or not to_results:
        print('  Topic not found!')
        return

    from_id = from_results[0].get('@rid', '')
    to_id = to_results[0].get('@rid', '')
    from_name = from_results[0].get('name', '')
    to_name = to_results[0].get('name', '')

    # BFS to find shortest path
    queue = [[from_id]]
    visited = []

    while queue:
        path = queue.pop(0)
        node_id = path[-1]

        if node_id in visited:
            continue
        visited.append(node_id)

        if node_id == to_id:
            print('  Shortest path found!')
            print('  Path length : ' + str(len(path)-1) + ' hops')
            for i, pid in enumerate(path):
                node = run('SELECT name, @class FROM ' + pid)
                if node:
                    nname = node[0].get('name', '')
                    ntype = node[0].get('@class', '')
                    if i == 0:
                        print('  START : [' + ntype + '] ' + nname)
                    elif i == len(path)-1:
                        print('  END   : [' + ntype + '] ' + nname)
                    else:
                        print('    ->    [' + ntype + '] ' + nname)
            return

        related = get_related(node_id)
        for r in related:
            rid = r.get('@rid', '')
            if rid not in visited:
                queue.append(path + [rid])

    print('  No path found between ' + from_name + ' and ' + to_name)

def compare_bfs_dfs(topic):
    print('')
    print('=' * 55)
    print('  BFS vs DFS Comparison for: ' + topic)
    print('=' * 55)

    # Run BFS
    print('')
    print('  Running BFS...')
    bfs_start = time.time()
    bfs_order, bfs_nodes = bfs(topic)
    bfs_time = round(time.time() - bfs_start, 4)

    print('  BFS Traversal Order:')
    for i, node in enumerate(bfs_order):
        print('    ' + str(i+1) + '. ' + node)
    print('  BFS Time   : ' + str(bfs_time) + ' seconds')
    print('  BFS Nodes  : ' + str(bfs_nodes))

    # Run DFS
    print('')
    print('  Running DFS...')
    dfs_start = time.time()
    dfs_order, dfs_nodes = dfs(topic)
    dfs_time = round(time.time() - dfs_start, 4)

    print('  DFS Traversal Order:')
    for i, node in enumerate(dfs_order):
        print('    ' + str(i+1) + '. ' + node)
    print('  DFS Time   : ' + str(dfs_time) + ' seconds')
    print('  DFS Nodes  : ' + str(dfs_nodes))

    # Comparison
    print('')
    print('=' * 55)
    print('  COMPARISON RESULTS')
    print('=' * 55)
    print('  Algorithm   BFS          DFS')
    print('  Time      : ' + str(bfs_time) + 's       ' + str(dfs_time) + 's')
    print('  Nodes     : ' + str(bfs_nodes) + '            ' + str(dfs_nodes))
    print('  Strategy  : Queue        Stack')
    print('  Order     : Level-wise   Depth-wise')
    print('')
    if bfs_time < dfs_time:
        print('  [RESULT] BFS is faster for this search!')
        print('  [REASON] BFS finds nearby nodes first')
    else:
        print('  [RESULT] DFS is faster for this search!')
        print('  [REASON] DFS goes deep before backtracking')
    print('=' * 55)

def run_traversal():
    while True:
        print('')
        print('=' * 55)
        print('  Graph Traversal Options')
        print('=' * 55)
        print('  1. BFS Search')
        print('  2. DFS Search')
        print('  3. Compare BFS vs DFS')
        print('  4. Find Shortest Path')
        print('  5. Back to main menu')
        print('=' * 55)
        choice = input('  Enter choice (1-5): ')

        if choice == '1':
            topic = input('  Enter topic for BFS: ')
            start = time.time()
            order, nodes = bfs(topic)
            elapsed = round(time.time() - start, 4)
            print('')
            print('  BFS Traversal Order:')
            for i, node in enumerate(order):
                print('    ' + str(i+1) + '. ' + node)
            print('  Time taken : ' + str(elapsed) + ' seconds')
            print('  Nodes found: ' + str(nodes))

        elif choice == '2':
            topic = input('  Enter topic for DFS: ')
            start = time.time()
            order, nodes = dfs(topic)
            elapsed = round(time.time() - start, 4)
            print('')
            print('  DFS Traversal Order:')
            for i, node in enumerate(order):
                print('    ' + str(i+1) + '. ' + node)
            print('  Time taken : ' + str(elapsed) + ' seconds')
            print('  Nodes found: ' + str(nodes))

        elif choice == '3':
            topic = input('  Enter topic to compare BFS vs DFS: ')
            compare_bfs_dfs(topic)

        elif choice == '4':
            print('')
            from_topic = input('  Enter FROM topic: ')
            to_topic = input('  Enter TO topic: ')
            print('')
            print('  Finding shortest path...')
            shortest_path(from_topic, to_topic)

        elif choice == '5':
            break
        else:
            print('  Invalid choice!')

if __name__ == '__main__':
    run_traversal()
