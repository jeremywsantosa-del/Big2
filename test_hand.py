from card import Card
from hand import Hand
from handtype import HandType

# Singles
low_single = Hand([Card("3", "Diamond")])
high_single = Hand([Card("4", "Diamond")])
assert low_single.hand_type == HandType.SINGLE
assert high_single.beats(low_single)
assert not low_single.beats(high_single)

# Pairs: same rank, higher suit wins
pair_low_suit = Hand([Card("5", "Diamond"), Card("5", "Club")])
pair_high_suit = Hand([Card("5", "Heart"), Card("5", "Spade")])
assert pair_high_suit.beats(pair_low_suit)
assert not pair_low_suit.beats(pair_high_suit)

# Pairs: different rank
pair_low_rank = Hand([Card("5", "Diamond"), Card("5", "Club")])
pair_high_rank = Hand([Card("6", "Diamond"), Card("6", "Club")])
assert pair_high_rank.beats(pair_low_rank)

# Triples
triple_low = Hand([Card("7", "Diamond"), Card("7", "Club"), Card("7", "Heart")])
triple_high = Hand([Card("9", "Diamond"), Card("9", "Club"), Card("9", "Heart")])
assert triple_high.beats(triple_low)

# Invalid combinations
try:
    Hand([Card("3", "Diamond"), Card("4", "Club")])
    assert False, "expected ValueError for invalid pair"
except ValueError:
    pass

# Mismatched sizes can't be compared
try:
    low_single.beats(pair_low_suit)
    assert False, "expected ValueError for size mismatch"
except ValueError:
    pass

# Straight: must be consecutive, not just distinct ranks
gappy = [Card("3", "Diamond"), Card("5", "Club"), Card("7", "Heart"), Card("9", "Spade"), Card("J", "Diamond")]
try:
    Hand(gappy)
    assert False, "expected ValueError for non-consecutive 'straight'"
except ValueError:
    pass

straight_low = Hand([Card("3", "Diamond"), Card("4", "Club"), Card("5", "Heart"), Card("6", "Spade"), Card("7", "Diamond")])
straight_high = Hand([Card("8", "Diamond"), Card("9", "Club"), Card("10", "Heart"), Card("J", "Spade"), Card("Q", "Diamond")])
assert straight_high.hand_type == HandType.STRAIGHT
assert straight_high.beats(straight_low)
assert not straight_low.beats(straight_high)

# Flush: same suit, non-consecutive ranks
flush_low = Hand([Card("3", "Club"), Card("5", "Club"), Card("7", "Club"), Card("9", "Club"), Card("J", "Club")])
flush_high = Hand([Card("4", "Club"), Card("6", "Club"), Card("8", "Club"), Card("10", "Club"), Card("K", "Club")])
assert flush_low.hand_type == HandType.FLUSH
assert flush_high.beats(flush_low)
assert flush_high.beats(straight_high)  # flush outranks straight regardless of card values

# Full house: compared by the triple's rank, not the pair's
full_house_low = Hand([Card("3", "Diamond"), Card("3", "Club"), Card("3", "Heart"), Card("K", "Diamond"), Card("K", "Club")])
full_house_high = Hand([Card("4", "Diamond"), Card("4", "Club"), Card("4", "Heart"), Card("5", "Diamond"), Card("5", "Club")])
assert full_house_high.beats(full_house_low)  # triple of 4s beats triple of 3s despite lower pair

# Four of a kind: compared by the quad's rank, not the kicker
quad_low = Hand([Card("6", "Diamond"), Card("6", "Club"), Card("6", "Heart"), Card("6", "Spade"), Card("A", "Diamond")])
quad_high = Hand([Card("7", "Diamond"), Card("7", "Club"), Card("7", "Heart"), Card("7", "Spade"), Card("3", "Diamond")])
assert quad_high.beats(quad_low)
assert quad_low.beats(full_house_high)  # four of a kind outranks full house

# Straight flush beats everything else at 5 cards
straight_flush = Hand([Card("3", "Spade"), Card("4", "Spade"), Card("5", "Spade"), Card("6", "Spade"), Card("7", "Spade")])
assert straight_flush.hand_type == HandType.STRAIGHT_FLUSH
assert straight_flush.beats(quad_high)

# Invalid 5-card combo (two pair) is rejected
try:
    Hand([Card("3", "Diamond"), Card("3", "Club"), Card("4", "Heart"), Card("4", "Spade"), Card("5", "Diamond")])
    assert False, "expected ValueError for two pair"
except ValueError:
    pass

print("All hand tests passed.")
