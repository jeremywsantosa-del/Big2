class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def play_cards(self, cards):
        for card in cards:
            if card not in self.hand:
                raise ValueError(f"Card {card} not in hand")
        for card in cards:
            self.hand.remove(card)
  
    def has_card(self, card):
        return card in self.hand

    def is_empty(self):
        return len(self.hand) == 0
    