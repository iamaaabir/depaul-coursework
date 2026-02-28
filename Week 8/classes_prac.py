class Account:
    
    def set_balance(self, value):
        self.balance = value
        
    def deposit(self, num):
        self.balance = self.balance + num
        
    def get_balance(self):
        return self.balance
        
    def withdraw(self, val2):
        self.balance = self.balance - val2
        
    def __str__(self):
        return f'${self.balance:.2f}'
    
    def __repr__(self):
        return f'Account({self.balance})'
        
acct1 = Account()
acct1.set_balance(50)
print(acct1)
print(repr(acct1))
        
        