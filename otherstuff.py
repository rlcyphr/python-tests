# making classes in python 2.7

# RPG game

class Creature(object):

    # shall be extended with different types of class (e.g. aviary, ground-based, water, hostile, etc. )
    
    def __init__(self, name, creatureType, speed, damage, items):
        self.name = name
        self.type = creatureType
        self.speed = speed
        self.damage = damage
        self.items = items # their inventory - will be an array containing Item objects


class Item(object):
    def __init__(self, itemType, owner, name):

        # create the attributes of the item
        # contains all of the information for what the item is, including the name, description, etc.
        # abstract class extended for weapons, food, medicine, and all other types of item

        self.type = itemType
        self.owner = owner
        self.name = name


class Player(Creature):

    # a particular type of creature
    # the players that are part of the party

    def __init__(self, cash, role):
        self.cash = 0
        self.role = role

    

