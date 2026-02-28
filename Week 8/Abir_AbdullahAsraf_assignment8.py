# Problem 1

class Player:
    '''This class represents a video game player.'''

    def __init__(self, level=1, hp=100, name='Ashen One'):
        '''Initializes the player's level, hp and name.'''

        self.level = level
        self.hp = hp
        self.name = name

# Problem 2

class Player:
    '''This class represents a video game player.'''

    def __init__(self, level=1, hp=100, name='Ashen One'):
        '''Initializes the player's level, hp and name.'''

        self.level = level
        self.hp = hp
        self.name = name

    def level_up(self):
        '''Increases the player's level by 1.'''
        self.level += 1

    def take_damage(self, amount):
        '''Reduces the player's hp by the amount provided.'''
        self.hp = self.hp - amount

    def __str__(self):
        '''Returns a formatted statistic of the player.'''
        return (f'Name: {self.name}\n'
                f'Current level: {self.level}\n'
                f'Current hit points: {self.hp}')

# Problem 3

class Enemy:
    '''This class represents an enemy from a video game.'''

    damage_multiplier = 3
    armor_bonus = 10

    def __init__(self, hp=30, base_damage=2):
        '''Initializes using default arguments the enemy's hp and base dmg.'''
        self.hp = hp
        self.base_damage = base_damage

# Problem 4

class Enemy:
    '''This class represents an enemy from a video game.'''

    damage_multiplier = 3
    armor_bonus = 10

    def __init__(self, hp=30, base_damage=2):
        '''Initializes using default arguments the enemy's hp and base dmg.'''
        self.hp = hp
        self.base_damage = base_damage
        self.armor = Enemy.armor_bonus

    def deal_damage(self):
        '''Returns the damage done by the enemy.'''
        return self.base_damage * Enemy.damage_multiplier

    def take_damage(self, damage_value):
        '''Applies damage to the armor first, and then to the hp.'''

        if self.armor >= damage_value:
            self.armor = self.armor - damage_value
        else:
            remaining_damage = damage_value - self.armor
            self.armor = 0
            self.hp = self.hp - remaining_damage









