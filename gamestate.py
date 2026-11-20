class GameState:
    def __init__(self):
        self.players = []
        self.current_player_index = 0
        self.last_played_hand = None
        self.last_player = None
        self.pass_count = 0
        self.is_first_move = True #first moveof the game (3 of diamonds)
        self.winner = None

    def get_current_player(self):
        return self.players[self.current_player_index] if self.players else None

    def get_last_player(self):
        return self.last_player

    def get_winner(self):
        return self.winner

    def get_last_played_hand(self):
        return self.last_played_hand

    def get_pass_count(self):
        return self.pass_count

    def advance_turn(self):
        self.current_player_index = (self.current_player_index + 1) % len(self.players)

    def record_play(self, player, hand):
        self.last_played_hand = hand
        self.last_player = player
        self.pass_count = 0
        self.is_first_move = False
        self.advance_turn()

    def record_pass(self):
        self.pass_count += 1
        if self.pass_count >= len(self.players) - 1:
            self.last_played_hand = None
            self.pass_count = 0
        self.advance_turn()

    def set_winner(self, player):
        self.winner = player

    def reset(self):
        self.current_player_index = 0
        self.last_played_hand = None
        self.last_player = None
        self.pass_count = 0
        self.is_first_move = True
        self.winner = None
        self.players = []
    
