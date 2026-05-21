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

  # get_suit() takes in the trump suit and returns the suit of a card
  # For the left bower, trump_suit will be returned

  def get_suit(self, trump_suit):
    if SUIT[self.suit] == SUIT[trump_suit] and self.rank == 3:
      return trump_suit
    else:
      return self.suit

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

    # Otherwise, if not trump just return the rank

    if self.suit != led_suit:
      return 0

    return self.rank

  # End of get_power()

  # is_trump() accepts a card and checks if it is trump. If so, return True
  # otherwise return false

  def is_trump(self, trump_suit):

    if get_suit(self) == trump_suit:
      return True
    else:
      return False

  # End of is_trump()


