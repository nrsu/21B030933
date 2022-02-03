a=int(input())
b=str(input())
if b=='k':
    c=int(input())
    r=round(a/1024, c)
    print(r)
    #
else:
    print(a*1024)