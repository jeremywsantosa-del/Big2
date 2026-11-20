from handtype import HandType
from card import RANK_VALUE, SUIT_VALUE, RANKS, SUITS
from collections import Counter

def classify(cards):
    if len(cards) == 1:
        return HandType.SINGLE
    elif len(cards) == 2:
        ranks = {card.rank for card in cards}
        if len(ranks) == 1:
            return HandType.PAIR
        else:
            raise ValueError("Invalid pair.")
    elif len(cards) == 3:
        ranks = {card.rank for card in cards}
        if len(ranks) == 1:
            return HandType.TRIPLE
        else:
            raise ValueError("Invalid triple.")

    elif len(cards) == 5:
        rank_counts = sorted(Counter(card.rank for card in cards).values())
        rank_values = sorted(RANK_VALUE[card.rank] for card in cards)
        if rank_counts == [1,4]:
            return HandType.FOUR_OF_A_KIND
        if rank_counts == [2,3]:
            return HandType.FULL_HOUSE

        suits = {card.suit for card in cards}
        is_straight = len(rank_counts) == 5 and rank_values[-1] - rank_values[0] == 4
        is_flush = len(suits) == 1
        if is_straight and is_flush:
            return HandType.STRAIGHT_FLUSH
        if is_straight:
            return HandType.STRAIGHT
        if is_flush:
            return HandType.FLUSH
        raise ValueError("Invalid five-card hand.")
    else:
        raise ValueError("Invalid hand length.")

class Hand:
    def __init__(self, cards):
        self.cards = sorted(cards)
        self.hand_type = classify(self.cards)

    def highest_card(self):
        return self.cards[-1]

    def group_rank_value(self, count):
        ranks = Counter(card.rank for card in self.cards)
        matching_rank = next(rank for rank, n in ranks.items() if n == count)
        return RANK_VALUE[matching_rank]

    def beats(self, other):
        if len(self.cards) != len(other.cards):
            raise ValueError("Hands must have the same number of cards to compare.")
        if self.hand_type != other.hand_type:
            return self.hand_type > other.hand_type
        if self.hand_type == HandType.FULL_HOUSE:
            return self.group_rank_value(3) > other.group_rank_value(3)
        if self.hand_type == HandType.FOUR_OF_A_KIND:
            return self.group_rank_value(4) > other.group_rank_value(4)
        return self.highest_card() > other.highest_card()