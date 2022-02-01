dish=str(input())
counter=0
for i in dish:
    counter+=ord(i)
if counter<300:
    print('Oh, no!')
else:
    print('It is tasty!')
