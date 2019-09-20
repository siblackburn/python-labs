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
print(my_deck) # this prints the total deck, as we've compiled it above.
# we create deck, then we print that decks .cards. deck is different to Deck. Deck is the class
print(type(my_deck))

# don't understand how to now check that we have a full deck of cards to call from. Shouldn't self.cards now contain 52 cards?
# when i try to print self.cards is says code is unreachable

#here we're defining functions that might be useful for the game. e.g. picking a random card, adding a card etc
def pop_card(self):
    return self.cards.pop()

def add_card(self, card):
    self.cards.append(card)

def shuffle(self):
    random.shuffle(self.cards)


'''
everything above here is imported from card_game. Everything below is my first attempt at dealing a random hand and comparing it to a computers hand
steps:
1. Deal 2 random cards to the user
2. Deal 2 random cards to the computer
3. Remove all 4 cards from the deck
4. Check they have been removed from the deck
5. Compare the total number in each hand. If one is bigger than the other, print that the hand has won
6. If they are the same number compare suits. whichever has the highest ranking single card wins
'''

user_hand = []


class Hand(Deck):
    def __init__(self, suit, rank):
        while i < 2:
            choice = random.choice(my_deck)
            user_hand.append(choice)
            i += 1


    def __str__(self):
        return user_hand


print(user_hand)
