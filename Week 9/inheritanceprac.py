class Account(object):
    'a bank account class'

    bank_name = 'Chase' #a class variable
    
    def __init__(self, balance = 0):
        '''constructor'''
        
        self.balance = balance

    def set_balance(self, value):
        'set the balance to value'
        self.balance = value   #an instance variable

    def get_balance(self):
        'return the current balance on the account'
        return self.balance    #an instance variable
        
    def deposit(self, value):
        self.balance += value
        
    def withdraw(self, value):
        self.balance -= value
        
    def __str__(self):
        return f'${self.balance}'
        
    def __repr__(self):
        return f'Account({self.balance})'

    def __gt__(self, other):
        if self.balance > other.balance:
            return True
        else:
            return False

    def __add__(self, other):
        return Account(self.balance + other.balance)
        
class Savings(Account):
    '''a savings account'''

    def __init__(self, balance=0, rate=0.0):
        '''constructor'''
        #self.balance = balance
        super().__init__(balance)
        self.rate = rate
    
    def set_rate(self, value):
        '''set the yearly interest rate'''
        self.rate = value

    def add_interest(self):
        '''add one month of interest to the balance'''
        self.balance += self.balance*(self.rate/12)

    def get_balance(self):
        '''prints the value of the balance'''
        print(f'balance = ${self.balance:.2f}\nrate = {self.rate}%')
        
class Animal:
    '''A representation of any kind of animal'''

    def __init__(self, species = 'pug', language = 'snore'):
        '''constructor'''
        self.species = species
        self.language = language

    def __add__(self, other):
        '''concatenates species and languages'''
        new_species = self.species + other.species
        new_language = self.language + other.language
        return Animal(new_species, new_language)

    def set_species(self, species):
        '''sets the animal's species'''
        self.species = species

    def set_language(self, language):
        '''sets the animal's language'''
        self.language = language

    def speak(self):
        '''makes the animal speak'''
        return f'I am a {self.species} and I {self.language}'
        
    def __eq__(self, other):
        if self.species == other.species and if self.language == other.language:
            return True
        else:
            return False
            
    def __add__(self, other):
        new_species = self.species + other.species
        new_language = self.language + other.language
        return Animal(new_species, new_language)
        
class Bird(Animal):
    '''subclass of Animal class'''
    
    def __init__(self, language = 'chirp'):
        super().__init__('bird', language)
        
    def fly(self, value):
        print(f'I am flying {value} feet.')
        
    def __repr__(self):
        return f'Bird({self.language})'
        
    def __str__(self):
        return self.speak()
        
eagle = Bird()
print(repr(eagle))
print(eagle)
    
        
        
        
        
        

