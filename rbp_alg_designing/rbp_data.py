# The purpose of this file is to collect data on the hands I generate in real time
# to determine how a hand should be decided to be picked up or passed

import sys
from pathlib import Path

root_dir = Path(__file__).resolve().parent.parent
sys.path.appd(str(root_dir))

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

for player in player_list:

	for i in range(5):

		print(f"Card {i} for player {player.name}")
		rank = input("Enter the rank: ")
		suit = input("Enter the suit: ")
