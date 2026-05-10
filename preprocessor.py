import os
import json

# AI Security keywords for classification
ATTACK_KEYWORDS = ['attack', 'adversarial', 'fgsm', 'pgd', 'cw', 'malware', 'exploit', 'injection', 'ddos', 'blackbox', 'whitebox', 'gan', 'idsgan', 'evasion', 'perturbation']
DEFENSE_KEYWORDS = ['defense', 'detection', 'mitigation', 'protection', 'prevent', 'training', 'distillation', 'preprocessing', 'firewall', 'countermeasure']
TOOL_KEYWORDS = ['tool', 'framework', 'model', 'neural', 'network', 'svm', 'dnn', 'mlp', 'autoencoder', 'classifier', 'algorithm', 'deep learning']
DATASET_KEYWORDS = ['dataset', 'nsl-kdd', 'cicids', 'kdd', 'benchmark', 'data', 'traffic', 'samples']

# Your AI Security data from research papers
AI_SECURITY_DATA = [
    {
        'name': 'FGSM Attack',
        'description': 'Fast Gradient Sign Method adds tiny invisible noise to fool AI models',
        'type': 'Attack',
        'severity': 'High',
        'keywords': ['adversarial', 'fgsm', 'gradient', 'perturbation'],
        'video': 'https://www.youtube.com/watch?v=4TseynD_v7M',
        'related_defense': 'Adversarial Training',
        'related_tool': 'DNN'
    },
    {
        'name': 'PGD Attack',
        'description': 'Projected Gradient Descent is a stronger multi-step version of FGSM',
        'type': 'Attack',
        'severity': 'High',
        'keywords': ['adversarial', 'pgd', 'gradient', 'multi-step'],
        'video': 'https://www.youtube.com/watch?v=YyTyWGUUhmo',
        'related_defense': 'Adversarial Training',
        'related_tool': 'DNN'
    },
    {
        'name': 'Black-Box Attack',
        'description': 'Attacking an AI model without knowing its internal structure',
        'type': 'Attack',
        'severity': 'High',
        'keywords': ['blackbox', 'attack', 'evasion'],
        'video': 'https://www.youtube.com/watch?v=YyTyWGUUhmo',
        'related_defense': 'Preprocessing Defense',
        'related_tool': 'GAN'
    },
    {
        'name': 'IDSGAN',
        'description': 'Uses GAN to generate adversarial traffic to fool Intrusion Detection Systems',
        'type': 'Attack',
        'severity': 'Critical',
        'keywords': ['idsgan', 'gan', 'intrusion', 'evasion'],
        'video': 'https://www.youtube.com/watch?v=8L11aMN5KY8',
        'related_defense': 'Adversarial Training',
        'related_tool': 'GAN'
    },
    {
        'name': 'DDoS Attack',
        'description': 'Distributed Denial of Service attack using AI-generated traffic',
        'type': 'Attack',
        'severity': 'Critical',
        'keywords': ['ddos', 'attack', 'network', 'flood'],
        'video': 'https://www.youtube.com/watch?v=dfVAi87BSEs',
        'related_defense': 'Preprocessing Defense',
        'related_tool': 'GAN'
    },
    {
        'name': 'Adversarial Training',
        'description': 'Retrains AI model using adversarial examples to make it more robust',
        'type': 'Defense',
        'severity': 'N/A',
        'keywords': ['defense', 'training', 'adversarial', 'robust'],
        'video': 'https://www.youtube.com/watch?v=YyTyWGUUhmo',
        'related_defense': 'N/A',
        'related_tool': 'DNN'
    },
    {
        'name': 'Preprocessing Defense',
        'description': 'Cleans and filters input data before feeding to AI to remove adversarial noise',
        'type': 'Defense',
        'severity': 'N/A',
        'keywords': ['defense', 'preprocessing', 'filter', 'input'],
        'video': 'https://www.youtube.com/watch?v=tlS5Y2vm02c',
        'related_defense': 'N/A',
        'related_tool': 'MLP'
    },
    {
        'name': 'Defensive Distillation',
        'description': 'Trains a second model to smooth predictions and resist adversarial attacks',
        'type': 'Defense',
        'severity': 'N/A',
        'keywords': ['defense', 'distillation', 'smooth', 'robust'],
        'video': 'https://www.youtube.com/watch?v=tlS5Y2vm02c',
        'related_defense': 'N/A',
        'related_tool': 'DNN'
    },
    {
        'name': 'GAN',
        'description': 'Generative Adversarial Network - two AI models competing to generate and detect fake data',
        'type': 'Tool',
        'severity': 'N/A',
        'keywords': ['gan', 'generative', 'adversarial', 'network'],
        'video': 'https://www.youtube.com/watch?v=8L11aMN5KY8',
        'related_defense': 'N/A',
        'related_tool': 'N/A'
    },
    {
        'name': 'DNN',
        'description': 'Deep Neural Network - multi-layered AI model used in modern security systems',
        'type': 'Tool',
        'severity': 'N/A',
        'keywords': ['dnn', 'deep', 'neural', 'network'],
        'video': 'https://www.youtube.com/watch?v=CqOfi41LfDw',
        'related_defense': 'N/A',
        'related_tool': 'N/A'
    },
    {
        'name': 'SVM',
        'description': 'Support Vector Machine - classic ML classifier used in intrusion detection',
        'type': 'Tool',
        'severity': 'N/A',
        'keywords': ['svm', 'support', 'vector', 'classifier'],
        'video': 'https://www.youtube.com/watch?v=efR1C6CvhmE',
        'related_defense': 'N/A',
        'related_tool': 'N/A'
    },
    {
        'name': 'MLP',
        'description': 'Multi Layer Perceptron - basic neural network used in security classification',
        'type': 'Tool',
        'severity': 'N/A',
        'keywords': ['mlp', 'perceptron', 'neural', 'network'],
        'video': 'https://www.youtube.com/watch?v=aircAruvnKk',
        'related_defense': 'N/A',
        'related_tool': 'N/A'
    },
    {
        'name': 'NSL-KDD',
        'description': 'Most popular benchmark dataset for testing Intrusion Detection Systems',
        'type': 'Dataset',
        'severity': 'N/A',
        'keywords': ['dataset', 'nsl-kdd', 'benchmark', 'intrusion'],
        'video': 'https://www.youtube.com/watch?v=dfVAi87BSEs',
        'related_defense': 'N/A',
        'related_tool': 'N/A'
    },
    {
        'name': 'CICIDS2017',
        'description': 'Modern network traffic dataset containing realistic attack scenarios',
        'type': 'Dataset',
        'severity': 'N/A',
        'keywords': ['dataset', 'cicids', 'network', 'traffic'],
        'video': 'https://www.youtube.com/watch?v=dfVAi87BSEs',
        'related_defense': 'N/A',
        'related_tool': 'N/A'
    }
]

def classify_text(text):
    text_lower = text.lower()
    if any(k in text_lower for k in ATTACK_KEYWORDS):
        return 'Attack'
    elif any(k in text_lower for k in DEFENSE_KEYWORDS):
        return 'Defense'
    elif any(k in text_lower for k in TOOL_KEYWORDS):
        return 'Tool'
    elif any(k in text_lower for k in DATASET_KEYWORDS):
        return 'Dataset'
    else:
        return 'General'

def process_all():
    os.makedirs('data/processed', exist_ok=True)
    print('Processing AI Security data...')
    print('Total topics found: ' + str(len(AI_SECURITY_DATA)))
    counts = {'Attack': 0, 'Defense': 0, 'Tool': 0, 'Dataset': 0}
    for item in AI_SECURITY_DATA:
        t = item['type']
        if t in counts:
            counts[t] += 1
        print('  [' + item['type'] + '] ' + item['name'])
    with open('data/processed/classified_data.json', 'w') as f:
        json.dump(AI_SECURITY_DATA, f, indent=2)
    print('Classification complete!')
    print('  Attacks:  ' + str(counts['Attack']))
    print('  Defenses: ' + str(counts['Defense']))
    print('  Tools:    ' + str(counts['Tool']))
    print('  Datasets: ' + str(counts['Dataset']))
    print('Saved to data/processed/classified_data.json')
    return AI_SECURITY_DATA

if __name__ == '__main__':
    process_all()
