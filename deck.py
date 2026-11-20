from card import Card, SUITS, RANKS
import random

class Deck:
    def __init__(self):
        self.cards = [Card(rank, suit) for suit in SUITS for rank in RANKS]

    def shuffle(self):
        random.shuffle(self.cards)
        return self.cards

    def deal(self, num_players=4): #TEMP: initial game is played by 4 players
        self.shuffle()
        return [self.cards[i::num_players] for i in range(num_players)]
    