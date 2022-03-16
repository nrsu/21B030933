import re
p=r'ab{2,3}'
s=str(input())
if re.search(p,  s):
        print('matches')
else:
        print('doesnt match')
