#
#  This file is to set up our data structure, the card. In here there will be
#  dictionaries that specify the powers and the suits, as well as the class that
#  allows us to construct our card objects.
#


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
  'A': 6,
  'LB': 7,
  'RB': 8

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

  def __repr__(self):
    return f"Card is the {rank} of {suit}"


