cntr=0
h=list()
def filter_prime():
    global cntr
    for i in num:
        for j in range(1, int(i)):
            if int(i)%j==0:
                cntr=cntr+1
        if cntr==1:
            h.append(i)
        cntr=0
num=input().split()
filter_prime()
print(h)