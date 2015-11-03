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
import pickle

gamestate = "continue"

class Characters(object):
	
	def __init__(self, exp, gender, name, race, age, height, weight, char_class, alignment, deity, str=0, con=0, dex=0, int=0, wis=0, char=0):
		self.exp = exp
		self.gender = gender
		self.name = name
		self.race = race
		self.age = age
		self.height = height
		self.weight = weight
		self.char_class = char_class
		self.alignment = alignment
		self.deity = deity
		self.str = str
		self.con = con
		self.dex = dex
		self.int = int
		self.wis = wis
		self.char = char
	
	
	def level(self):
		if self.exp < 1000:
			return 1
		elif self.exp < 2250:
			return 2
		elif self.exp < 3750:
			return 3
		elif self.exp < 5500:
			return 4
		elif self.exp < 7500:
			return 5
		elif self.exp < 10000:
			return 6
		elif self.exp < 13000:
			return 7
		elif self.exp < 16500:
			return 8
		elif self.exp < 20500:
			return 9
		elif self.exp < 26000:
			return 10
		elif self.exp < 32000:
			return 11
		elif self.exp < 39000:
			return 12
		elif self.exp < 47000:
			return 13
		elif self.exp < 57000:
			return 14
		elif self.exp < 69000:
			return 15
		elif self.exp < 83000:
			return 16
		elif self.exp < 99000:
			return 17
		elif self.exp < 119000:
			return 18
		elif self.exp < 143000:
			return 19
		elif self.exp < 175000:
			return 20
		elif self.exp < 210000:
			return 21
		elif self.exp < 255000:
			return 22
		elif self.exp < 310000:
			return 23
		elif self.exp < 375000:
			return 24
		elif self.exp < 450000:
			return 25
		elif self.exp < 550000:
			return 26
		elif self.exp < 675000:
			return 27
		elif self.exp < 825000:
			return 28
		elif self.exp < 1000000:
			return 29
		else:
			return 30



races = ['deva', 'dragonborn', 'drow', 'dwarf', 'eladrin', 'elf', 'genasi', 'githzerai', 'gnoll', 'gnome', 'goblin', 'goliath', 'half-elf', 'half-orc', 'halfling', 'hamadryad', 'human', 'kalashtar', 'shifter', 'minotaur', 'mul', 'pixie', 'revenant', 'satyr', 'shadar-kai', 'shade', 'shardmind', 'thri-kreen', 'tiefling', 'vryloka', 'warforged', 'wilden']
classes = ['ardent', 'avenger', 'barbarian', 'bard', 'battlemind', 'cleric', 'druid', 'fighter', 'invoker', 'monk', 'paladin', 'psion', 'ranger', 'rogue', 'runepriest', 'seeker', 'shaman', 'sorcerer', 'warden', 'warlock', 'warlord', 'wizard']

def help():
	print "Welcome to the D&D Player\'s Character Environment v0.1"
	print "Now go dungeoneering!"

def save():
	#save_text = "%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s %s" %(char.exp, char.gender, char.name, char.race, char.age, char.height, char.weight, char.char_class, char.alignment, char.deity, char.str, char.con, char.dex, char.int, char.wis, char.char)
	#with open("character.txt", "w") as save_file:
	#	save_file.write(save_text)
	#if not save_file.closed:
	#	save_file.close()
	#	print "file closed"
	file = open("save", "w")
	pickle.dump(char, file)
	file.close

def load():
	global char
	load_file = open("save", "r")
	char = pickle.load(load_file)
	load_file.close()

def exit():
	global gamestate
	gamestate = "quit"
	
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
	global char
	char = Characters(
		0,
		raw_input("Are you male or female? "),
		raw_input("What is your name? "),
		raw_input("You are the representative of which race? "),
		int(raw_input("How old are you? ")),
		int(raw_input("How tall are you? ")),
		int(raw_input("How fat are you? ")),
		raw_input("Please enter your class. "),
		raw_input("Please enter your alignment. "),
		raw_input("Who is your deity? ")
	)

	
"""

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


"""	
	
def new_char_atr():
	user_creation_choice = raw_input("random? (y/n) ")
	if user_creation_choice.lower() == "y" or user_creation_choice.lower() == "yes":
		char.str = sum(d(6, 3, 1))
		char.con = sum(d(6, 3, 1))
		char.dex = sum(d(6, 3, 1))
		char.int = sum(d(6, 3, 1))
		char.wis = sum(d(6, 3, 1))
		char.char = sum(d(6, 3, 1))
		print "You rolled the following stats: \nStr: %s Con: %s Dex: %s Int: %s Wis: %s Char: %s" %(char.str, char.con, char.dex, char.int, char.wis, char.char)
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

		
def interface():
	choice = raw_input("What do you want to do? \nnew \ndice \nsee character \nsave \nload \nexit \n")
	if choice == "new":
		new_char_input()
		new_char_atr()
	elif choice == "dice":
		side = int(raw_input("How many sides does the dice have? "))
		throws = int(raw_input("How many throws do you want to make? "))
		advantage = int(raw_input("What is your advantage? "))
		print d(side, throws, advantage)
	elif choice == "see character":
		if "char" in globals():
			print char.exp
			print char.gender
			print char.name
			print char.race
			print char.age
			print char.height
			print char.weight
			print char.char_class
			print char.alignment
			print char.deity
			print char.str
			print char.con
			print char.dex
			print char.int
			print char.wis
			print char.char
		else:
			print "No character available"
	elif choice == "save":
		save()
	elif choice == "load":
		load()
	elif choice == "exit":
		exit()
		
while gamestate == "continue":
	interface()
		
"""

Future structure for inventory

class Inventory(object):
    items_in_inventory = {}
    def __init__(self, char_name):
        self.char_name = char_name

    def add_item(self, item, amount):
		self.items_in_inventory[item] += amount
		print product + " added."

    def remove_item(self, item, amount):
        if item in self.items_in_inventory and self.items_in_inventory[item] > 0:
            self.items_in_inventory[item] += -amount
            print "%s %s removed." %(amount, item)
        else:
            print item + " is not in the inventory."

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
