import requests
import time

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql', auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def analyze_graph():
    print('')
    print('=' * 55)
    print('  AI Security Knowledge Graph - Analysis Report')
    print('=' * 55)

    # Count nodes by type
    attacks  = run('SELECT count(*) as total FROM Attack')
    defenses = run('SELECT count(*) as total FROM Defense')
    tools    = run('SELECT count(*) as total FROM Tool')
    datasets = run('SELECT count(*) as total FROM Dataset')
    total_v  = run('SELECT count(*) as total FROM V')
    total_e  = run('SELECT count(*) as total FROM E')

    V = total_v[0].get('total', 0)
    E = total_e[0].get('total', 0)

    print('')
    print('  [GRAPH STRUCTURE]')
    print('  Total Nodes (V)  : ' + str(V))
    print('  Total Edges (E)  : ' + str(E))
    print('  Attacks          : ' + str(attacks[0].get('total', 0)))
    print('  Defenses         : ' + str(defenses[0].get('total', 0)))
    print('  Tools            : ' + str(tools[0].get('total', 0)))
    print('  Datasets         : ' + str(datasets[0].get('total', 0)))

    # Graph density
    if V > 1:
        max_edges = V * (V - 1)
        density = round(E / max_edges, 4)
    else:
        density = 0

    print('')
    print('  [GRAPH PROPERTIES]')
    print('  Graph Type       : Directed Graph')
    print('  Graph Density    : ' + str(density))
    print('  Max Possible E   : ' + str(V * (V-1)))
    print('  Actual Edges     : ' + str(E))
    if density < 0.3:
        print('  Graph Category   : Sparse Graph')
    else:
        print('  Graph Category   : Dense Graph')

    # Edge types
    mit_edges = run('SELECT count(*) as total FROM mitigated_by')
    uses_edges = run('SELECT count(*) as total FROM uses')
    print('')
    print('  [EDGE ANALYSIS]')
    print('  mitigated_by     : ' + str(mit_edges[0].get('total', 0)) + ' edges')
    print('  uses             : ' + str(uses_edges[0].get('total', 0)) + ' edges')

    # Complexity analysis
    print('')
    print('  [COMPLEXITY ANALYSIS]')
    print('  BFS Time  Complexity : O(V+E) = O(' + str(V) + '+' + str(E) + ') = O(' + str(V+E) + ')')
    print('  BFS Space Complexity : O(V)   = O(' + str(V) + ')')
    print('  Storage Complexity   : O(V+E) = O(' + str(V+E) + ')')

    # Benchmark - run multiple searches
    print('')
    print('  [BENCHMARK - EXECUTION TIMES]')
    print('  Running 5 searches...')
    print('')

    topics = ['FGSM Attack', 'GAN', 'defense', 'DNN', 'DDoS']
    times = []

    for topic in topics:
        start = time.time()
        sql = "SELECT * FROM V WHERE name.toLowerCase() LIKE '%" + topic.lower() + "%'"
        results = run(sql)
        if results:
            for node in results:
                rid = node.get('@rid', '')
                run('SELECT expand(both()) FROM ' + rid)
        end = time.time()
        elapsed = round(end - start, 4)
        times.append(elapsed)
        print('  Search: ' + topic.ljust(20) + ' -> ' + str(elapsed) + ' seconds')

    avg_time = round(sum(times) / len(times), 4)
    min_time = round(min(times), 4)
    max_time = round(max(times), 4)

    print('')
    print('  [BENCHMARK SUMMARY]')
    print('  Average time : ' + str(avg_time) + ' seconds')
    print('  Minimum time : ' + str(min_time) + ' seconds')
    print('  Maximum time : ' + str(max_time) + ' seconds')
    print('')
    print('=' * 55)
    print('  Graph Analysis Complete!')
    print('=' * 55)

if __name__ == '__main__':
    analyze_graph()
