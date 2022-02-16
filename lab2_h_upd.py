cntr=0
xyz={}
x, y=map(int, input().split())
n=int(input())
arr=list()
arrone=list()
arrtwo=list()
sqr=list()
for i in range(0, n):
    x1, y1=map(int, input().split())
    arrone.append(f'{x1}')
    arrtwo.append(f'{y1}')
    arr.append(f'{x1} {y1}')
for i in range(0, n):
    h=(int(arrone[i])-x)**2+(int(arrtwo[i])-y)**2
    xyz[i]=h
val=list(xyz.values())
val=sorted(val)
for i in val:
    for j in range(0, n):
        if xyz[j]==i:
            print(arr[j])
            del xyz[j]