import os
path='C:\\Users\\Админ\\Desktop\\books'
p=os.listdir(path)
print("only directories:")
for i in p:
    if os.path.isdir(i):
        print(i)
print("only files:")
for i in p:
    if os.path.isdir(i)==False:
        print(i)
print("all directories and files:")
for i in p:
    print(i)
