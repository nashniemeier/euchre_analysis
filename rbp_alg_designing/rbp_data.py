# The purpose of this file is to collect data on the hands I generate in real time
# to determine how a hand should be decided to be picked up or passed

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.append(str(root_dir))

from euchre.cards import Card, Deck
from euchre.players import BasePlayer

# Initialize the objects we will work with.

game_deck = Deck()

p_one = BasePlayer("p1")
p_two = BasePlayer("p2")
p_three = BasePlayer("p3")
p_four = BasePlayer("p4")

# We have a player list to go through

player_list = [p_one, p_two, p_three, p_four]
game_deck.shuffle()

for player in player_list:

	player.hand = game_deck.deal(5)

	print(f"\n{player.name}'s hand :")
	print("~~~~~~~~~~~~~")

	hand_sum = 0
	suit_list = []

	for card in player.hand:

		print(f"{card.number} of {card.suit}")
		hand_sum += card.rank
		if card.suit not in suit_list:
			suit_list.append(card.suit)

	print(suit_list)
	
	print(f"SUM = {hand_sum}")
	print(f"{len(suit_list)} Suited")




# Now the players hands are set, we should do calculations




