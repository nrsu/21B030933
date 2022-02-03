word=str(input())
emp=''
ltr=str(input())
g=list(word)
sz=len(g)
for i in range(0, sz):
    if g[i]==ltr:
        emp=emp+str(i)
        frs=i
        break
rvrs=g[::-1]
for x in range(0, sz):
    if rvrs[x]==ltr:
        emp=emp+' '+str(sz-x-1)
        scnd=sz-x-1
        break
if frs==scnd:
    print(frs)
else:
    print(emp)