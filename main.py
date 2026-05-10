import os
import sys
import webbrowser

def run_collector():
    print('Running content collector...')
    os.system('python collector.py')

def run_preprocessor():
    print('Running preprocessor...')
    os.system('python preprocessor.py')

def run_graph_manager():
    print('Storing data in OrientDB...')
    os.system('python graph_manager.py')

def list_topics():
    os.system('python list_topics.py')

def run_query():
    os.system('python query_engine.py')

def run_traversal():
    os.system('python traversal.py')

def run_bidirectional():
    os.system('python bidirectional.py')

def run_quiz():
    os.system('python quiz.py')

def run_auto_quiz():
    os.system('python auto_quiz.py')

def run_analysis():
    os.system('python graph_analysis.py')

def show_papers():
    print('')
    print('=' * 55)
    print('   All Research Papers')
    print('=' * 55)
    papers = [
        ('P1', 'CleverUniversity - Adaptive Hypermedia System',
         'http://www.warse.org/IJETER/static/pdf/file/ijeter04852020.pdf'),
        ('P2', 'Adversarial ML Attacks against IDS',
         'https://www.mdpi.com/1999-5903/15/2/62/pdf'),
        ('P3', 'Deep Model Poisoning - Federated Learning',
         'https://www.mdpi.com/1999-5903/13/3/73/pdf'),
        ('P4', 'Defense against Neural Trojan Attacks',
         'https://doi.org/10.1016/j.neucom.2020.07.133'),
        ('P5', 'Adversarial Training and Real-time Detection',
         'https://doi.org/10.1016/j.array.2025.100546'),
        ('P6', 'AI Security Paper - ACM',
         'https://doi.org/10.1145/3769694.3771166'),
        ('P7', 'Hypermedia Learning Paper',
         'https://doi.org/10.1080/10494820.2019.1674881'),
        ('P8', 'Meticulous Thought Defender - Prompt Injection',
         'https://doi.org/10.1109/ACCESS.2025.3583759'),
    ]
    for pid, title, link in papers:
        print('')
        print('  [' + pid + '] ' + title)
        print('       ' + link)
    print('')
    print('=' * 55)
    print('  Total: 8 Research Papers')

def show_status():
    platform = 'Windows' if sys.platform == 'win32' else 'Linux/Ubuntu'
    print('')
    print('  System Status:')
    print('  Platform    : ' + platform)
    print('  OrientDB    : Running at http://localhost:2480')
    print('  Database    : AISecurityDB')
    print('  Topics      : 14 AI Security topics loaded')
    print('  Attacks     : FGSM, PGD, Black-Box, IDSGAN, DDoS')
    print('  Defenses    : Adversarial Training, Preprocessing, Distillation')
    print('  Tools       : GAN, DNN, SVM, MLP')
    print('  Datasets    : NSL-KDD, CICIDS2017')
    print('  Media       : YouTube links + 8 Research Papers')
    print('  Quiz        : Manual (42 Q) + Auto-Generated')
    print('  Traversal   : BFS + DFS + Shortest Path + Bidirectional')
    print('  Edges       : 13 Weighted edges (0.75 to 0.95)')
    print('  Edge Types  : mitigated_by + uses + benchmarked_on')
    print('')

def visualize_graph():
    print('')
    print('=' * 55)
    print('  Graph Visualization')
    print('=' * 55)
    print('  Opening OrientDB Studio in browser...')
    print('')
    print('  Instructions:')
    print('  1. Browser will open automatically')
    print('  2. Login: username=root password=root')
    print('  3. Click GRAPH tab at the top')
    print('  4. Type: SELECT * FROM V')
    print('  5. Click the Play button to run')
    print('  6. You will see all 14 nodes with')
    print('     colored circles and 13 edges!')
    print('')
    print('  Legend:')
    print('  Orange (dark) = Attacks')
    print('  Green         = Defenses')
    print('  Orange (light)= Tools + Datasets')
    print('  Grey arrows   = mitigated_by')
    print('  Red arrows    = uses')
    print('  Dark red      = benchmarked_on')
    print('=' * 55)

    # Open OrientDB Studio directly to graph page
    url = 'http://localhost:2480/studio/index.html#/database/AISecurityDB/graph'
    try:
        webbrowser.open(url)
        print('')
        print('  Browser opened successfully!')
        print('  Run this query in the Graph Editor:')
        print('  SELECT * FROM V')
        print('')
    except Exception as e:
        print('  Could not open browser automatically.')
        print('  Please open manually: http://localhost:2480')
        print('  Error: ' + str(e))
    print('=' * 55)

def main():
    while True:
        print('')
        print('=' * 55)
        print('   AI Security Hypermedia System')
        print('   Powered by OrientDB Graph Database')
        print('=' * 55)
        print('  1.  Collect AI Security content')
        print('  2.  Preprocess and classify content')
        print('  3.  Store into OrientDB graph')
        print('  4.  Show all available topics')
        print('  5.  Search a topic (BFS traversal)')
        print('  6.  Graph Traversal (BFS/DFS/Shortest Path)')
        print('  7.  Bidirectional Graph Traversal')
        print('  8.  List all research papers')
        print('  9.  Take Manual Quiz (42 questions)')
        print('  10. Take Auto-Generated Quiz')
        print('  11. Graph Analysis and Benchmarks')
        print('  12. Show system status')
        print('  13. Visualize Graph (Open in Browser)')
        print('  14. Exit')
        print('=' * 55)
        choice = input('  Enter your choice (1-14): ')

        if choice == '1':
            run_collector()
        elif choice == '2':
            run_preprocessor()
        elif choice == '3':
            run_graph_manager()
        elif choice == '4':
            list_topics()
        elif choice == '5':
            run_query()
        elif choice == '6':
            run_traversal()
        elif choice == '7':
            run_bidirectional()
        elif choice == '8':
            show_papers()
        elif choice == '9':
            run_quiz()
        elif choice == '10':
            run_auto_quiz()
        elif choice == '11':
            run_analysis()
        elif choice == '12':
            show_status()
        elif choice == '13':
            visualize_graph()
        elif choice == '14':
            print('  Goodbye!')
            break
        else:
            print('  Invalid choice! Enter 1-14')

if __name__ == '__main__':
    main()