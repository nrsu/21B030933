n=int(input())
a=[[0]*n for i in range(n)]
if n%2==0:
    for i in range(0, n):
        for j in range(0, n):
            if i>=j:
                a[i][j]='#'
            else:
                a[i][j]='.'
    for m in range(0, n):
        for p in range(0, n):
            print(a[m][p], end='')
        print()
else:
    for x in range(0, n):
        for y in range(0, n):
            if x+y<n-1:
                a[x][y]='.'
            else:
                a[x][y]='#'
    for m in range(0, n):
        for p in range(0, n):
            print(a[m][p], end='')
        print()