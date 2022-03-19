import os
path='C:\\Users\\Админ\\Desktop\\text\\test\\delete\\deleteme.txt'
if os.access(path, os.F_OK):
    os.remove(path)