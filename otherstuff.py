# RPG game

# still need to write up the plan for this but oh well

# ---- All the ABCs go here ----


class Creature:

    # shall be extended with different types of class (e.g. aviary, ground-based, water, hostile, etc. )
    
    def __init__(self, name, creatureType, speed, damage, items, location):
        self.name = name
        self.type = creatureType
        self.speed = speed
        self.damage = damage
        self.items = items # their inventory - will be an array containing Item objects
        self.location = location


    def move(self, locx, locy):
        # move this creature to another location
        # check if the location can be moved to, given the obstacles that might be facing this creature

        # this is the case for now - later will be subject to conditions
        self.location = (locx, locy)



     


class Item:

    def __init__(self, itemType, name, owner=None):

        # create the attributes of the item
        # contains all of the information for what the item is, including the name, description, etc.
        # abstract class extended for weapons, food, medicine, and all other types of item

        self.type = itemType
        self.name = name
        self.owner = owner
        


# -------------------------------
# ---- Other classes go here ----
# -------------------------------


# ---- Creatures of all kinds ----


class Player(Creature):
 
    # a particular type of creature
    # the players that are part of the party

    # 'role' is the specific feature of the player object

    def __init__(self, speed=5, damage=10):

        
        
        super().__init__('', 'Player', speed, damage, [], (0, 0)) # create a creature object
        self._roles = {'1': 'Knight', '2': 'Wizard', '3': 'Explorer'} 
        self.createPlayer() # create the player part of the object


    def createPlayer(self):

        # get the name of the player

        print(self.name + " is the name of the superclass")

        self.name = input('What is your name? ')



        # create the role of the player - this allows the instantiation process to be done with only a single line later on

        self.role = None

        while self.role == None:
            self.role = self.checkRole(input("What role do you want? "))
        self.cash = 0

    

    def checkRole(self, role):

        # method of checking if the role entered is correct

        if str(role) not in self._roles:
            print("That's not a valid role! \n")
            return None
        return self._roles[str(role)]


class Monster(Creature):
    # thing that is hostile to the player
    

    def __init__(self, name, damage, speed=5):
        super().__init__(name, 'Monster', speed, damage, [], (0, 0)) # make a Creature class


# ---- Items ----

class Weapon(Item):

    # any kind of item that can be used to inflict damage on another thing

    _weapons = [] # list of all the items of this type

    def __init__(self, weapon_type, damage=None):

        super().__init__('Weapon', weapon_type, damage)
        Weapon._weapons.append(self)

    @classmethod

    def getList(self):
        
        for i in Weapon._weapons:
            print(i.__dict__)





def main():

    # main function for testing stuff

    # creation of a player

    newPlayer = Player(15, 100)

    print("The role type of %s is %s. " % (newPlayer.name, newPlayer.role))
    print("The speed is {s} and the damage is: {f}".format(s=newPlayer.speed, f=newPlayer.damage))

    # creation of a monster

    newMonster = Monster('Zombie', 10)

    for i in newMonster.__dict__:
        print(newMonster.__dict__[i])

    newWeapon = Weapon('Sword', 10) # create a new weapon object

    newWeapon2 = Weapon('Gun', 50) # other weapon in _weapons

    Weapon.getList()

    



main()