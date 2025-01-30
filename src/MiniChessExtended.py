from MiniChessSkeletonCode import MiniChess

class MiniChessExtended(MiniChess):
    def __init__(self):
        super().__init__()

    def is_valid_move(self, game_state, move):
        return super().is_valid_move(game_state, move)

    def valid_moves(self, game_state):
        return super().valid_moves(game_state)

def play():
    game = MiniChessExtended()
    game.play()

if __name__ == "__main__":
    play()
