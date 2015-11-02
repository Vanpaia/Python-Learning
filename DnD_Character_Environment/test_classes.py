from random import randint

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

class Characters(object):
	
	def __init__(self, name, race, exp, attributes = {}):
		self.name = name
		self.race = race
		self.exp = exp
		self.attributes = attributes
	
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
				


	
hagen = Characters("Hagen", "Human", 352909)

print hagen.level()

def new_char_atr():
	user_creation_choice = raw_input("random? (y/n) ")
 	if user_creation_choice.lower() == "y" or user_creation_choice.lower() == "yes":
		temp_atr= {}
		temp_atr["Strength"] = sum(d(6, 3, 1))
		temp_atr["Constitution"] = sum(d(6, 3, 1))
		temp_atr["Dexterity"] = sum(d(6, 3, 1))
		temp_atr["Intelligence"] = sum(d(6, 3, 1))
		temp_atr["Wisdom"] = sum(d(6, 3, 1))
		temp_atr["Charisma"] = sum(d(6, 3, 1))
		hagen.attributes = temp_atr
		print "You rolled the following stats: \nStr: %s Con: %s Dex: %s Int: %s Wis: %s Char: %s" %(temp_atr["Strength"], temp_atr["Constitution"], temp_atr["Dexterity"], temp_atr["Intelligence"], temp_atr["Wisdom"], temp_atr["Charisma"])
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