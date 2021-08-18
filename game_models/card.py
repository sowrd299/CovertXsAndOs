from util.vector2 import *
from util.writer import side_by_side

class Card():

	revealed = True
	friendly = True

	ability_text = ""
	label = ""

	full_ability_text = ""

	''' # NOTE: OLD VERSION, DOES NOTHING
	str_format = "/{defTop}{atkTop}{defTop}\\\n"
	str_format += "{defLeft}{cost}  {defRight}\n"
	str_format += "{atkLeft} {symbol} {atkRight}\n"
	str_format += "{defLeft}{label:<3}{defRight}\n"
	str_format += "\\{defBottom}{atkBottom}{defBottom}/"
	'''

	str_format = "╭{defTop}{atkTop}{defTop}╮\n"
	str_format += "{defLeft}{ability_text:<3}{defRight}\n"
	str_format += "{atkLeft} {symbol} {atkRight}\n"
	str_format += "{defLeft}{label:<3}{defRight}\n"
	str_format += "╰{defBottom}{atkBottom}{defBottom}╯"

	def __init__(self, name = "", cost = 0, symbol = " ", atk_sides = [], def_sides = []):
		self.name = name
		self.cost = cost
		self.symbol = symbol
		self.atk_sides = list(atk_sides)
		self.def_sides = list(def_sides)


	def __str__(self):

		details = {
			"symbol" : self.symbol,
			"cost" : self.cost if self.cost else " ",
			"defLeft" : "╫" if Vector2(-1,0) in self.def_sides else "│",
			"defRight" : "╫" if Vector2(1,0) in self.def_sides else "│",
			"defTop" : "╪" if Vector2(0,-1) in self.def_sides else "─",
			"defBottom" : "╪" if Vector2(0,1) in self.def_sides else "─",
			"atkLeft" : "☚" if Vector2(-1,0) in self.atk_sides else " ",
			"atkRight" : "☛" if Vector2(1,0) in self.atk_sides else " ",
			"atkTop" : "♠" if Vector2(0,-1) in self.atk_sides else " ",
			"atkBottom" : "↓" if Vector2(0,1) in self.atk_sides else " ",
			"ability_text" : self.ability_text,
			"label" : self.label
		}

		return self.str_format.format(**details)

	def get_info(self):
		'''
		Returns a longer, more written out representation of the card
		'''
		info = self.name + "\n"
		info += self.symbol + ": " + self.symbol.name
		if self.ability_text:
			info += "\n" + self.ability_text + ": " + self.full_ability_text
		return side_by_side(self, info)


	def invert(self):
		'''
		Returns a version of the card with all edges rotated 180 degrees
		'''
		return type(self)(self.name, self.cost, self.symbol, map(Vector2.invert, self.atk_sides), map(Vector2.invert, self.def_sides))


	def get_secret_card(self):
		'''
		Returns the secret card that goes on the opponent's board
		'''
		return SecretCard(self.cost)



class SecretCard(Card):
	'''
	Represents a card face-down that was played by an enemy
	'''

	revealed = False
	friendly = False

	str_format = "╭-?-╮\n"
	str_format += "|( )|\n"
	str_format += "?({cost})?\n"
	str_format += "|( )|\n"
	str_format += "╰─?─╯"

	def __init__(self, cost):
		super().__init__("", cost, "", [], [UP, DOWN, LEFT, RIGHT])