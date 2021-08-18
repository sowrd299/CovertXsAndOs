from game_models.board import Board
from random import shuffle

class Player():
	'''
	Represents a player in the game
	Used to configure who will be playing the game and how
	'''

	hand_size = 3

	def __init__(self, deck = [], board = None):
		self.board = board or Board(3,3)
		self.deck = deck
		self.hand = []


	def shuffle(self):
		shuffle(self.deck)


	def draw_hand(self):
		'''
		Draw's the players full starting hand
		'''
		for i in range(self.hand_size):
			self.draw()


	def draw(self):
		if len(self.deck) > 0:
			self.hand.append(self.deck.pop())


	def play(self, card):
		'''
		Plays the card out of the player's hand
		'''
		self.hand.remove(card)


