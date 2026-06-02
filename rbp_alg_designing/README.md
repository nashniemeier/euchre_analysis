# Introduction

This file contains my thought process on making an algorithm that determines
A players moves from determining what trump should be to playing each card.<br>

## Step 1, Real hands

First, I dealt some Euchre hands to see a hand that I would call Trump on and I kept these in mind. Here are a few key things that stood out to me in Euchre hands:

1. **Number of Trump Versus Strength of Trump**<br>

	I noticed that there were times where I would have 2-3 trump cards, but they were not the strongest cards. For example, one of my hands I had the 9, Q, A of
	diamonds, then two other Queens. I noticed that this is not a hand that I would pick up because the trump is too weak and I do not have any aces to fall back
	on. With this, I realize the importance of having the right or left. 

	However, there would be hands (very rarely) where there are four trump cards. Now thinking about this, the worst case scenario is you'd have the 9, 10, Q, K
	of trump, and then that leaves the top 3 still out there (A, L, R). Now it would be extremely rare for a one player to have the top 3 and another player have
	the bottom 4 of trump, so it would be a great idea to call trump with 4 or more.

	Bottom line, having 3 or more trump is very dependent on the strength of the cards, but having 4 or more trump is almost an instant call no matter the strength

2. **Aces are Important**<br>

	Imagine a hand with the Right and Ace of trump. Having two trump in its own is a risky move to call trump, but these are two strong cards (that I've called
	trump on a few times). But there are times where I would definitely not call it, and I probably would not call trump if I did not have an Ace (that wasn't trump).
	This highlights the importance of having aces in your hand, they are a strong lead in the beginning and end of a round.

3. **Number of Suits Show a Hand's Potential**<br>

	There was a bit of an error I came up with, and that was overestimating the importance of having fewer suits in hand. While yes it is incredibly helpful and a
	player is far more likely to succeed with that, there are many other dilemmas a player would face before looking at that as a reason to pass.
<br>
	In my algorithm, I do think the number of suits is something to keep in mind, but I do not want it to be the only thing that limits the strength of a hand.

## Step 2, Get Some Numbers

The next step in figuring out this algorithm was to generate some numbers using what I observed from the real hands above. I first made a small engine that builds a
deck and 4 players, then dealt 5 cards to each player (Note I did not do the 2-3-2-3 3-2-3-2 deal, just 5 to each player).
<br><br>
I had hands randomly generated using the shuffle() method I designed in the Deck class. I would then print out the hands to see what hands I would call Trump on.
For each player's hand, I would also print out how many unique suits they had, how many aces, and the sum of the strength of their trump.
<br><br>
I created a spreadsheet that tracked the Total Trump Power (TPS), Average Total Trump Power (AVGTP), TPS * AVGTP, TPS * AVGTP * AVGTP / 1000, Number of Aces, 
my personal calling confidence, and Final Score ((TPS * AVGTP) + (TPS * AVGTP * AVGTP / 1000))
<br><br>
Here are some graphs that go with that data (based off 16 hands, for each trump out of 4 suits, 64 data points)

![Graph of confidence of a Euchre Hand vs. TPS * TPAVG](https://docs.google.com/spreadsheets/d/e/2PACX-1vREVjvAyvumOnqigWEj9qFK4UlV9yPDguN_08UVGvZxEtRZTNil4QGVemd-VLnI11KKjPEM0tTjCP69/pubchart?oid=1274441869&format=image)

![Graph of confidence of a Euchre Hand vs. TPS * TPAVG * TPAVG / 1000](https://docs.google.com/spreadsheets/d/e/2PACX-1vREVjvAyvumOnqigWEj9qFK4UlV9yPDguN_08UVGvZxEtRZTNil4QGVemd-VLnI11KKjPEM0tTjCP69/pubchart?oid=1534187539&format=image)

![Graph of confidence of a Euchre Hand vs. Final Score](https://docs.google.com/spreadsheets/d/e/2PACX-1vREVjvAyvumOnqigWEj9qFK4UlV9yPDguN_08UVGvZxEtRZTNil4QGVemd-VLnI11KKjPEM0tTjCP69/pubchart?oid=654096712&format=image)
