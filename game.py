import random

moves_beat_matrix = { "rock": ["scissors"], "paper": ["rock"], "scissors": ["paper"] }

class Game:
    def __init__(self):
        self.computer_move = random.choice(list(moves_beat_matrix.keys()))
        self.player_move = ""

    def set_player_move(self, move: str):
        self.player_move = move.lower()

    def determine_winner(self) -> str:
        if self.player_move == self.computer_move:
            return "tie"
        elif self.computer_move in moves_beat_matrix[self.player_move]:
            return "computer"
        return "player"

    def __str__(self) -> str:
        return f"Winner: {self.determine_winner()}. Computer move: {self.computer_move}. Player move: {self.player_move}\n"
