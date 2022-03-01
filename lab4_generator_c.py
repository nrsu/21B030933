def dvs():
    for i in range(0, n):
        if i%4==0:
            if i%3==0:
                yield i
n=int(input())
for i in dvs():
    print(i)