import re
s=str(input())
x=re.sub(r"(\w)([A-Z])", r"\1_\2", s)
x=x.lower()
print(x)