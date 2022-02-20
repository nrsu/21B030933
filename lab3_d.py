import math
class Point():
    def __init__(self, x, y, x1, y1):
        self.x = x
        self.y = y
    def show(self):
        return self.x, self.y
    def move(self):
        self.x = x-1
        self.y = y-1
        return self.x, self.y
    def dist(self):
        self.x=x
        self.y=y
        self.x1=x1
        self.y1=y1
        return math.sqrt((x-x1)**2+(y-y1)**2)
x, y=map(int, input().split())
x1, y1=map(int, input().split()) 
z=Point(x, y, x1, y1)
print(z.show())
print(z.move())
print(z.dist())