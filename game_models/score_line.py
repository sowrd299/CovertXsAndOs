class ScoreLine():
	'''
	This class represents a row of spaces that allow a player
	to score a point.
	Implements the rules for scoring 
	'''

	def __init__(self, origin, vector, board):

		self.friendly = None
		self.symbol = None

		self.size = board.size

		self.spaces = []

		space = origin
		while space in board:
			card = board[space]
			if not card:
				pass # NOTE: Allows blank spaces to be included in lines
			else:
				match_friendly = self.friendly == None or self.friendly == card.friendly
				match_symbol = not self.symbol or self.symbol == card.symbol
				if match_friendly and match_symbol:
					self.friendly = card.friendly
					self.symbol = card.symbol
				else:
					# Stop the line if encounter an enemy card or a card with a different symbol
					break

			self.spaces.append(space)
			space += vector


	def __str__(self):
		l = [ ["☐" for i in range(self.size.x)] for j in range(self.size.y) ]
		for space in self.spaces:
			l[space.y][space.x] = str(self.symbol)

		return "\n".join( map(lambda x : "".join(x), l) )


	def get_score(self, spaces_needed = 3):
		'''
		A line is worth 1 point iff it has atleast one card and three spaces
		'''
		return 1 if self.symbol and len(self.spaces) >= spaces_needed else 0
					

