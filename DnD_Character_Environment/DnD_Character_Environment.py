##############################################
##############################################
##											##
##			Dungeons & Dragons				##
##		Player's Character Environment		##
##					v0.1					##
##											##
##############################################
##############################################


## Plans for v0.1
## 
##	- Character creator
## 		- Random
##		- Custom
##
##	- Combat
##		- Turn order
##	- Inventory
##	- Equipment
##	- Encounters
##	- Leveling
##		- Paragon Path at level 11
##		- Epic Destiny
##	- Keep track of AP
##
##	- Sleeping
##		- Refill health/ap
##
##	- Saving
##	- Loading

from random import randint

char = {
"Level" : 1,
"Experience" : 0
}

races = ['deva', 'dragonborn', 'drow', 'dwarf', 'eladrin', 'elf', 'genasi', 'githzerai', 'gnoll', 'gnome', 'goblin', 'goliath', 'half-elf', 'half-orc', 'halfling', 'hamadryad', 'human', 'kalashtar', 'shifter', 'minotaur', 'mul', 'pixie', 'revenant', 'satyr', 'shadar-kai', 'shade', 'shardmind', 'thri-kreen', 'tiefling', 'vryloka', 'warforged', 'wilden']
classes = ['ardent', 'avenger', 'barbarian', 'bard', 'battlemind', 'cleric', 'druid', 'fighter', 'invoker', 'monk', 'paladin', 'psion', 'ranger', 'rogue', 'runepriest', 'seeker', 'shaman', 'sorcerer', 'warden', 'warlock', 'warlord', 'wizard']

def help():
	print "Welcome to the D&D Player\'s Character Environment v0.1"
	print "Now go dungeoneering!"


def d(sides, throws = 1, advantage = 0):
	result = []
	if advantage == 0:	
		for i in range(throws):
			result.append(randint(1, sides))
	else:
		for i in range(throws + abs(advantage)):
			result.append(randint(1, sides))
		if advantage > 0:
			for i in range (advantage):
				result.remove(min(result))
		elif advantage < 0:
			for i in range (abs(advantage)):
				result.remove(max(result))
	return result

def new_char_input():
	## These choices are cosmetic and will not change anything later on
	char["Gender"] = raw_input("Are you male or female? ")
	char["Name"] = raw_input("What is your name? ")
	char["Race"] = raw_input("You are the representative of which race? ")
	while char["Race"].lower() not in races:
		print "Not a valid race."
		char["Race"] = raw_input("You are the representative of which race? ")
	char["Age"] = raw_input("How old are you? ")
	char["Height"] = raw_input("How tall are you? ")
	char["Weight"] = raw_input("How fat are you? ")

	## These choices should be limited and have impact on other things
	char["Class"] = raw_input("Please enter your class. ")
	while char["Class"].lower() not in classes:
		print "Not a valid class."
		char["Class"] = raw_input("Please enter your class. ")
	char["Alignment"] = raw_input("Please enter your alignment. ")
	char["Deity"] = raw_input("Who is your deity? ")

def new_char_atr():
	user_creation_choice = raw_input("random? (y/n) ")
	if user_creation_choice.lower() == "y" or user_creation_choice.lower() == "yes":
		char["Strength"] = sum(d(6, 3, 1))
		char["Constitution"] = sum(d(6, 3, 1))
		char["Dexterity"] = sum(d(6, 3, 1))
		char["Intelligence"] = sum(d(6, 3, 1))
		char["Wisdom"] = sum(d(6, 3, 1))
		char["Charisma"] = sum(d(6, 3, 1))
		print "You rolled the following stats: \nStr: %s Con: %s Dex: %s Int: %s Wis: %s Char: %s" %(char["Strength"], char["Constitution"], char["Dexterity"], char["Intelligence"], char["Wisdom"], char["Charisma"])
	elif user_creation_choice.lower() == "n" or user_creation_choice.lower() == "no":
		print "not done yet"
		"""
		The second method is a little more complicated. Start with the following scores: 8, 10, 10, 10, 10, and 10. You have 22 "points" to spend in order to increase the ability scores. Use the following rules to spend these points and improve your ability scores, then assign the score to the specific abilities.
		Improving the numbers 8-12 costs one point. As such, increasing the "8" to a "12" would cost 4 points. Improving a "10" to a "13" would cost only 3: one point each for 10-to-11, 11-to-12, and 12-to-13.
		Improving the numbers 13-15 costs two points. As such, increasing the "12" from before would cost another point to become a "13", but an additional two points to improve to a "14". Similarly, improving the "13" to a "16" would cost 6 points: two each for 13-to-14, 14-to-15, and 15-to-16.
		Improving a "16" to a "17" costs another three points.
		Improving a "17" to an "18" costs another four points. As a result, upgrading a "10" to an "18" would cost a total of 16 points = 3*1 + 3*2 + 3 + 4.
		"""
	else:
		print "Sorry, I don't understand."
		new_char_atr()

"""

Future structure for inventory

class ShoppingCart(object):
    """Creates shopping cart objects
    for users of our fine website."""
    items_in_cart = {}
    def __init__(self, customer_name):
        self.customer_name = customer_name

    def add_item(self, product, price):
        """Add product to the cart."""
        if not product in self.items_in_cart:
            self.items_in_cart[product] = price
            print product + " added."
        else:
            print product + " is already in the cart."

    def remove_item(self, product):
        """Remove product from the cart."""
        if product in self.items_in_cart:
            del self.items_in_cart[product]
            print product + " removed."
        else:
            print product + " is not in the cart."

"""
		

##	Strength represents physical power.
##	Constitution represents health and stamina.
##	Dexterity represents agility and reflexes.
##	Intelligence represents reasoning.
##	Wisdom represents common sense.
##	Charisma represents personality.


"""

Future plans:

- Menu
- Online capability
- Multiple characters
- UI


"""

## By Versace_Python
