import random 

#  This file is to set up our data structure, the card. In here there will be
#  dictionaries that specify the powers and the suits, as well as the class that
#  allows us to construct our card objects.

# This is a dictionary, it allows us to map a value to another value,
# and allows us to work between types. This dictionary holds values for
# the card strengths, as it is much easier to visibily see the rank of a card
# Rather than memorizing numbers.
#
# Note LB = Left Bower, RB = Right Bower

POWER = {

	'9': 1,
	'10': 2,
	'J': 3,
	'Q': 4,
	'K': 5,
	'A': 6

}

# Here is another dictionary! This time for suits

SUIT = {

	'Spades': 'Black',
	'Clubs': 'Black',
	'Diamonds': 'Red',
	'Hearts': 'Red'

}

# Here is a Python class for our card.

class Card:

	def __init__(self, suit, rank):

		self.suit = suit
		self.rank = POWER[rank]

		# We do not use SUIT[suit] because that is how we get the color of a card
	# End __init()

	def __repr__(self):
		match self.suit:
			case 'Spades':
				return f"{self.rank}♠"
			case 'Clubs':
				return f"{self.rank}♣"
			case 'Hearts':
				return f"{self.rank}♡"
			case 'Diamonds':
				return f"{self.rank}♢"
			case _:
				return "Unknown suit"
	# End __repr()


	# get_suit() takes in the trump suit and returns the suit of a card
	# For the left bower, trump_suit will be returned

	def get_suit(self, trump_suit):
		if SUIT[self.suit] == SUIT[trump_suit] and self.rank == 3:
			return trump_suit
		else:
			return self.suit
	# End get_suit()

	# get_power() returns the power of a card and adjusts according to trump.
	# If a card is trump (excluding the right and left) then the rank will be
	# the power + 6 (since 9 of trump beats ace of non-trump)

	def get_power(self, trump_suit, led_suit):

		# Take care of the jack case first
		# If we have a jack and the colors match

		if self.rank == 3 and SUIT[self.suit] == SUIT[trump_suit]:

			# Now split by what is right and left

			if self.suit == trump_suit:
				return self.rank + 11 # This would return 14 with our dictionary
			else:
				return self.rank + 10 # This would return 13 with our dictionary

		# Now we need to take care of the rest of the trump cards, a simple check

		if self.suit == trump_suit:

			return self.rank + 6 # 9: 1->7, 10: 2->8,..., A: 6->12 ✓

		# Check if a player is simply throwing off

		if self.suit != led_suit:
			return 0
		# If the card is on suit, it is its own rank
		return self.rank
	# End get_power()

	# is_trump() accepts a card and checks if it is trump. If so, return True
	# otherwise return false

	def is_trump(self, trump_suit):
		if get_suit(self, trump_suit) == trump_suit:
			return True
		else:
			return False

	# End is_trump()

	# beats() is our main comparison function, comparing two cards. Returns true
	# if self's get_power() return is strictly greater than that of other_card's

	def beats(self, other_card, trump_suit, led_suit):

		if self.get_power(self, trump_suit, led_suit) > 
		   other_card.get_power(self, trump_suit, led_suit):
			return True
		else:
			return False
	# End beats()

# End Card class

# The Deck class holds our cards. The field cards is the only field in the
# object, and there are a few methods to go with it

class Deck:

	# __init__() initalizes our object

	def __init__(self):

		# This is called a list comprehension, a quick way to make a list

		self.cards = [Card(s, p) for s in SUIT for p in POWER]

	# End __init()

	# shuffle() just uses Python's shuffle() method in the random module

	def shuffle(self):

		random.shuffle(self.cards)

	# End shuffle()
	
	# This function deals cards, and will later be used by the players for their decks

	def deal(self, num_cards):

		if num_cards > 5 or num_cards > len(self.cards):
			print("INVALID DEAL")
			return

		popped_cards = []
		for i in range(num_cards):
			popped_cards.append(self.cards.pop())

		return popped_cards

	# End deal()



