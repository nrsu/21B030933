import os
path='C:\\Users\\Админ\\Desktop\\books'
print('exist')
if os.access(path, os.F_OK):
    print(True)
else:
    print(False)
print('readable')
if os.access(path, os.R_OK):
    print(True)
else:
    print(False)
print('writable')
if os.access(path, os.W_OK):
    print(True)
else:
    print(False)
print('executable')
if os.access(path, os.X_OK):
    print(True)
else:
    print(False)