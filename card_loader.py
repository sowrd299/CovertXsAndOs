from game_models.card import Card, UP, DOWN, LEFT, RIGHT
from game_models.symbol import Symbol
from game_models.ability_cards import ExposedCard


'''
This card contains all the available cards in the game
'''


HARO_SYMB = Symbol("⚔", "House Haro")
AVOND_SYMB = Symbol("♚", "House Avond")
CALITUS_SYMB = Symbol("C", "House Calitus")
BLAI_SYMB = Symbol("B", "House Blai")

NAVOSC_MERC = Card("Navosc Trained Merc", 0, HARO_SYMB, [UP], [DOWN])
GUNSLINGER = Card("Portov d'Ana Gunslinger", 0, HARO_SYMB, [LEFT, RIGHT], [])
TURRET = Card("Broadsword-Class Turret", 0, HARO_SYMB, [UP, DOWN], [])
ENFORCER = Card("Dockside Enforcer", 0, HARO_SYMB, [RIGHT], [LEFT])

TOWNSHIP_PATROL = ExposedCard("Township Patrol", 0, BLAI_SYMB, [UP, DOWN], [RIGHT]) 
PICKPOCKET = Card("Pucov Pickpocket", 0, BLAI_SYMB, [DOWN], [RIGHT])




BODYGUARD = Card("Senate Bodyguard", 0, AVOND_SYMB, [UP], [UP])
INFORMANT = Card("Aristocratic Informant", 0, AVOND_SYMB, [DOWN], [DOWN] )
STREET_PATROL = Card("Olimpiav Street Patrol", 0, AVOND_SYMB, [RIGHT], [RIGHT])
ARISTOCRAT = Card("Hinterland Aristocrat", 0, AVOND_SYMB, [LEFT], [LEFT])
WARHERO = ExposedCard("Warhero Senator", 0, AVOND_SYMB, [UP], [UP, RIGHT])
DIPLOMAT = ExposedCard("Senetorial Diplomat", 0, AVOND_SYMB, [UP], [LEFT, RIGHT])

DIGINITARY = Card("Cijangle Dignatary", 0, CALITUS_SYMB, [], [RIGHT, UP, DOWN])