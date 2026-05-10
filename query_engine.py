import requests
import time

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def search(topic):
    sql = "SELECT * FROM V WHERE name.toLowerCase() LIKE '%" + topic.lower() + "%'"
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def get_related(node_id):
    sql = "SELECT expand(both()) FROM " + node_id
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def bfs_search(topic):
    print('Searching for: ' + topic)
    print('=' * 55)

    total_start = time.time()
    search_start = time.time()
    results = search(topic)
    search_end = time.time()

    if not results:
        print('No results found for: ' + topic)
        return

    visited = []
    queue = list(results)
    nodes_visited = 0
    edges_traversed = 0

    traversal_start = time.time()

    while queue:
        node = queue.pop(0)
        node_id = node.get('@rid', '')

        if node_id in visited:
            continue
        visited.append(node_id)
        nodes_visited += 1

        name       = node.get('name', 'Unknown')
        ntype      = node.get('@class', 'Unknown')
        desc       = node.get('description', '')
        video      = node.get('video', '')
        pdf        = node.get('pdf', '')
        pdf2       = node.get('pdf2', '')
        pdf3       = node.get('pdf3', '')
        severity   = node.get('severity', '')
        difficulty = node.get('difficulty', '')

        print('')
        print('[' + ntype.upper() + '] ' + name)
        if difficulty:
            print('  Difficulty  : ' + difficulty)
        print('  Description : ' + desc)
        if severity and severity not in ['NA', 'N/A']:
            print('  Severity    : ' + severity)
        if video:
            print('  Watch Video : ' + video)
        if pdf:
            print('  Read Paper1 : ' + pdf)
        if pdf2:
            print('  Read Paper2 : ' + pdf2)
        if pdf3:
            print('  Read Paper3 : ' + pdf3)

        related = get_related(node_id)
        if related:
            print('  Related Topics:')
            for r in related:
                rname = r.get('name', '')
                rtype = r.get('@class', '')
                rdiff = r.get('difficulty', '')
                if rname and r.get('@rid', '') not in visited:
                    if rdiff:
                        print('    -> [' + rtype + '] ' + rname + ' (' + rdiff + ')')
                    else:
                        print('    -> [' + rtype + '] ' + rname)
                    queue.append(r)
                    edges_traversed += 1

    traversal_end = time.time()
    total_end = time.time()

    print('')
    print('=' * 55)
    print('  SEARCH COMPLETE!')
    print('=' * 55)
    print('  [PERFORMANCE ANALYSIS]')
    print('  Search time      : ' + str(round(search_end - search_start, 4)) + ' seconds')
    print('  Traversal time   : ' + str(round(traversal_end - traversal_start, 4)) + ' seconds')
    print('  Total time       : ' + str(round(total_end - total_start, 4)) + ' seconds')
    print('  Nodes visited    : ' + str(nodes_visited))
    print('  Edges traversed  : ' + str(edges_traversed))
    print('  Time Complexity  : O(V+E) = O(' + str(nodes_visited) + '+' + str(edges_traversed) + ')')
    print('=' * 55)

if __name__ == '__main__':
    print('')
    print('  AI Security Hypermedia System')
    print('  Knowledge Graph - BFS Search')
    print('=' * 55)
    topic = input('Enter topic to search: ')
    bfs_search(topic)
