from player import Player
from util.writer import side_by_side
from util.vector2 import Vector2

from card_loader import *
from game import Game

from functools import reduce
import re


'''
This script runs the game in a CLI
'''


def print_score(player_score_lines):
	print("\n" + side_by_side("\nControlled Lines: ", reduce(side_by_side, player_score_lines, "")) + "\n")



DECKS = [
	[TOWNSHIP_PATROL, GUNSLINGER, TURRET, ENFORCER, PICKPOCKET] * 2,
	[BODYGUARD, INFORMANT, WARHERO, ARISTOCRAT, DIPLOMAT] *2
]
	

if __name__ == "__main__":

	game = Game([ Player(deck = DECKS[i]) for i in range(2) ] )

	# the CLI
	while game.ongoing:
		# taking turns
		player = game.get_turn_player()
		i = game.turn_ind

		# Turn hider
		input("Side {}, Begin your turn.".format(i))

		print("\n\n  == SIDE {} ==  ".format(i))
		print("  == SCENARIO ==  ")
		print_score(game.get_score(player)[1])
		print(player.board.string([[i * player.board.size.x + j for j in range(player.board.size.x)] for i in range(player.board.size.y)]))
		print("  == HAND ==  ")
		print(reduce(side_by_side, map(str, player.hand)))
		for i,card in enumerate(player.hand):
			print("\\ {} /".format(i), end=" ") # TODO: I don't like how hard coded this is
		print("")

		# Command parsing
		while True:
			command = input("\n Command _")
			args = re.split("[ -]", command)

			try:
				if args[0] == "help":
					print("\n info # - Shows more information about card # in your hand.")
					print(" #-# - Places card # from your hand on space #.")
					print(" help - Don't be silly.")
				elif args[0] == "info":
					print("\n" + player.hand[int(args[1])].get_info())
				else:
					card = player.hand[int(args[0])]
					x = int(args[1]) % player.board.size.x
					y = int(args[1]) // player.board.size.y
					pos = Vector2(x,y)
					if not player.board[pos]:
						game.play_card(player, pos, card)
						break
					else:
						print("Error - Grid space is already occupied!")
			except ValueError as e:
				print("Error - Illegal command!")
			except IndexError as e:
				print("Error - There is no such card!")


		print("\n\n  == SCENARIO DEVELOPMENT ==  ")
		print_score(game.get_score(player)[1])
		print(player.board)

		input("Side {}, End your turn.".format(i))
		print("\n" * 60)


# Wrapping up the game
for i,player in enumerate(game.players):

	resolved_board, player_score_lines = game.get_score(player)

	print("\n\n  == FINAL OUTCOME (SIDE {}'S PERSPECTIVE) ==".format(i))
	print_score(player_score_lines)
	print(side_by_side(player.board, resolved_board, "   --->   "))
