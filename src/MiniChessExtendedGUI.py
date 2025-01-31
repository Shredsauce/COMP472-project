import tkinter as tk
from MiniChessExtended import MiniChessExtended

class MiniChessExtendedGUI(MiniChessExtended):
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("MiniChess GUI")
        self.create_board()
        self.selected_square = None

    def create_board(self):
        self.board_buttons = {}
        for row in range(5):
            for col in range(5):
                square_color = "white" if (row + col) % 2 == 0 else "gray"
                btn = tk.Button(
                    self.window,
                    bg=square_color,
                    width=6,
                    height=3,
                    command=lambda r=row, c=col: self.on_square_click(r, c),
                )
                btn.grid(row=row, column=col)
                self.board_buttons[(row, col)] = btn

    def get_piece_at(self, row, col):
        board = self.current_game_state["board"]
        return board[row][col]

    def update_board(self):
        for (row, col), btn in self.board_buttons.items():
            piece = self.get_piece_at(row, col)
            btn.config(text=piece if piece != "." else "")

    def on_square_click(self, row, col):
        if not self.selected_square:
            self.selected_square = (row, col)
        else:
            move = (self.selected_square, (row, col))
            if self.is_valid_move(self.current_game_state, move):
                self.make_move(self.current_game_state, move)
                self.update_board()
            else:
                print("Invalid move!")
            self.selected_square = None

    def play(self):
        self.update_board()
        self.window.mainloop()

if __name__ == "__main__":
    game = MiniChessExtendedGUI()
    game.play()
