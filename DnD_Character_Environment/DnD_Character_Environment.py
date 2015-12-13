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
##	- Character creator						x
## 		- Random							x
##		- Custom							x
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
##	- Saving								x
##	- Loading								x

from random import randint
import pickle

gamestate = "continue"

class Characters(object):
	
	def __init__(self, exp, gender, name, race, age, height, weight, char_class, alignment, deity, str=10, con=10, dex=10, int=10, wis=10, char=10):
		self.exp = exp
		self.gender = gender
		self.name = name
		self.race = Dragonborn()
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


class Dragonborn(object):
	def __init__(self):
		self.name = "Dragonborn"
		self.max_h = 203
		self.min_h = 188
		self.max_w = 145
		self.min_w = 100
	def ability_scores(self):
		char.str = char.str +2
		char.char = char.char +2
	def test(self):
		return "succes"
			
races = ['deva', 'dragonborn', 'drow', 'dwarf', 'eladrin', 'elf', 'genasi', 'githzerai', 'gnoll', 'gnome', 'goblin', 'goliath', 'half-elf', 'half-orc', 'halfling', 'hamadryad', 'human', 'kalashtar', 'shifter', 'minotaur', 'mul', 'pixie', 'revenant', 'satyr', 'shadar-kai', 'shade', 'shardmind', 'thri-kreen', 'tiefling', 'vryloka', 'warforged', 'wilden']
classes = ['ardent', 'avenger', 'barbarian', 'bard', 'battlemind', 'cleric', 'druid', 'fighter', 'invoker', 'monk', 'paladin', 'psion', 'ranger', 'rogue', 'runepriest', 'seeker', 'shaman', 'sorcerer', 'warden', 'warlock', 'warlord', 'wizard']

def help():
	print "Welcome to the D&D Player\'s Character Environment v0.1"
	print "Now go dungeoneering!"

def save():
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
		raw_input("What is your class? "),
		raw_input("What is your alignment? "),
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
	user_creation_choice = raw_input("random attributes? (y/n) ")
	if user_creation_choice.lower() == "y" or user_creation_choice.lower() == "yes":
		char.str = sum(d(6, 3, 1))
		char.con = sum(d(6, 3, 1))
		char.dex = sum(d(6, 3, 1))
		char.int = sum(d(6, 3, 1))
		char.wis = sum(d(6, 3, 1))
		char.char = sum(d(6, 3, 1))
		print "You rolled the following stats: \nStr: %s Con: %s Dex: %s Int: %s Wis: %s Char: %s" %(char.str, char.con, char.dex, char.int, char.wis, char.char)
		char.race.ability_scores()
		print "You rolled the following stats: \nStr: %s Con: %s Dex: %s Int: %s Wis: %s Char: %s" %(char.str, char.con, char.dex, char.int, char.wis, char.char)
		
	elif user_creation_choice.lower() == "n" or user_creation_choice.lower() == "no":
		attributes = ["str", "con", "dex", "int", "wis", "char"]
		attribute_cost = {10:0, 11:1, 12:2, 13:3, 14:5, 15:7, 16:9, 17:12, 18:16}
		attribute_cost_weakness = {8:0, 9:1, 10:2, 11:3, 12:4, 13:5, 14:7, 15:9, 16:11, 17:14, 18:18}
		points_left = 22
		print ""
		weakpoint = str(raw_input("What attribute is your weakpoint? \n(str, con, dex, int, wis, char) "))
		while weakpoint not in attributes:
			print "not a valid attribute"
			weakpoint = raw_input("What attribute is your weakpoint? \n(str, con, dex, int, wis, char) ")
		if weakpoint.lower() == "str":
			char.str = 8
		elif weakpoint.lower() == "con":
			char.con = 8
		elif weakpoint.lower() == "dex":
			char.dex = 8
		elif weakpoint.lower() == "int":
			char.int = 8
		elif weakpoint.lower() == "wis":
			char.wis = 8
		elif weakpoint.lower() == "char":
			char.char = 8
		print ""
		print "You start with the following stats: \nStr: %s Con: %s Dex: %s Int: %s Wis: %s Char: %s" %(char.str, char.con, char.dex, char.int, char.wis, char.char)
		print ""	
		print "You have %s points left" %(points_left)
		print "The cost of improving scales up as follows: \nScore   Cost \n9       -(1) \n10      0(2) \n11      1 \n12      2 \n13      3 \n14      5 \n15      7 \n16      9 \n17      12 \n18      16"
		choice_str = int(raw_input("What should your strength be? "))
		if weakpoint.lower() == "str":
			while choice_str > 18 or choice_str < 8:
				print "Try a different score"
				choice_str = int(raw_input("What should your strength be? "))
			while attribute_cost_weakness[choice_str] > points_left:
				print "Not enough points left."
				choice_str = int(raw_input("What should your strength be? "))
			points_left = points_left - attribute_cost_weakness[choice_str]
		else:
			while choice_str > 18 or choice_str < 10:
				print "Try a different score"
				choice_str = int(raw_input("What should your strength be? "))
			while attribute_cost[choice_str] > points_left:
				print "Not enough points left."
				choice_str = int(raw_input("What should your strength be? "))
			points_left = points_left - attribute_cost[choice_str]
		
		print ""
		print "You have %s points left" %(points_left)
		
		choice_con = int(raw_input("What should your constitution be? "))
		if weakpoint.lower() == "con":
			print "This is your weakness, you start at 8 points."
			while choice_con > 18 or choice_con <8:
				print "Try a different score"
				choice_con = int(raw_input("What should your constitution be? "))
			while attribute_cost_weakness[choice_con] > points_left:
				print "Not enough points left."
				choice_con = int(raw_input("What should your constitution be? "))
			points_left = points_left - attribute_cost_weakness[choice_con]
		else:
			while choice_con > 18 or choice_con <10:
				print "Try a different score"
				choice_con = int(raw_input("What should your constitution be? "))
			while attribute_cost[choice_con] > points_left:
				print "Not enough points left."
				choice_con = int(raw_input("What should your constitution be? "))
			points_left = points_left - attribute_cost[choice_con]
		
		print ""
		print "You have %s points left" %(points_left)
		
		choice_dex = int(raw_input("What should your dexterity be? "))
		if weakpoint.lower() == "dex":
			print "This is your weakness, you start at 8 points."
			while choice_dex > 18 or choice_dex <8:
				print "Try a different score"
				choice_dex = int(raw_input("What should your dexterity be? "))
			while attribute_cost_weakness[choice_dex] > points_left:
				print "Not enough points left."
				choice_dex = int(raw_input("What should your dexterity be? "))
			points_left = points_left - attribute_cost_weakness[choice_dex]
		else:
			while choice_dex > 18 or choice_dex <10:
				print "Try a different score"
				choice_dex = int(raw_input("What should your dexterity be? "))
			while attribute_cost[choice_dex] > points_left:
				print "Not enough points left."
				choice_dex = int(raw_input("What should your dexterity be? "))
			points_left = points_left - attribute_cost[choice_dex]
		
		print ""
		print "You have %s points left" %(points_left)
		
		choice_int = int(raw_input("What should your intelligence be? "))
		if weakpoint.lower() == "int":
			print "This is your weakness, you start at 8 points."
			while choice_int > 18 or choice_int <8:
				print "Try a different score"
				choice_int = int(raw_input("What should your intelligence be? "))
			while attribute_cost_weakness[choice_int] > points_left:
				print "Not enough points left."
				choice_int = int(raw_input("What should your intelligence be? "))
			points_left = points_left - attribute_cost_weakness[choice_int]
		else:
			while choice_int > 18 or choice_int <10:
				print "Try a different score"
				choice_int = int(raw_input("What should your intelligence be? "))
			while attribute_cost[choice_int] > points_left:
				print "Not enough points left."
				choice_int = int(raw_input("What should your intelligence be? "))
			points_left = points_left - attribute_cost[choice_int]
		
		print ""
		print "You have %s points left" %(points_left)
		
		choice_wis = int(raw_input("What should your wisdom be? "))
		if weakpoint.lower() == "wis":
			print "This is your weakness, you start at 8 points."
			while choice_wis > 18 or choice_wis <8:
				print "Try a different score"
				choice_wis = int(raw_input("What should your wisdom be? "))
			while attribute_cost_weakness[choice_wis] > points_left:
				print "Not enough points left."
				choice_wis = int(raw_input("What should your wisdom be? "))
			points_left = points_left - attribute_cost_weakness[choice_wis]
		else:
			while choice_wis > 18 or choice_wis <10:
				print "Try a different score"
				choice_wis = int(raw_input("What should your wisdom be? "))
			while attribute_cost[choice_wis] > points_left:
				print "Not enough points left."
				choice_wis = int(raw_input("What should your wisdom be? "))
			points_left = points_left - attribute_cost[choice_wis]
		
		print ""
		print "You have %s points left" %(points_left)
		
		choice_char = int(raw_input("What should your charisma be? "))
		if weakpoint.lower() == "char":
			print "This is your weakness, you start at 8 points."
			while choice_char > 18 or choice_char <8:
				print "Try a different score"
				choice_char = int(raw_input("What should your charisma be? "))
			while attribute_cost_weakness[choice_char] > points_left:
				print "Not enough points left."
				choice_char = int(raw_input("What should your charisma be? "))
			points_left = points_left - attribute_cost_weakness[choice_char]
		else:
			while choice_char > 18 or choice_char <10:
				print "Try a different score"
				choice_char = int(raw_input("What should your charisma be? "))
			while attribute_cost[choice_char] > points_left:
				print "Not enough points left."
				choice_char = int(raw_input("What should your charisma be? "))
			points_left = points_left - attribute_cost[choice_char]
		
		char.str = choice_str
		char.con = choice_con
		char.dex = choice_dex
		char.int = choice_int
		char.wis = choice_wis
		char.char = choice_char
		
		print ""
		print "You now have the following stats: \nStr: %s Con: %s Dex: %s Int: %s Wis: %s Char: %s" %(char.str, char.con, char.dex, char.int, char.wis, char.char)
		print ""
		user_confirmation = raw_input("Are you happy with your stats? (y/n) ")
		if user_confirmation.lower() == "n" or user_confirmation.lower() == "no":
			new_char_atr()
	else:
		print "Sorry, I don't understand."
		new_char_atr()

		
def interface():
	choice = raw_input("\n|---------------|\n|      NEW      |\n|---------------|\n|     DICE      |\n|---------------|\n| SEE CHARACTER |\n|---------------|\n|     SAVE      |\n|---------------|\n|     LOAD      |\n|---------------|\n|     EXIT      |\n|---------------|\n \n")
	if choice == "new":
		new_char_input()
		new_char_atr()
	elif choice == "dice":
		side = int(raw_input("How many sides does the dice have? "))
		throws = int(raw_input("How many throws do you want to make? "))
		advantage = int(raw_input("What is your advantage? "))
		print d(side, throws, advantage)
		print ""
		raw_input("")
	elif choice == "see character":
		if "char" in globals():
			print "\nD&D    Character Sheet    D&D\n-----------------------------\nNAME:       %s\nEXP:        %s\nLEVEL:      %s\nGENDER:     %s\nRACE:       %s\nAGE:        %s\nHEIGHT:     %s\nWEIGHT:     %s\nCLASS:      %s\nALIGNMENT:  %s\nDEITY:      %s\n-----------------------------\nSTR:        %s\nCON:        %s\nDEX:        %s\nINT:        %s\nWIS:        %s\nCHAR:       %s\n \n" %(char.name, char.exp, char.level(), char.gender, char.race.name, char.age, char.height, char.weight, char.char_class, char.alignment, char.deity, char.str, char.con, char.dex, char.int, char.wis, char.char)
			raw_input("")
		else:
			print "No character available"
			raw_input("")
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
