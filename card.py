from functools import total_ordering

RANKS = ["3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A", "2"]
SUITS = ["Diamond", "Club", "Heart", "Spade"]

RANK_VALUE = {rank: index for index, rank in enumerate(RANKS)}
SUIT_VALUE = {suit: index for index, suit in enumerate(SUITS)}


@total_ordering
class Card:
    def __init__(self, rank, suit):
        if rank not in RANK_VALUE:
            raise ValueError(f"Invalid rank: {rank}")
        if suit not in SUIT_VALUE:
            raise ValueError(f"Invalid suit: {suit}")
        self.rank = rank
        self.suit = suit

    @property
    def rank_value(self):
        return RANK_VALUE[self.rank]

    @property
    def suit_value(self):
        return SUIT_VALUE[self.suit]

    def __eq__(self, other):
        return self.rank_value == other.rank_value and self.suit_value == other.suit_value #without this, python would assume ex: 3 != diamond, when card is 3 of diamonds

    def __lt__(self, other):
        return (self.rank_value, self.suit_value) < (other.rank_value, other.suit_value) #compare first by rank then by suit

    def __hash__(self):
        return hash((self.rank, self.suit)) #cards can be used in sets and as dictionary keys

    def __repr__(self):
        return f"{self.rank} of {self.suit}" #text representation
