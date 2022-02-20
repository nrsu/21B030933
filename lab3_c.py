class Shape():
    def __init__(self):
        pass
    def area(self):
        print(0)
class Square(Shape):
    def __init__(self, length):
        self.length=length
    def area(self):
        print(self.length**2)
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length=length
        self.width=width
    def area(self):
        print(self.length*self.width)
x, y=map(int, input().split())
z=Rectangle(x, y)
z.area()