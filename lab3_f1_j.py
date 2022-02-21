h=list()
cntr=0
xyz={}
num=input().split()
def unique():
    global cntr
    for i in num:
        xyz[i]=cntr
        cntr=cntr+1
    for i in xyz.keys():
        h.append(i)
    return h
print(unique())