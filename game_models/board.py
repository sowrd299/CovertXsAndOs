from util.vector2 import Vector2
from util.writer import side_by_side
from .enemy_card import EnemyCard

class Board():

	str_blank_format = ((" " * 5) + "\n") * 2
	str_blank_format = str_blank_format + (" "*2) + "{letter}" + (" " * 2) + "\n" + str_blank_format

	def __init__(self, width, height):
		self.board = [ ([None] * width) for i in range(height) ]
		self.size = Vector2(width, height)

	def string(self, letters = None):
		letters = letters or [(["+"] * len(self.board[0]))] * len(self.board)
		text = ""
		first = True
		for i,row in enumerate(self.board):
			row_text = ""
			for j,card in enumerate(row):
				row_text = side_by_side(row_text, str(card) if card else self.str_blank_format.format(letter = letters[i][j]))
			
			if first:
				first = False
			else:
				text += "\n\n"

			text += row_text
		
		return text

	def __str__(self):
		return self.string()

	def __getitem__(self, pos):
		'''
		Returns the item at the given vector position
		Does not support negative indexing
		'''
		if pos.x < 0 or pos.y < 0:
			raise IndexError
		return self.board[pos.y][pos.x]

	def __contains__(self, item):
		if isinstance(item, Vector2):
			return item.x >= 0 and item.x < self.size.x and item.y >= 0 and item.y < self.size.y
	
	# returns the mirroed pos on the board
	def invert(self, pos):
		return  self.size - Vector2(1,1) - pos

	def place(self, pos, card):
		self.board[pos.y][pos.x] = card			

	def is_full(self):
		#print(self.board)
		return all(map( all, self.board ))

	def __iter__(self):
		for y,row in enumerate(self.board):
			for x,card in enumerate(row):
				yield (Vector2(x,y), card)

	def reveal_from(self, other, inverted = True):
		'''
		Makes all cards revealed on the given board but not on this one revealed
		'''
		for pos, card in self:
			#print(pos)
			other_card = other[other.invert(pos) if inverted else pos]
			if card and (not card.revealed) and other_card and other_card.revealed:
				self.place(pos, EnemyCard.from_card(other_card.invert() if inverted else other_card))

	def copy(self):
		'''
		Returns a semi-deep copy of the board (card objects and bellow are not coppied)
		'''
		new_board = Board(self.size.x,self.size.y)
		for item in self:
			new_board.place(*item)
		return new_board
