n=int(input())
a=[[0] * n for i in range(n)]
for i in range(0, n):
    for j in range(0, n):
        a[i][j]=0
for x in range(0, n):
    a[x][0]=x
    a[0][x]=x
    a[x][x]=x*x
for p in range(0, n):
    for k in range(0, n):
        print(a[p][k], end=' ')
    print()