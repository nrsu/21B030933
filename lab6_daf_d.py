file=open("C:\\Users\\Админ\\Desktop\\text\\textpy.txt","r")
textest=file.read()
textlist=textest.split("\n")
print(len(textlist))