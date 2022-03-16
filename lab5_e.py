import re
s=str(input())
p=r'a.+b'
if re.search(p, s):
    print('matches')
else:
    print('doesnt match')