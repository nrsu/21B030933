from time import sleep
import math
num=int(input())
ms=int(input())
sleep(ms/1000)
print('Square root of',num, 'after',ms,'milliseconds is',math.sqrt(num))
