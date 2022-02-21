str=""
def reverse():
    global str
    for i in wrds:
        str=i+" "+str   
wrds=input().split()
reverse()
print(str)