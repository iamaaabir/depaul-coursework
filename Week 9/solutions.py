class Animal:
    '''A representation of any kind of animal'''

    def __init__(self, species = 'pug', language = 'snore'):
        '''constructor'''
        self.species = species
        self.language = language

    def __repr__(self):
        '''returns Animal(species, language)'''
        return f'Animal({self.species}, {self.language})'

    def __str__(self):
        return self.speak()

    def set_species(self, species):
        '''sets the animal's species'''
        self.species = species

    def set_language(self, language):
        '''sets the animal's language'''
        self.language = language

    def speak(self):
        '''makes the animal speak'''
        return f'I am a {self.species} and I {self.language}'

class Account:
    'a bank account class'

    bank = 'Chase'

    def print(self):
        '''showcase class variable usage'''
        print(self.bank)

    def __init__(self, value = 0):
        '''constructor'''
        self.balance = value

    def __str__(self):
        '''returns pretty string of balance'''
        if type(self.balance) is int:
            pretty_print = f'${self.balance}.00'
        else:
            pretty_print = f'${self.balance}'
        return pretty_print

    def __repr__(self):
        return f'Account({self.balance})'

    def __gt__(self, other):
        '''compares balances'''
        return self.balance > other.balance

    def __add__(self, rhs):
        '''add balances'''
        return Account(self.balance + rhs.balance)

    def set_balance(self, value):
        'set the balance to value'
        self.balance = value

    def get_balance(self):
        'return the current balance on the account'
        return self.balance

    def deposit(self, value):
        '''add value to balance'''
        try:
            self.balance += value
        except:
            self.balance = value

    def withdraw(self, value):
        '''subtracts value from balance'''
        self.balance -= value

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

    def __eq__(self, other):
        '''compares species and language'''
        #if self.species == other.species:
        #    if self.language == other.language:
        #        return True
        #return False
        return self.species == other.species and self.language == other.language

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

class Bird(Animal):
    '''Bird-specific animal class'''

    def __init__(self, language = 'chirp'):
        '''constructor'''
        super().__init__('bird', language)

    def __repr__(self):
        '''canonical string repr'''
        return f'Bird({self.language})'

    def __str__(self):
        '''pretty print str'''
        return self.speak()

    def fly(self, height):
        '''make bird fly at height'''
        print(f'I am flying {height} feet')









        
