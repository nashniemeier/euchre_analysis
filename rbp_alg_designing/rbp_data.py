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

all_suits = ['Hearts', 'Diamonds', 'Spades', 'Clubs']

# To make this algorithm, we will use these weights (type double)

trump_power_weight = 0.0
num_aces_weight = 0.0
num_suits_weight = 0.0

print("=====================")
print("= WELCOME TO EUCHRE =")
print("=    PLAY / PASS    =")
print("=    SIMULATION!    =")
print("=====================")

# Begin checking hands, for each player

for player in player_list:

	player.hand = game_deck.deal(5)

	print(f"\n{player.name}'s hand :")
	print("~~~~~~~~~~~~~")

	suit_list = []

	# Check the strength of the hand for each suit as trump

	keep_print = True

	# For each suit to be trump

	for trump_suit in all_suits:

		num_aces = 0
		trump_power_sum = 0
		# Num Suits = len(suit_list)

		# For each card in the hand

		for card in player.hand:

			#if keep_print == True:
			#	print(f"{card.number} of {card.suit}")
			if card.suit not in suit_list:
				suit_list.append(card.suit)

			if card.suit == trump_suit:
				trump_power_sum += card.get_power(trump_suit, None)
			if card.number == 'A':
				print("ACE FOUND")
				num_aces += 1

		# keep_print = False

		overall_weight = (
			(trump_power_sum * trump_power_weight)
			+ (num_aces * num_aces_weight)
			- (len(suit_list) * num_suits_weight)
		)

	print(f"{len(suit_list)} Suited")






# Now the players hands are set, we should do calculations




