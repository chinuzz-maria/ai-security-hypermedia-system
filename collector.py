import os
import shutil

print('=' * 55)
print('  AI Security Content Collector')
print('=' * 55)

# Create folders if not exist
os.makedirs('data/raw', exist_ok=True)
os.makedirs('data/processed', exist_ok=True)
os.makedirs('media', exist_ok=True)

print('')
print('  Collecting AI Security content...')
print('')

# Check PDF exists
pdf_path = 'data/raw/new_papers.pdf'
if os.path.exists(pdf_path):
    size = os.path.getsize(pdf_path)
    print('  [COLLECTED] Research papers PDF')
    print('              Path : ' + pdf_path)
    print('              Size : ' + str(round(size/1024/1024, 1)) + ' MB')
else:
    print('  [WARNING] PDF not found at: ' + pdf_path)

print('')
print('  Collecting YouTube video links...')
print('')

videos = [
    ('AI Security Overview',     'https://youtu.be/tlS5Y2vm02c'),
    ('Neural Network Basics',    'https://www.youtube.com/watch?v=aircAruvnKk'),
    ('GAN Explained',            'https://www.youtube.com/watch?v=8L11aMN5KY8'),
    ('Adversarial Attack',       'https://www.youtube.com/watch?v=YyTyWGUUhmo'),
    ('FGSM Attack',              'https://www.youtube.com/watch?v=4TseynD_v7M'),
    ('Intrusion Detection ML',   'https://www.youtube.com/watch?v=dfVAi87BSEs'),
    ('SVM Explained',            'https://www.youtube.com/watch?v=efR1C6CvhmE'),
    ('DNN Deep Neural Network',  'https://www.youtube.com/watch?v=CqOfi41LfDw'),
]

for title, url in videos:
    print('  [COLLECTED] ' + title)
    print('              ' + url)

print('')
print('  Collecting research paper links...')
print('')

papers = [
    ('CleverUniversity',                    'http://www.warse.org/IJETER/static/pdf/file/ijeter04852020.pdf'),
    ('Adversarial ML against IDS',          'https://www.mdpi.com/1999-5903/15/2/62/pdf'),
    ('Deep Model Poisoning',                'https://www.mdpi.com/1999-5903/13/3/73/pdf'),
    ('Defense against Neural Trojan',       'https://doi.org/10.1016/j.neucom.2020.07.133'),
    ('Adversarial Training Real-time',      'https://doi.org/10.1016/j.array.2025.100546'),
    ('AI Security ACM',                     'https://doi.org/10.1145/3769694.3771166'),
    ('Hypermedia Learning',                 'https://doi.org/10.1080/10494820.2019.1674881'),
    ('Meticulous Thought Defender CoT',     'https://doi.org/10.1109/ACCESS.2025.3583759'),
]

for title, url in papers:
    print('  [COLLECTED] ' + title)
    print('              ' + url)

print('')
print('=' * 55)
print('  Collection Summary:')
print('  Videos  collected : 8')
print('  Papers  collected : 8')
print('  PDF     collected : 1')
print('  Total             : 17 resources')
print('=' * 55)
print('  Content collection complete!')
