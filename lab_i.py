a=int(input())
rsl=''
cntr=0
for i in range(0, a):
    s=str(input())
    for x in s:
        cntr=cntr+1
    result=s.find('@gmail.com')
    if result+10==cntr and result>0:
        for y in s:
            if y=='@':
                break
            rsl=rsl+y
        print(rsl)
        rsl=''
    cntr=0
