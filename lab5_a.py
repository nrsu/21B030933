import re
p=r'^a(b*)$'
s=str(input())
if re.search(p, s):
    print('matches')
else:
    print('doesnt match')