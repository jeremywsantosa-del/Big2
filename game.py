from deck import Deck
from gamestate import GameState
from player import Player
from card import Card
from hand import Hand

class Game:
    def __init__(self, players):
        self.deck = Deck()
        self.state = GameState()
        self.state.players = [Player(name) for name in players]
        self._deal()

    def _deal(self):
        hands = self.deck.deal()
        for player, hand in zip(self.state.players, hands):
            player.hand = hand
        self.state.current_player_index = self._find_starting_player()

    def _find_starting_player(self):
        three_of_diamonds = Card("3", "Diamond")
        for i, player in enumerate(self.state.players):
            if player.has_card(three_of_diamonds):
                return i
        raise RuntimeError("No player holds the 3 of diamonds.")

    def play(self, cards):
        player = self.state.get_current_player()
        hand = Hand(cards)

        if self.state.is_first_move:
            if Card("3", "Diamond") not in cards:
                raise ValueError("The opening play must include the 3 of Diamonds.")
        elif self.state.last_played_hand is not None:
            if not hand.beats(self.state.last_played_hand):
                raise ValueError("This hand does not beat the last played hand.")

        player.play_cards(cards)
        self.state.record_play(player, hand)

        if player.is_empty():
            self.state.set_winner(player)

    def pass_turn(self):
        if self.state.last_played_hand is None:
            raise ValueError("You must play a hand when leading; you cannot pass.")
        self.state.record_pass()