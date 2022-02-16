cntr=0
numb=0
xyz={}
max=-9999999
n=int(input())
arr=list()
arnum=list()
for i in range(0, n):
    s=input().split()
    arr.append(f'{s[0]}')
    arnum.append(f'{s[1]}')
nam=set(arr)
namo=list(nam)
namo=sorted(namo)
for i in namo:
    for j in range(0, n):
        if i==arr[j]:
            numb=numb+int(arnum[j])
    xyz[i]=numb
    numb=0
for i in xyz.values():
    if i>max:
        max=i
for i in xyz.keys():
    if xyz[i]!=max:
        xyz[i]=max-xyz[i]
for i in xyz.keys():
    if xyz[i]==max:
        print(namo[cntr], "is lucky!")
    else:
        print(namo[cntr], "has to receive", xyz[i], "tenge")
    cntr=cntr+1