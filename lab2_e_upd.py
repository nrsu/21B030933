s = input().split()
if len(s) == 1:
    s.append(input())
arr=[[0]*int(s[0]) for i in range(int(s[0]))]
for i in range(0, int(s[0])):
    arr[i]=int(s[1])+2*i
xor=arr[0]
for j in range(0, int(s[0])-1):
    xor=xor^arr[j+1]
print(xor)