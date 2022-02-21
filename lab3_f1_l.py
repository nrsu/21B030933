str=""
def histogram():
    global str
    for i in num:
        for j in range(0, int(i)):
            str="*"+str
        print(str)
        str=""      
num=input().split()
histogram()