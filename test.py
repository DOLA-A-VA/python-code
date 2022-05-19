# 王秉濂    林宇軒  楊子弘  吳政霖  https://github.com/DOLA-A-VA/python-code.git

import os

if not os.path.exists('./data'):
    os.mkdir('./data')

with open('./data/f.txt' , 'w') as f_obj:
    f_obj.write('hello world')

print(os.path.basename('./data/f.txt'))

a = os.path.basename('./data/f.txt')
print(a.split('.')[1])