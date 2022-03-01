def down():
    for i in range(0, n+1):
        x=n-i
        yield x
n=int(input())
for i in down():
    print(i) 