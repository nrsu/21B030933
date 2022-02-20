class String():
    def __init__(self):
        self.strng=""
    def getString(self):
        self.strng=input()
    def printString(self):
        self.strng=self.strng.upper()
        print(self.strng)
strng=String()
strng.getString()
strng.printString()