# This file details a few types of players and makes algorithms for them to play
# at different levels. There will be a player that Randomly plays correct cards
# and a player that plays more "smart." Eventually, in phase 4 there will be
# MLPlayer, one who learns to play based on previous games
#
# This file uses classes and subclasses, thank you online documentation

class BasePlayer:

	def __init__(self, name):

		self.name = name
		self.hand = []
	
	def receive_cards(self, cards):
		self.hand = 


