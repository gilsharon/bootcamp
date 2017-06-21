import os
if os.path.isfile('mastery.txt'):
    print('file exists')
else:
    with open('mastery.txt', 'w') as f:
        f.write('aaaaaassss/n')
        f.write('aaaaaassss/n')
