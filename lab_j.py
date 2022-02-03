s=str(input())
u=''
cntr=0
a=s.split()
b=len(a)
for i in range(0, b):
    for x in a[i]:
        cntr=cntr+1
    if cntr>=3:
        #print(a[i])
        u=u+a[i]+' '
    cntr=0
print(u)