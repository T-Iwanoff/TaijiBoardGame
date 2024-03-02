import random
from util.game import TaijiGame

class TaijiAI:
    def __init__(self, player):
        self.player = player

    def get_move(self, game):
        # Generate all possible moves
        possible_moves = [(i, j) for i in range(9) for j in range(9) if game.is_valid_move(i, j)]
        # Evaluate each move using a basic heuristic
        best_move = None
        best_score = -float('inf')
        for move in possible_moves:
            temp_game = TaijiGame()
            temp_game.board = [row[:] for row in game.board]
            temp_game.current_player = game.current_player
            temp_game.place_taijitu(move[0], move[1])
            score = temp_game.calculate_score(self.player)
            if score > best_score:
                best_score = score
                best_move = move
        return best_move

class ComputerAI:
    def __init__(self, player):
        self.player = player

    def get_move(self, game):
        # Generate all possible moves
        possible_moves = [(i, j) for i in range(9) for j in range(9) if game.is_valid_move(i, j)]
        # Randomly select a move
        return random.choice(possible_moves) if possible_moves else None
