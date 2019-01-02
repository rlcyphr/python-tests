# RPG game

# still need to write up the plan for this but oh well

# ---- All the ABCs go here ----


class Creature:

    # shall be extended with different types of class (e.g. aviary, ground-based, water, hostile, etc. )
    
    def __init__(self, name, creatureType, speed, damage, items, location, holding=None):
        self.name = name
        self.type = creatureType
        self.speed = speed
        self.damage = damage
        self.items = items # their inventory - will be an array containing Item objects (can hold a maximum of 15 items)
        self.location = location
        self.holding = holding


    def move(self, locx, locy):
        # move this creature to another location
        # check if the location can be moved to, given the obstacles that might be facing this creature

        # this is the case for now - later will be subject to conditions
        self.location = (locx, locy)



     


class Item:

    def __init__(self, itemType, owner=None):

        # create the attributes of the item
        # contains all of the information for what the item is, including the description, etc.
        # abstract class extended for weapons, food, medicine, and all other types of item

        self.type = itemType
        self.owner = owner


        


# ---------------------------------------
# ---- Creature-type classes go here ----
# ---------------------------------------


# ---- Creatures of all kinds ----


class Player(Creature):
 
    # a particular type of creature
    # the players that are part of the party

    # 'role' is the specific feature of the player object

    # all players will be put in the (1, 1) region, from 0 to 50 on each axis

    def __init__(self, speed=5, damage=10):

        
        
        super().__init__('', 'Player', speed, damage, [], (0, 0)) # create a creature object
        self._roles = {'1': 'Knight', '2': 'Wizard', '3': 'Explorer'} 
        self.createPlayer() # create the player part of the object


    def createPlayer(self):

        # get the name of the player

        self.name = input('What is your name? ')

        print(self.name + " is the name of the superclass")

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

    def addItem(self, *args):
        # this is going to be used to set the inventory of a user.
        # *args allows this to be filled with an arbitrary amount of things to add to the inv

        # will fill the inventory of the player - different way to how creatures' inventory will work (set items that cannot change in any way once set)

        print(self.items)





class Monster(Creature):
    # thing that is hostile to the player
    

    def __init__(self, name, damage, speed=5):
        super().__init__(name, 'Monster', speed, damage, [], (0, 0)) # make a Creature class


#----------------------------
# ---- Item Type Classes ----
# ---------------------------


class Weapon(Item):

    # any kind of item that can be used to inflict damage on another thing

    _weapons = [] # list of all the items of this type

    def __init__(self, weapon_type, damage):

        # weapon_type is the specific type of weapon that this is
        # and damage is the amount of damage that this thing can inflict


        super().__init__('Weapon') # make an 'Item' type - second argument will be the owner of this weapon
        self.setWeapon(weapon_type, damage) 
        Weapon._weapons.append(self)


    def setWeapon(self, weapon_type, damage):
        # set the specific things for this type of item
        self.weapon_type = weapon_type
        self.damage = damage




    @classmethod
    def getList(self):
        # get a list of all of the weapon type items that exist, including the type, owner, and damage
        for i in Weapon._weapons:
            print(i.__dict__)


# ----------------------------------
# ---- World-associated classes ----
# ----------------------------------

class Region:

    _regions = {} 

    # list of all regions in the map
    # regions are created east and west, north and south of the starting point, and are 50x50 spaces each. 
    # Each region is referred to by how many spaces in each of the directions it is: for instance, if a region
    # is 1 space west and 3 spaces south, it would be set as a tuple (-1, 3) 

    def __init__(self, x, y):


        # build a region that is 50x50, and which has a certain position on the map
        # the region will be created empty, and populated with items once it has been
        # instantiated.

        self.area = []
        self.fill_area() # fill the area with asterisks
        Region._regions[(x, y)] = self
    
    def fill_area(self):
        for i in range(50):
            self.area.append([])
            for j in range(50):
                self.area[i].append('*')

    def print_region(self):
        # print each row of the region
        for i in self.area:
            print(' '.join(j for j in i))


    @classmethod
    def get_regions(self):
        # print all of the attributes of each region 
        for i in Region._regions:
            print(Region._regions[i].__name__)


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

    newWeapon3 = Weapon('Gun', 15)

    Weapon.getList() # print a list of all weapons

    newRegion = Region(1, 1)

    newRegion.print_region()

    Region.get_regions()
    



main()