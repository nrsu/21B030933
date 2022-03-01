def squares():
    for i in range(a, b):
        x=i**2
        yield x
a, b=map(int, input().split())
for i in squares():
    print(i)