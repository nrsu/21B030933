import re
s=str(input())
p=r'[A-Z]+[a-z]+'
if re.search(p, s):
    print('matches')
else:
    print('doesnt match')