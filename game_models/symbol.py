class Symbol():
	'''
	Represents the factions symbol on a card
	'''

	def __init__(self, symbol, name):
		self.symbol = symbol
		self.name = name

	def __str__(self):
		return self.symbol

	def __add__ (self, other):
		return str(self) + other

	def __radd__(self, other):
		return other + str(self)
