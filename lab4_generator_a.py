n=int(input())
def square():
    for i in range(1, n+1):
        yield i
num=square()
x=0
while x<n:
    print(next(num)**2)
    x=1+x