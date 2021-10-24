# Create a deck of 52 cards,Shuffle the deck
# Ask the Player for their bet
# Make sure that the Player’s bet does not exceed their available chips
# Deal two cards to the Dealer and two cards to the Player
# Show only one of the Dealer’s cards, the other remains hidden
# Show both of the Player’s cards
# Ask the Player if they wish to Hit, and take another card
# If the Player’s hand does not Bust (go over 21), ask if they’d like to Hit again.
# If a Player Stands, play the Dealer’s hand. The dealer will always Hit until the Dealer’s value meets or exceeds 17
# Determine the winner and adjust the Player’s chips accordingly
# Ask the Player if they’d like to play again

# declare the deck cards

import random

suits = ('club', 'hearts', 'diamond', 'spade')
ranks = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'jack', 'queen', 'king', 'ace')
values = {'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10,
          'jack': 10, 'queen': 10, 'king': 10, 'ace': 11}


# created a class for the card with only two attribute suit and rank then created function for both
class card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return self.rank + 'of' + self.suit


# lets create a deck that has 52 cards
def shuffle(self):
    random.shuffle(self.deck)


class deck:
    def __init__(self):
        self.deck = {}
        for suit in suits:
            for rank in ranks:
                self.deck.append(card(suit, rank))

    def __str__(self):
        deck_com = ''  # empty string
        for card in self.deck:
            deck_com += '/n' + card.__str__()  # add each card object's print string
            return 'the deck cards has' + deck_com

    def deal(self):
        single_card = self.deck.pop(self)
        return single_card
