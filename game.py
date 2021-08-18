from game_models.score_line import ScoreLine
from util.vector2 import Vector2

class Game():
	'''
	A class for running a game
	'''


	def __init__(self, players):
		self.players = players
		self.turn_ind = 0
		self.ongoing = True

		# DRAW OPENING HANDS
		for player in self.players:
			player.shuffle()
			player.draw_hand()


	def place_card(self, placing_player, pos, card):
		for player in self.players:
			if placing_player == player:
				player.board.place(pos, card)
			else:
				player.board.place(player.board.invert(pos), card.get_secret_card())


	@staticmethod
	def resolve_board(board):
		'''
		TODO: Maybe these make sense in another class
		Returns a board with all the attacked and undefended cards removed
		'''
		new_board = board.copy()
		for pos, card in board:
			if card:
				for attack in card.atk_sides:
					attacked_pos = pos + attack
					try:
						if board[attacked_pos] and card.friendly != board[attacked_pos].friendly and (not attack.invert() in board[attacked_pos].def_sides):
							new_board.place(attacked_pos, None)
					except IndexError as e:
						pass
			
		return new_board


	@staticmethod
	def score_board(board):
		# TODO: Maybe this makes sense in another class?
		# TODO: This shouldn't assume a square board... but it does
		vertical_lines = [ ScoreLine(Vector2(i,0), Vector2(0,1), board) for i in range(board.size.x) ]
		horizontal_lines = [ ScoreLine(Vector2(0,i), Vector2(1,0), board) for i in range(board.size.y) ]
		diagonal_lines = [ 
			ScoreLine(Vector2(0,0), Vector2(1,1), board),
			ScoreLine(Vector2(0,board.size.y-1), Vector2(1,-1), board)
		]
		return vertical_lines + horizontal_lines + diagonal_lines

	
	def play_card(self, player, pos, card ):
		'''
		Enters the given player's turn action
		Does NOT enforce turn order
		'''
		player.play(card)
		self.place_card(player, pos, card )
		player.draw()
		self.next_turn()


	# TURN MANAGEMENT
	def next_turn(self):
		'''
		Advances the turn order
		Will also end the game when appropriate
		'''
		if self.players[0].board.is_full():
			self.end_game()
		else:
			self.turn_ind += 1
			self.turn_ind %= len(self.players)


	def get_turn_player(self):
		return self.players[self.turn_ind]


	def end_game(self):
		'''
		Will manage the final score at the end of the game
		'''
		self.ongoing = False
		for player in self.players:
			for other_player in filter(lambda x : x != player, self.players):
				player.board.reveal_from(other_player.board)


	def get_score(self, player):
		'''
		Returns the in-progress (resovled board, score lines) for the given
		player
		'''

		resolved_board = self.resolve_board(player.board) 
		score_lines = self.score_board(resolved_board)
		player_score_lines = filter(lambda x : x.get_score() > 0 and x.friendly, score_lines)

		return (resolved_board, player_score_lines)