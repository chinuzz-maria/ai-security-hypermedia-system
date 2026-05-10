import requests
import random

BASE_URL = 'http://localhost:2480'
AUTH = ('root', 'root')

def run(sql):
    r = requests.post(BASE_URL + '/command/AISecurityDB/sql',
                      auth=AUTH, json={'command': sql})
    return r.json().get('result', [])

def generate_questions():
    questions = []

    # Get all nodes
    all_nodes   = run('SELECT * FROM V')
    attacks     = run('SELECT * FROM Attack')
    defenses    = run('SELECT * FROM Defense')
    tools       = run('SELECT * FROM Tool')
    datasets    = run('SELECT * FROM Dataset')
    all_names   = [n.get('name', '') for n in all_nodes if n.get('name')]

    # Question Type 1: What mitigates this attack?
    mit_edges = run('SELECT out().name as attack, in().name as defense FROM mitigated_by')
    for edge in mit_edges:
        attack  = edge.get('attack', '')
        defense = edge.get('defense', '')
        if not attack or not defense:
            continue

        wrong_defenses = [d.get('name', '') for d in defenses
                          if d.get('name', '') != defense][:3]
        if len(wrong_defenses) < 3:
            continue

        options = [defense] + wrong_defenses
        random.shuffle(options)
        correct = chr(65 + options.index(defense))

        questions.append({
            'question': 'Which defense method mitigates ' + attack + '?',
            'options':  options,
            'answer':   correct,
            'explanation': defense + ' is the defense that mitigates ' +
                           attack + ' by reducing the effectiveness of the attack.'
        })

    # Question Type 2: What does this attack use?
    uses_edges = run('SELECT out().name as attack, in().name as tool FROM uses')
    for edge in uses_edges:
        attack = edge.get('attack', '')
        tool   = edge.get('tool', '')
        if not attack or not tool:
            continue

        wrong_tools = [t.get('name', '') for t in tools
                       if t.get('name', '') != tool][:3]
        if len(wrong_tools) < 3:
            continue

        options = [tool] + wrong_tools
        random.shuffle(options)
        correct = chr(65 + options.index(tool))

        questions.append({
            'question': 'Which tool does ' + attack + ' use?',
            'options':  options,
            'answer':   correct,
            'explanation': attack + ' uses ' + tool +
                           ' as its primary tool or technique.'
        })

    # Question Type 3: What category is this topic?
    for node in all_nodes:
        name  = node.get('name', '')
        ntype = node.get('@class', '')
        if not name or not ntype:
            continue

        wrong_types = [t for t in ['Attack', 'Defense', 'Tool', 'Dataset']
                       if t != ntype]
        options = [ntype] + wrong_types
        random.shuffle(options)
        correct = chr(65 + options.index(ntype))

        questions.append({
            'question': 'Which category does ' + name + ' belong to?',
            'options':  options,
            'answer':   correct,
            'explanation': name + ' is a ' + ntype +
                           ' in the AI Security knowledge graph.'
        })

    # Question Type 4: What is the severity?
    for node in attacks:
        name     = node.get('name', '')
        severity = node.get('severity', '')
        if not name or not severity or severity == 'NA':
            continue

        wrong_sev = [s for s in ['High', 'Critical', 'Medium', 'Low']
                     if s != severity][:3]
        options = [severity] + wrong_sev
        random.shuffle(options)
        correct = chr(65 + options.index(severity))

        questions.append({
            'question': 'What is the severity level of ' + name + '?',
            'options':  options,
            'answer':   correct,
            'explanation': name + ' has ' + severity +
                           ' severity because it poses significant threat to AI systems.'
        })

    # Question Type 5: What is the difficulty level?
    for node in all_nodes:
        name  = node.get('name', '')
        diff  = node.get('difficulty', '')
        if not name or not diff:
            continue

        wrong_diff = [d for d in ['Beginner', 'Intermediate', 'Advanced']
                      if d != diff]
        options = [diff] + wrong_diff
        random.shuffle(options)
        correct = chr(65 + options.index(diff))

        questions.append({
            'question': 'What is the difficulty level of ' + name + '?',
            'options':  options,
            'answer':   correct,
            'explanation': name + ' is classified as ' + diff +
                           ' level in the AI Security learning path.'
        })

    return questions

def run_auto_quiz():
    print('')
    print('=' * 55)
    print('  AI Security Auto-Generated Quiz')
    print('  Questions generated from OrientDB graph!')
    print('=' * 55)

    print('  Generating questions from database...')
    questions = generate_questions()

    if not questions:
        print('  No questions generated! Check OrientDB.')
        return

    print('  Generated ' + str(len(questions)) + ' questions!')
    print('')
    print('  How many questions do you want?')
    print('  1. Quick Quiz  (5 questions)')
    print('  2. Medium Quiz (10 questions)')
    print('  3. Full Quiz   (all ' + str(len(questions)) + ' questions)')
    print('')
    choice = input('  Enter choice (1/2/3): ')

    if choice == '1':
        selected = random.sample(questions, min(5, len(questions)))
    elif choice == '2':
        selected = random.sample(questions, min(10, len(questions)))
    else:
        selected = random.sample(questions, len(questions))

    score = 0
    total = len(selected)

    for i, q in enumerate(selected):
        print('')
        print('=' * 55)
        print('  Question ' + str(i+1) + ' of ' + str(total) + ':')
        print('')
        print('  ' + q['question'])
        print('')
        for j, opt in enumerate(q['options']):
            print('    ' + chr(65+j) + '. ' + opt)
        print('')
        answer = input('  Your answer (A/B/C/D): ').strip().upper()

        if answer == q['answer']:
            score += 1
            print('')
            print('  [CORRECT!]')
            print('  ' + q['explanation'])
        else:
            print('')
            print('  [WRONG!] Correct answer is: ' +
                  q['answer'] + '. ' + q['options'][ord(q['answer'])-65])
            print('  ' + q['explanation'])

    print('')
    print('=' * 55)
    print('  AUTO QUIZ COMPLETE!')
    print('  Score      : ' + str(score) + '/' + str(total))
    percentage = int((score/total)*100)
    print('  Percentage : ' + str(percentage) + '%')
    print('')
    if percentage == 100:
        print('  [PERFECT! AI Security Expert!]')
    elif percentage >= 80:
        print('  [EXCELLENT! Great knowledge!]')
    elif percentage >= 60:
        print('  [GOOD! Keep studying!]')
    else:
        print('  [Study more topics using option 5!]')
    print('=' * 55)

if __name__ == '__main__':
    run_auto_quiz()
