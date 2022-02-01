s=str(input())
txt=s[::-1]
cntr=0
sum=0
for i in txt:
    x=int(i)
    sum=x*(2**cntr)+sum
    cntr=cntr+1
print(sum)