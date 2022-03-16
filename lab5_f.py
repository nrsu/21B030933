import re
s=str(input())
x=re.sub("\ ", ",", s)
x=re.sub("\.", ":", x)
print(x)