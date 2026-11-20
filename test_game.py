from game import Game
from card import Card

game = Game(["Alice", "Bob", "Carol", "Dave"])

# Force a deterministic setup: give Alice the 3 of Diamonds and control her turn
for player in game.state.players:
    player.hand = []

alice, bob, carol, dave = game.state.players
alice.hand = [Card("3", "Diamond"), Card("4", "Diamond"), Card("5", "Diamond")]
bob.hand = [Card("3", "Club"), Card("4", "Club")]
carol.hand = [Card("6", "Heart")]
dave.hand = [Card("7", "Spade")]
game.state.current_player_index = 0

# Opening play must include the 3 of Diamonds
try:
    game.play([Card("4", "Diamond")])
    assert False, "expected ValueError: opening play without 3D"
except ValueError:
    pass

# Legal opening play: Alice(0) -> Bob(1)
game.play([Card("3", "Diamond")])
assert game.state.current_player_index == 1
assert not game.state.is_first_move
assert game.state.last_played_hand.cards == [Card("3", "Diamond")]

# 3 of Diamonds is the lowest card in the deck, so any single legally beats it: Bob(1) -> Carol(2)
game.play([Card("3", "Club")])
assert game.state.current_player_index == 2
assert game.state.last_played_hand.cards == [Card("3", "Club")]

# Carol(2) passes -> Dave(3)
game.pass_turn()
assert game.state.current_player_index == 3

# Dave(3) passes -> Alice(0)
game.pass_turn()
assert game.state.current_player_index == 0

# Alice(0) passes -> comes full circle back to Bob, table clears
game.pass_turn()
assert game.state.last_played_hand is None
assert game.state.current_player_index == 1

# Bob is now leading with nothing to beat -> cannot pass
try:
    game.pass_turn()
    assert False, "expected ValueError: cannot pass while leading"
except ValueError:
    pass

# Bob leads freely with a stronger single than his last play
game.play([Card("4", "Club")])
assert game.state.current_player_index == 2

# Carol has only a 6 of Hearts, which beats 4 Club -> legal
game.play([Card("6", "Heart")])
assert game.state.current_player_index == 3

# Dave's 7 of Spades beats 6 of Hearts and empties his hand -> Dave wins
game.play([Card("7", "Spade")])
assert game.state.winner is dave
assert dave.is_empty()

print("All game tests passed.")
