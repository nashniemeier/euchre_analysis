import random
from euchre import cards

# This file details a few types of players and makes algorithms for them to play
# at different levels. There will be a player that Randomly plays correct cards
# and a player that plays more "smart." Eventually, in phase 4 there will be
# MLPlayer, one who learns to play based on previous games
#
# This file uses classes and subclasses, thank you online documentation

# This is the base class BasePlayer with methods __init()__,
# receive_card(), and get_legal_moves()

class BasePlayer:

	# __init__() creates a player object with a name and a hand

	def __init__(self, name):

		self.name = name
		self.hand = []
	# End __init__()

	# receive_cards() accepts cards dealt to it later in engine.py

	def receive_cards(self, cards):
		self.hand += cards
	# End receive_cards()

	# get_legal_moves() checks and returns the legal cards.
	# - If there is no led_suit, then all cards are able to be played
	# - If a player has no cards that match led_suit, return all cards
	# - Otherwise returns all cards that follow led_suit

	def get_legal_moves(self, led_suit, trump_suit):

		if led_suit == None:
			return self.hand

		legal_cards = []

		for card in self.hand:
			if card.get_suit(trump_suit) == led_suit:
				legal_cards += card

		if len(legal_cards) == 0:
			return self.hand
		else:
			return legal_cards

	# End get_legal_moves()

# End of base class BasePlayer

class RandomPlayer(BasePlayer):

	def play_card(self, led_suit, trump_suit):
		legal_cards = get_legal_moves(led_suit, trump_suit)
		
		card_to_remove = random.choice(legal_cards)

		if card_to_remove in self.hand:
			index_in_hand = self.hand.index(card_to_remove)
			return self.hand.pop(index_in_hand)
		else:
			print("ERROR! RandomPlayer had a missing card in play_card()")
			exit(1)
	
	# End play_card()

class RuleBasedPlayer(BasePlayer):

	pass

# So much to figure out here, more to do :)


