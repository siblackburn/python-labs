'''
Challenge: Build a card game!
Create your objects
Chapter 18 of the Think Python book does a great job of explaining inheritance through the creation of Cards, Decks, and Hands.
http://greenteapress.com/thinkpython2/html/thinkpython2019.html

First, follow the book and build out the examples in that chapter.

Create your game
Next, attempt to build a card game that utilizes the classes you created earlier.

Inspirations
http://openbookproject.net/pybiblio/tips/wilson/simpleCardGame.php
https://github.com/AllenDowney/ThinkPython2/blob/master/code/Card.py
Resources
Python Tutorial: https://docs.python.org/3.6/tutorial/classes.html#inheritance
Chapter 18: Inheritance: http://greenteapress.com/thinkpython2/html/thinkpython2019.html
'''

import random

#defining how the deck is composed, in terms of suit and rank and their relative position to each other
class Card():
    def __init__(self, suit = 0, rank = 1):
        self.suit = suit
        self.rank = rank

    suit_names = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    rank_names = [None, 'Ace', '2', '3', '4', '5', '6', '7',
                      '8', '9', '10', 'Jack', 'Queen', 'King']

    def __str__(self):
        return '%s of %s' % (Card.rank_names[self.rank], Card.suit_names[self.suit])

#where does "other" come from? how does Python use this to compare to cards to decide which is better?
    def __lt__(self, other):
        t1 = self.suit, self.rank
        t2 = other.suit, other.rank
        return t1 < t2


# defining the cards in a deck

class Deck():

    def __init__(self):
        self.cards = []
        for suit in range(4):
            for rank in range(1, 14):
                card = Card(suit, rank) # don't understand why we're defining the card as "suit" rather than "suit_names".
                # Aren't we trying to populate a full deck using this function? If so why aren't we looking up the names?
                self.cards.append(card)

    def __str__(self):
        res = []
        for card in self.cards:
            res.append(str(card))
        return '\n'.join(res)


my_deck = Deck()
print(my_deck)

# don't understand how to now check that we have a full deck of cards to call from. Shouldn't self.cards now contain 52 cards?
# when i try to print self.cards is says code is unreachable

#here we're defining functions that might be useful for the game. e.g. picking a random card, adding a card etc
def pop_card(self):
    return self.cards.pop()

def add_card(self, card):
    self.cards.append(card)

def shuffle(self):
    random.shuffle(self.cards)



    card1 = Card(2,11)
    print(card1)

#hand of cards class inherits methods from Deck class. If we write another init, it will overwrite the parents init


#I don't understand this class! We're trying to create a hand, but we're creating a new "label" attribute
# and I don't understand why. Shouldn't we inherit suit and rank from classCard? Then random to pick a card, and add it to
# our new hand?
class Hand(Deck):

    def __init__(self, label = ''):
        self.cards = []
        self.label = label
#what does label do?
        hand = Hand(new_hand) #is this simply creating a new list which will be our list of cards representing one hand?
        hand.cards = []
        hand.label = 'new_hand'

        deck = Deck()
        card = deck.pop_card()
        hand.add_card(card)
        print(hand)



'''
example of how to call a comparison between 2 hands
hand1 = Card(1,2)
hand2 = Card(2,4)

if hand1.rank > hand2.rank:
    print("win")
else:
    print("lose")
'''


