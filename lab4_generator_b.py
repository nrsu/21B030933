def even():
    for i in range(0, n+1):
        if i%2==0:
            yield i
n=int(input())
lst=list()
num=even()
x=0
for i in num:
    lst.append(str(i))
print (", ".join(lst))
