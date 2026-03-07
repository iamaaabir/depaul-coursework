class Character:
    '''This class represents a general character of a game.'''

    def __init__(self, name='Tom Nook', level=1, hp=50):
        '''Initializes the player's level, hp and name.'''
        self.name = name
        self.level = level
        self.hp = hp

    def __str__(self):
        '''Returns a formatted statistic of the player.'''
        return (f'Name: {self.name}\n'
                f'Current level: {self.level}\n'
                f'Current hit points: {self.hp}')

    def __add__(self, other):
        '''Returns a combined total of name objects, level and hp.'''
        new_name = f'Team {self.name} and {other.name}'
        new_level = self.level + other.level
        new_hp = self.hp + other.hp

        return Character(new_name, new_level, new_hp)

    def __eq__(self, other):
        '''Checks if two characters have the same hp and level.'''
        if self.hp == other.hp and self.level == other.level:
            return True
        else:
            return False

class Enemy(Character):
    '''This class represents an enemy from a video game.'''

    damage_multiplier = 3
    armor_bonus = 10

    def __init__(self, hp=30, base_damage=2, name='Tom Nook', level=1):
        '''Initializes using default arguments the enemy's hp and base dmg.'''

        super().__init__(name, level, hp)

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

    def __str__(self):
        '''Returns a formatted statistic of the player.'''
        return (f'Enemy Name: {self.name}\n'
                f'Enemy Current level: {self.level}\n'
                f'Enemy Current hit points: {self.hp}\n'
                f'Enemy Base damage: {self.base_damage}')

    def __eq__(self, other):
        '''Checks equality of the parent class and also checks base damage equality.'''

        return super().__eq__(other) and self.base_damage == other.base_damage

class Player(Character):
    '''This class represents a video game player.'''

    def __init__(self, level=1, hp=100, name='Ashen One'):
        '''Initializes the player's level, hp and name.'''

        super().__init__(name, level, hp)

    def level_up(self):
        '''Increases the player's level by 1.'''
        self.level += 1

    def take_damage(self, amount):
        '''Reduces the player's hp by the amount provided.'''
        self.hp = self.hp - amount

    def __str__(self):
        '''Returns a formatted statistic of the player.'''
        return (f'Player Name: {self.name}\n'
                f'Player Current level: {self.level}\n'
                f'Player Current hit points: {self.hp}')


