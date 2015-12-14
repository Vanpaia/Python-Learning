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
	
	def __init__(self, exp, gender, name, race, age, height, weight, char_class, alignment, deity, str=10, con=10, dex=10, int=10, wis=10, char=10, acrobatics = 0, arcana = 0, athletics = 0, bluff = 0, diplomacy = 0, dungeoneering = 0, endurance = 0, heal = 0, history = 0, insight = 0, intimidate = 0, nature = 0, perception = 0, religion = 0, stealth = 0, streetwise = 0, thievery = 0, speed = 0):
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
		
		self.acrobatics = acrobatics
		self.arcana = arcana
		self.athletics = athletics
		self.bluff = bluff
		self.diplomacy = diplomacy
		self.dungeoneering = dungeoneering
		self.endurance = endurance
		self.heal = heal
		self.history = history
		self.insight = insight
		self.intimidate = intimidate
		self.nature = nature
		self.perception = perception
		self.religion = religion
		self.stealth = stealth
		self.streetwise = streetwise
		self.thievery = thievery

		self.speed = speed
	
	
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

			
class Race(object):
	def __init__(self, name, max_h, min_h, max_w, min_w, size, speed, vision, languages, as1, as2, sb1, sb2):
		self.name = name
		self.max_h = max_h
		self.min_h = min_h
		self.max_w = max_w
		self.min_w = min_w
		self.size = size
		self.speed = speed
		self.vision = vision
		self.languages = languages
		self.as1 = as1
		self.as2 = as2
		self.sb1 = sb1
		self.sb2 = sb2
	def ability_scores(self):
		if self.as1 == "str" or self.as2 == "str" :
			char.str += 2
		if self.as1 == "con" or self.as2 == "con":
			char.con += 2
		if self.as1 == "dex" or self.as2 == "dex":
			char.dex += 2
		if self.as1 == "int" or self.as2 == "int":
			char.int += 2
		if self.as1 == "wis" or self.as2 == "wis":
			char.wis += 2
		if self.as1 == "char" or self.as2 == "char":
			char.char += 2
		if self.as1 == "choice":
			print "Your Ability Score lets you choose an ability you want to improve by two"
			improve = str(raw_input("What attribute do you want to improve? \n(str, con, dex, int, wis, char) "))
			while improve not in attributes:
				print "not a valid attribute"
				improve = raw_input("What attribute do you want to improve? \n(str, con, dex, int, wis, char) ")
			if improve.lower() == "str":
				char.str += 2
			elif improve.lower() == "con":
				char.con += 2
			elif improve.lower() == "dex":
				char.dex += 2
			elif improve.lower() == "int":
				char.int += 2
			elif improve.lower() == "wis":
				char.wis += 2
			elif improve.lower() == "char":
				char.char += 2
		if self.as2 == "choice":
			print "Your Ability Score lets you choose another ability you want to improve by two"
			improve = str(raw_input("What attribute do you want to improve? \n(str, con, dex, int, wis, char) "))
			while improve not in attributes:
				print "not a valid attribute"
				improve = raw_input("What attribute do you want to improve? \n(str, con, dex, int, wis, char) ")
			if improve.lower() == "str":
				char.str += 2
			elif improve.lower() == "con":
				char.con += 2
			elif improve.lower() == "dex":
				char.dex += 2
			elif improve.lower() == "int":
				char.int += 2
			elif improve.lower() == "wis":
				char.wis += 2
			elif improve.lower() == "char":
				char.char += 2

class CharacterClasses(object):
	
	def __init__(self, name, role, powersource, keyabilities, armorproficiency, weaponproficiency, implement, defensebonus, hitpoints, healingsurges, trainedskills):
		self.name = name
		self.role = role
		self.powersource = powersource
		self.keyabilities = keyabilities
		self.armorproficiency = armorproficiency
		self.weaponproficiency = weaponproficiency
		self.implement = implement
		self.defensebonus = defensebonus
		self.hitpoints = hitpoints
		self.healingsurges = healingsurges
		self.trainedskills = trainedskills

dragonborn = Race("Dragonborn", 203, 188, 145, 100, "medium", 6, "normal", ["common", "draconic"], "str", "char", "history", "intimidate")
dwarf = Race("Dwarf", 145, 130, 100, 73, "medium", 5, "low-light", ["common", "dwarven"], "con", "wis", "dungeoneering", "endurance")
eladrin = Race("Eldarin", 185, 165, 82, 59, "medium", 6, "low-light", ["common", "elven"], "dex", "int", "arcana", "history")
elf = Race("Elf", 183, 163, 77, 59, "medium", 7, "low-light", ["common", "elven"], "dex", "wis", "nature", "perception")
halfelf = Race("Half-Elf", 188, 165, 86, 59, "medium", 6, "low-light", ["common", "elven"], "con", "char", "diplomacy", "insight")
halfling = Race("Halfling", 127, 117, 39, 34, "small", 6, "normal", ["common"], "dex", "char", "acrobatics", "thievery")
human = Race("Human", 188, 168, 61, 100, "medium", 6, "normal", ["common"], "choice", "choice", "training", "nothing")
tiefling = Race("Tiefling",188, 168, 104, 64, "medium", 6, "low-light", ["common"], "int", "char", "bluff", "stealth")

cleric = CharacterClasses("Cleric", "Leader", "Divine", ["wis", "str", "char"], ["cloth", "leather", "hide", "chainmail"], ["simple melee", "simple ranged"], "Holy symbol", "will", [12, "con"], [7, "con"], {1:"religion", 2:["arcana", "diplomacy", "heal", "history", "insight", "religion"]} )

skills = ["acrobatics", "arcana", "athletics", "bluff", "diplomacy", "dungeoneering", "endurance", "heal", "history", "insight", "intimidate", "nature", "perception", "religion", "stealth", "streetwise", "thievery"]
races = ['deva', 'dragonborn', 'drow', 'dwarf', 'eladrin', 'elf', 'genasi', 'githzerai', 'gnoll', 'gnome', 'goblin', 'goliath', 'half-elf', 'half-orc', 'halfling', 'hamadryad', 'human', 'kalashtar', 'shifter', 'minotaur', 'mul', 'pixie', 'revenant', 'satyr', 'shadar-kai', 'shade', 'shardmind', 'thri-kreen', 'tiefling', 'vryloka', 'warforged', 'wilden']
classes = ['ardent', 'avenger', 'barbarian', 'bard', 'battlemind', 'cleric', 'druid', 'fighter', 'invoker', 'monk', 'paladin', 'psion', 'ranger', 'rogue', 'runepriest', 'seeker', 'shaman', 'sorcerer', 'warden', 'warlock', 'warlord', 'wizard']
attributes = ["str", "con", "dex", "int", "wis", "char"]

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
	
	while True:
		new_sex = raw_input("Are you male or female? ").capitalize()
		if new_sex == "Male" or new_sex == "Female":
			break
		print "We are not that progressive..."
	new_name = raw_input("What is your name? ").capitalize()
	new_race = raw_input("You are the representative of which race? ").lower()
	while new_race not in races:
		print "Not a valid race."
		new_race = raw_input("You are the representative of which race? ").lower()
	if new_race == "dragonborn":
		new_race = dragonborn
	elif new_race == "dwarf":
		new_race = dwarf
	elif new_race == "eladrin":
		new_race = eladrin
	elif new_race == "elf":
		new_race = elf
	elif new_race == "half-elf":
		new_race = halfelf
	elif new_race == "halfling":
		new_race = halfling
	elif new_race == "human":
		new_race = human
	elif new_race == "tiefling":
		new_race = tiefling
	new_age = int(raw_input("How old are you? "))
	while (new_age <= 0):
		print "That would mean you don't exist..."
		new_age = int(raw_input("How old are you? "))
	new_h = int(raw_input("How tall are you? "))
	while (new_h <= 0):
		print "You want me to believe that?"
		new_h = int(raw_input("How tall are you? "))
	new_w = int(raw_input("How fat are you? "))
	while (new_w <= 0):
		print "That'd be an unbelieveable diet..."
		new_w = int(raw_input("How fat are you? "))
	new_class = raw_input("What is your class? ")
	new_allignment = raw_input("What is your alignment? ")
	new_deity = raw_input("Who is your deity? ")
	
	char = Characters(0, new_sex, new_name, new_race, new_age, new_h, new_w, new_class, new_allignment, new_deity)
	char.size = char.race.size
	char.speed = char.race.speed
	char.vision = char.race.vision
	char.languages = char.race.languages
	
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
		print "Your race changes this to: \nStr: %s Con: %s Dex: %s Int: %s Wis: %s Char: %s" %(char.str, char.con, char.dex, char.int, char.wis, char.char)
		
	elif user_creation_choice.lower() == "n" or user_creation_choice.lower() == "no":
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
		char.race.ability_scores()
		print "Your race changes this to: \nStr: %s Con: %s Dex: %s Int: %s Wis: %s Char: %s" %(char.str, char.con, char.dex, char.int, char.wis, char.char)
		
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
			print "\nD&D    Character Sheet    D&D\n-----------------------------\nNAME:       %s\nEXP:        %s\nLEVEL:      %s\nGENDER:     %s\nRACE:       %s\nAGE:        %s\nHEIGHT:     %s\nWEIGHT:     %s\nCLASS:      %s\nALIGNMENT:  %s\nDEITY:      %s\n-----------------------------\nSTR:        %s\nCON:        %s\nDEX:        %s\nINT:        %s\nWIS:        %s\nCHAR:       %s\n-----------------------------\nSIZE:       %s\nSPEED:      %s\nVISION:     %s\nLANGUAGES:  %s\n \n" %(char.name, char.exp, char.level(), char.gender, char.race.name, char.age, char.height, char.weight, char.char_class, char.alignment, char.deity, char.str, char.con, char.dex, char.int, char.wis, char.char, char.size, char.speed, char.vision, char.languages)
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
		

"""

Future plans:

- Menu
- Multiple characters
- UI


"""

## By Versace_Python
