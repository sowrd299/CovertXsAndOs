from .card import Card
from .enemy_card import EnemyCard

'''
A file for subclass of the type "card" that represent different
...cards with different special abilities 
'''

class ExposedCard(Card):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.ability_text += "⚲"
		self.full_ability_text += "This card will be played face up for you oponent to see."

	def get_secret_card(self):
		return EnemyCard.from_card(self).invert()