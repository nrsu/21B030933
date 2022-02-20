class Account():
    def __init__(self, owner, balance):
        self.owner=owner
        self.balance=balance
    def info(self):
        return('Owner: {}\nBalance: {}'.format(self.owner, self.balance))
    def deposit(self):
        print("Enter the amount of money you want to add to the deposit")
        dpst=int(input())
        self.balance=int(self.balance)+dpst
        return('Owner: {}\nBalance: {}'.format(self.owner, self.balance))
    def withdraw(self):
        print("Enter the amount of money you want to withdraw")
        wthdrw=int(input())
        self.balance=self.balance-wthdrw
        if self.balance>=0:
            return('Owner: {}\nBalance: {}'.format(self.owner, self.balance))
        else:
            return('OVERDRAWN!')

x,y=input().split()
z=Account(x,y)
print(z.info())
print(z.deposit())
print(z.withdraw())