import random

# ============================================================
# ATTACKS QUESTIONS
# ============================================================
attack_questions = [
    {
        'question': 'What does FGSM stand for?',
        'options': ['A. Fast Gradient Sign Method', 'B. Federated Gradient Security Model', 'C. Fast General Security Method', 'D. Forward Gradient Sign Model'],
        'answer': 'A',
        'explanation': 'FGSM = Fast Gradient Sign Method. It adds tiny invisible noise to input data to fool AI models into making wrong predictions.'
    },
    {
        'question': 'What does FGSM add to fool AI models?',
        'options': ['A. Visible watermarks', 'B. Large random noise', 'C. Tiny invisible perturbations', 'D. Encrypted data'],
        'answer': 'C',
        'explanation': 'FGSM adds tiny invisible perturbations (noise) to input data. These changes are so small humans cannot see them but they fool the AI model.'
    },
    {
        'question': 'What is the severity level of FGSM Attack?',
        'options': ['A. Low', 'B. Medium', 'C. High', 'D. Critical'],
        'answer': 'C',
        'explanation': 'FGSM Attack has High severity because it can fool any gradient-based AI model with minimal effort from the attacker.'
    },
    {
        'question': 'What does PGD stand for?',
        'options': ['A. Partial Gradient Defense', 'B. Projected Gradient Descent', 'C. Protected Graph Database', 'D. Partial Graph Detection'],
        'answer': 'B',
        'explanation': 'PGD = Projected Gradient Descent. It is a stronger multi-step version of FGSM that applies multiple small perturbations.'
    },
    {
        'question': 'How is PGD different from FGSM?',
        'options': ['A. PGD is weaker than FGSM', 'B. PGD uses single step like FGSM', 'C. PGD applies multiple steps making it stronger', 'D. PGD only works on images'],
        'answer': 'C',
        'explanation': 'PGD is a multi-step attack that applies perturbations iteratively making it much stronger than single-step FGSM.'
    },
    {
        'question': 'What is a Black-Box Attack?',
        'options': ['A. Attack using black colored data', 'B. Attacking AI model without knowing its internal structure', 'C. Attack only on hardware', 'D. Defense mechanism'],
        'answer': 'B',
        'explanation': 'Black-Box Attack means attacker has NO knowledge of the AI model internals. They only observe inputs and outputs to craft attacks.'
    },
    {
        'question': 'What is the severity of Black-Box Attack?',
        'options': ['A. Low', 'B. Medium', 'C. High', 'D. Critical'],
        'answer': 'C',
        'explanation': 'Black-Box Attack has High severity because it can attack ANY AI system without needing internal access making it very dangerous.'
    },
    {
        'question': 'What does IDSGAN use to generate adversarial traffic?',
        'options': ['A. DNN', 'B. SVM', 'C. MLP', 'D. GAN'],
        'answer': 'D',
        'explanation': 'IDSGAN uses GAN (Generative Adversarial Network) to generate adversarial traffic that fools Intrusion Detection Systems.'
    },
    {
        'question': 'What is the severity of IDSGAN?',
        'options': ['A. Low', 'B. Medium', 'C. High', 'D. Critical'],
        'answer': 'D',
        'explanation': 'IDSGAN has Critical severity because it specifically targets Intrusion Detection Systems making them completely blind to real attacks.'
    },
    {
        'question': 'What does DDoS stand for?',
        'options': ['A. Deep Denial of Service', 'B. Distributed Denial of Service', 'C. Dynamic Denial of Service', 'D. Direct Denial of Service'],
        'answer': 'B',
        'explanation': 'DDoS = Distributed Denial of Service. It uses multiple sources to flood a system with traffic making it unavailable.'
    },
    {
        'question': 'What is the severity level of DDoS Attack?',
        'options': ['A. Low', 'B. Medium', 'C. High', 'D. Critical'],
        'answer': 'D',
        'explanation': 'DDoS Attack has Critical severity because it uses AI-generated traffic to completely shut down systems and networks.'
    },
    {
        'question': 'Which attack specifically targets Intrusion Detection Systems?',
        'options': ['A. FGSM', 'B. PGD', 'C. IDSGAN', 'D. Black-Box'],
        'answer': 'C',
        'explanation': 'IDSGAN specifically targets Intrusion Detection Systems by using GAN to generate traffic that looks normal but contains attacks.'
    },
]

# ============================================================
# DEFENSES QUESTIONS
# ============================================================
defense_questions = [
    {
        'question': 'What does Adversarial Training do?',
        'options': ['A. Deletes adversarial examples', 'B. Retrains AI model using adversarial examples', 'C. Blocks all network traffic', 'D. Encrypts the model'],
        'answer': 'B',
        'explanation': 'Adversarial Training retrains the AI model using adversarial examples so the model learns to resist such attacks and becomes more robust.'
    },
    {
        'question': 'Which defense method cleans input data before feeding to AI?',
        'options': ['A. Adversarial Training', 'B. Defensive Distillation', 'C. Preprocessing Defense', 'D. Encryption'],
        'answer': 'C',
        'explanation': 'Preprocessing Defense cleans and filters input data BEFORE it reaches the AI model removing adversarial noise added by attackers.'
    },
    {
        'question': 'What is Defensive Distillation?',
        'options': ['A. Removing water from data', 'B. Training second model on soft predictions to resist attacks', 'C. Encrypting neural network', 'D. Deleting attack data'],
        'answer': 'B',
        'explanation': 'Defensive Distillation trains a second neural network using soft probability outputs of first model making it smoother and resistant to attacks.'
    },
    {
        'question': 'Which defense is best against FGSM and PGD attacks?',
        'options': ['A. Preprocessing Defense', 'B. Defensive Distillation', 'C. Adversarial Training', 'D. Encryption'],
        'answer': 'C',
        'explanation': 'Adversarial Training is most effective against FGSM and PGD because it trains the model on these exact attack types making it immune.'
    },
    {
        'question': 'Which defense works by filtering data BEFORE it reaches the model?',
        'options': ['A. Adversarial Training', 'B. Preprocessing Defense', 'C. Defensive Distillation', 'D. Model Encryption'],
        'answer': 'B',
        'explanation': 'Preprocessing Defense filters and cleans input data before it reaches the AI model acting as a shield against adversarial inputs.'
    },
    {
        'question': 'Which defense method uses probability outputs of one model to train another?',
        'options': ['A. Adversarial Training', 'B. Preprocessing Defense', 'C. Defensive Distillation', 'D. Data Augmentation'],
        'answer': 'C',
        'explanation': 'Defensive Distillation uses soft probability outputs (not hard labels) from first model to train second model making it more robust.'
    },
    {
        'question': 'Which defense mitigates Black-Box Attack?',
        'options': ['A. Adversarial Training', 'B. Preprocessing Defense', 'C. Defensive Distillation', 'D. Firewall'],
        'answer': 'B',
        'explanation': 'Preprocessing Defense mitigates Black-Box Attacks by cleaning and filtering inputs before they reach the model removing adversarial patterns.'
    },
    {
        'question': 'How many defense methods are in our AI Security system?',
        'options': ['A. 2', 'B. 3', 'C. 4', 'D. 5'],
        'answer': 'B',
        'explanation': 'Our system has 3 defense methods: Adversarial Training, Preprocessing Defense, and Defensive Distillation.'
    },
    {
        'question': 'Which defense is most suitable against DDoS attacks?',
        'options': ['A. Adversarial Training', 'B. Preprocessing Defense', 'C. Defensive Distillation', 'D. None'],
        'answer': 'B',
        'explanation': 'Preprocessing Defense helps against DDoS by filtering and cleaning malicious traffic before it reaches the system.'
    },
]

# ============================================================
# TOOLS QUESTIONS
# ============================================================
tool_questions = [
    {
        'question': 'What does GAN stand for?',
        'options': ['A. General Adversarial Node', 'B. Generative Adversarial Network', 'C. Graph Adversarial Network', 'D. General Attack Network'],
        'answer': 'B',
        'explanation': 'GAN = Generative Adversarial Network. Two AI models compete - one generates fake data and the other tries to detect it.'
    },
    {
        'question': 'What does DNN stand for?',
        'options': ['A. Distributed Neural Node', 'B. Deep Neural Network', 'C. Dynamic Network Node', 'D. Defense Neural Network'],
        'answer': 'B',
        'explanation': 'DNN = Deep Neural Network. It is a multi-layered AI model used in modern security systems for detecting attacks.'
    },
    {
        'question': 'What does SVM stand for?',
        'options': ['A. Security Virtual Machine', 'B. Support Vector Method', 'C. Support Vector Machine', 'D. System Virtual Model'],
        'answer': 'C',
        'explanation': 'SVM = Support Vector Machine. It is a classic ML classifier used in intrusion detection systems.'
    },
    {
        'question': 'What does MLP stand for?',
        'options': ['A. Multi Layer Perceptron', 'B. Machine Learning Protocol', 'C. Multiple Layer Processing', 'D. Model Learning Pattern'],
        'answer': 'A',
        'explanation': 'MLP = Multi Layer Perceptron. It is a basic neural network used in security classification tasks.'
    },
    {
        'question': 'Which tool is used by IDSGAN to generate adversarial traffic?',
        'options': ['A. DNN', 'B. SVM', 'C. GAN', 'D. MLP'],
        'answer': 'C',
        'explanation': 'IDSGAN uses GAN because GAN can generate realistic fake network traffic that looks normal but contains attack patterns.'
    },
    {
        'question': 'Which tool is used by FGSM Attack?',
        'options': ['A. GAN', 'B. DNN', 'C. SVM', 'D. MLP'],
        'answer': 'B',
        'explanation': 'FGSM Attack uses DNN (Deep Neural Network) because it exploits the gradient information of deep neural networks to create perturbations.'
    },
    {
        'question': 'Which tool is a classic ML classifier NOT a deep learning model?',
        'options': ['A. GAN', 'B. DNN', 'C. SVM', 'D. MLP'],
        'answer': 'C',
        'explanation': 'SVM (Support Vector Machine) is a classic machine learning classifier that does not use deep learning or neural networks.'
    },
    {
        'question': 'How many AI tools are in our security system?',
        'options': ['A. 2', 'B. 3', 'C. 4', 'D. 5'],
        'answer': 'C',
        'explanation': 'Our system has 4 tools: GAN, DNN, SVM, and MLP.'
    },
    {
        'question': 'Which tool consists of two competing AI models?',
        'options': ['A. DNN', 'B. SVM', 'C. MLP', 'D. GAN'],
        'answer': 'D',
        'explanation': 'GAN consists of two competing models - Generator creates fake data and Discriminator tries to detect fake vs real data.'
    },
    {
        'question': 'Which tool is used for basic neural network classification?',
        'options': ['A. GAN', 'B. DNN', 'C. SVM', 'D. MLP'],
        'answer': 'D',
        'explanation': 'MLP (Multi Layer Perceptron) is the most basic neural network used for classification tasks in security systems.'
    },
]

# ============================================================
# DATASETS QUESTIONS
# ============================================================
dataset_questions = [
    {
        'question': 'What does NSL-KDD stand for?',
        'options': ['A. Network Security Lab Knowledge Discovery Dataset', 'B. Neural Security Learning Knowledge Data', 'C. Network Supervised Learning Knowledge Discovery', 'D. None of the above'],
        'answer': 'A',
        'explanation': 'NSL-KDD = Network Security Lab Knowledge Discovery Dataset. It is a benchmark dataset for testing Intrusion Detection Systems.'
    },
    {
        'question': 'What does CICIDS2017 contain?',
        'options': ['A. Image data from 2017', 'B. Real network traffic from 2017 with attack types', 'C. Medical records from 2017', 'D. Social media data from 2017'],
        'answer': 'B',
        'explanation': 'CICIDS2017 contains realistic network traffic captured in 2017 including various attack types for IDS benchmarking.'
    },
    {
        'question': 'Which institute created CICIDS2017?',
        'options': ['A. MIT', 'B. Stanford', 'C. Canadian Institute for Cybersecurity', 'D. Oxford'],
        'answer': 'C',
        'explanation': 'CICIDS2017 was created by the Canadian Institute for Cybersecurity (CIC) specifically for intrusion detection research.'
    },
    {
        'question': 'Which dataset is used for testing Intrusion Detection Systems?',
        'options': ['A. MNIST', 'B. ImageNet', 'C. NSL-KDD', 'D. CIFAR-10'],
        'answer': 'C',
        'explanation': 'NSL-KDD is specifically designed for testing IDS systems containing labeled network traffic with attack and normal records.'
    },
    {
        'question': 'How many datasets are in our AI Security system?',
        'options': ['A. 1', 'B. 2', 'C. 3', 'D. 4'],
        'answer': 'B',
        'explanation': 'Our system has 2 datasets: NSL-KDD and CICIDS2017 both used for intrusion detection research.'
    },
    {
        'question': 'Which dataset is more recent?',
        'options': ['A. NSL-KDD', 'B. CICIDS2017', 'C. Both same year', 'D. Neither'],
        'answer': 'B',
        'explanation': 'CICIDS2017 is more recent as it was created in 2017 with modern attack types while NSL-KDD is an older benchmark dataset.'
    },
]

def run_category_quiz(category, questions, num_questions=None):
    print('')
    print('=' * 55)
    print('  ' + category + ' Quiz')
    print('=' * 55)

    if num_questions:
        selected = random.sample(questions, min(num_questions, len(questions)))
    else:
        selected = random.sample(questions, len(questions))

    score = 0
    total = len(selected)

    for i, q in enumerate(selected):
        print('')
        print('  Question ' + str(i+1) + ' of ' + str(total) + ':')
        print('')
        print('  ' + q['question'])
        print('')
        for opt in q['options']:
            print('    ' + opt)
        print('')
        answer = input('  Your answer (A/B/C/D): ').strip().upper()

        if answer == q['answer']:
            score += 1
            print('')
            print('  [CORRECT!]')
            print('  ' + q['explanation'])
        else:
            print('')
            print('  [WRONG!] Correct answer is: ' + q['answer'])
            print('  ' + q['explanation'])

    print('')
    print('=' * 55)
    print('  ' + category + ' Quiz Complete!')
    print('  Score      : ' + str(score) + '/' + str(total))
    percentage = int((score/total) * 100)
    print('  Percentage : ' + str(percentage) + '%')
    if percentage == 100:
        print('  [PERFECT! You mastered ' + category + '!]')
    elif percentage >= 80:
        print('  [EXCELLENT! Great knowledge of ' + category + '!]')
    elif percentage >= 60:
        print('  [GOOD! Keep studying ' + category + '!]')
    else:
        print('  [Study ' + category + ' more using option 5!]')
    print('=' * 55)
    return score, total

def run_quiz():
    while True:
        print('')
        print('=' * 55)
        print('  AI Security Quiz')
        print('  Choose Quiz Type:')
        print('=' * 55)
        print('  1. Attacks Quiz      (12 questions)')
        print('  2. Defenses Quiz     (9 questions)')
        print('  3. Tools Quiz        (10 questions)')
        print('  4. Datasets Quiz     (6 questions)')
        print('  5. Complete Quiz     (all topics)')
        print('  6. Back to main menu')
        print('=' * 55)
        choice = input('  Enter choice (1-6): ')

        if choice == '1':
            run_category_quiz('ATTACKS', attack_questions)
        elif choice == '2':
            run_category_quiz('DEFENSES', defense_questions)
        elif choice == '3':
            run_category_quiz('TOOLS', tool_questions)
        elif choice == '4':
            run_category_quiz('DATASETS', dataset_questions)
        elif choice == '5':
            print('')
            print('  COMPLETE QUIZ - All Topics!')
            total_score = 0
            total_questions = 0

            s, t = run_category_quiz('ATTACKS', attack_questions, 5)
            total_score += s
            total_questions += t

            s, t = run_category_quiz('DEFENSES', defense_questions, 3)
            total_score += s
            total_questions += t

            s, t = run_category_quiz('TOOLS', tool_questions, 4)
            total_score += s
            total_questions += t

            s, t = run_category_quiz('DATASETS', dataset_questions, 2)
            total_score += s
            total_questions += t

            print('')
            print('=' * 55)
            print('  FINAL SCORE - ALL TOPICS')
            print('=' * 55)
            print('  Total Score : ' + str(total_score) + '/' + str(total_questions))
            percentage = int((total_score/total_questions) * 100)
            print('  Percentage  : ' + str(percentage) + '%')
            print('')
            if percentage == 100:
                print('  [PERFECT! AI Security Expert!]')
            elif percentage >= 80:
                print('  [EXCELLENT! Great overall knowledge!]')
            elif percentage >= 60:
                print('  [GOOD! Review weak topics using option 5!]')
            elif percentage >= 40:
                print('  [FAIR! Study all topics and try again!]')
            else:
                print('  [Study all topics first using option 5!]')
            print('=' * 55)
        elif choice == '6':
            break
        else:
            print('  Invalid choice! Enter 1-6')

if __name__ == '__main__':
    run_quiz()
