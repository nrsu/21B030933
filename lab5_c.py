import re
p=r'^[a-z]+_[a-z]+$'
s=str(input())
if re.search(p, s):
    print('matches')
else:
    print('doesnt match')