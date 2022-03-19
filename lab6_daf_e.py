lst=['Abc', 'car', 'Apple', '15948', 'green', 'dog']
with open('C:\\Users\\Админ\\Desktop\\text\\textpy1.txt', "w") as file:
    for x in lst:
        file.write("%s "%x)
textest=open('C:\\Users\\Админ\\Desktop\\text\\textpy1.txt')
print(textest.read())
