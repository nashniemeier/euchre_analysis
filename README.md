# Analysis of a Euchre hand

### Purpose

  The purpose of this project is to learn more about data science / machine learning, Pythonskills, problem solving, and the probabilities that lie within Euchre.

### Representations + The data structure

  We are representing cards as an object with two items. The first is the suit, listed below. The second is the strength of the card, also listed below.

#### Suits

DIAMONDS - 1<br>
HEARTS   - 2<br>
CLUBS    - 3<br>
SPADES   - 4<br>

#### Powers

##### Not trump, on suit

9 = 1<br>
10 = 2<br>
Jack = 3 (Not bower)<br>
Queen = 4<br>
King = 5<br>
Ace = 6<br>

##### For Trump

9 = 7<br>
10 = 8<br>
Queen = 10<br>
King = 11<br>
Ace = 12<br>
Left bower = 13<br>
Right bower = 14<br>

##### Not trump, off suit

All cards are 0, this is called throwing off

#### The deck

The deck consists of the 24 cards in Euchre, and contains methods to shuffle and deal cards

### An explanation on the players

*As an exclaimer, it is understood that there is not necessarily an algorithm to Euchre,
and when coming up with the algorithm of which card is best to play I tried my best to
preserve a typical mindset with playing cards.*

In this project, the goal is to have 3 types of players that stem from BasePlayer.
To begin, BasePlayer has their hand and a name to keep track of the player
<br>
Then we split off into 3 types of players:<br>

1. RandomPlayer
	Pretty straight forward, this player plays a valid card at random. What
	we can learn from this player is seeing the hands that are nearly impossible to lose,
	or what hands the RandomPlayer gets lucky on.
<br>
2. RuleBasedPlayer
	I designed algorithms to determine if a player should order up a card as trump or not.
	To see all of my scratch work + ideas go into this, please refer to
	rbp-alg.md
	<br>
	But here are the rules I made:

	Using an algorithm I turned into code, this player will do the following:




