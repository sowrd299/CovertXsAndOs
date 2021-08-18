from .card import Card

class EnemyCard (Card):

	friendly = False	
	label = "foe"

	@staticmethod
	def from_card(card):
		'''
		A factory for making an enemy card from a card
		Incorporates the class of the card as a superclass
		'''

		class MadeEnemyCard(EnemyCard, type(card)):
			pass

		enemy_card = MadeEnemyCard(card.name, card.cost, card.symbol, card.atk_sides, card.def_sides)
		return enemy_card 