import os
import tkinter as tk
from PIL import Image, ImageTk
from MiniChessExtended import MiniChessExtended

class MiniChessExtendedGUI(MiniChessExtended):
    def __init__(self):
        super().__init__()
        self.window = tk.Tk()
        self.window.title("MiniChess GUI")
        self.canvas = tk.Canvas(self.window, width=250, height=250)
        self.canvas.pack()
        self.piece_images = self.load_piece_images()
        self.create_board()
        self.selected_square = None

    def load_piece_images(self):
        """Load images for each chess piece"""
        base_path = "images/pieces"
        pieces = {
            "wp": "white_pawn.png", "wN": "white_knight.png", "wB": "white_bishop.png",
            "wR": "white_rook.png", "wQ": "white_queen.png", "wK": "white_king.png",
            "bp": "black_pawn.png", "bN": "black_knight.png", "bB": "black_bishop.png",
            "bR": "black_rook.png", "bQ": "black_queen.png", "bK": "black_king.png"
        }
        images = {}
        for piece, filename in pieces.items():
            filepath = os.path.join(base_path, filename)
            try:
                img = Image.open(filepath).resize((40, 40), Image.Resampling.LANCZOS)
                images[piece] = ImageTk.PhotoImage(img)
            except Exception as e:
                print(f"Error loading image for {piece}: {e}")
        return images

    def create_board(self):
        self.board_squares = []
        colors = ["white", "gray"]
        for row in range(5):
            row_squares = []
            for col in range(5):
                x1, y1 = col * 50, row * 50
                x2, y2 = x1 + 50, y1 + 50
                color = colors[(row + col) % 2]
                square = self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline="black")
                row_squares.append(square)
            self.board_squares.append(row_squares)
        self.update_board()

    def get_piece_at(self, row, col):
        board = self.current_game_state["board"]
        return board[row][col]

    def update_board(self):
        self.canvas.delete("pieces")
        for row in range(5):
            for col in range(5):
                piece = self.get_piece_at(row, col)
                if piece != ".":
                    x, y = col * 50 + 5, row * 50 + 5
                    self.canvas.create_image(x, y, anchor=tk.NW, image=self.piece_images.get(piece, ""), tags="pieces")

    def on_square_click(self, event):
        col, row = event.x // 50, event.y // 50
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
        self.canvas.bind("<Button-1>", self.on_square_click)
        self.window.mainloop()

if __name__ == "__main__":
    game = MiniChessExtendedGUI()
    game.play()