import random
from tkinter import *


class FifteenPuzzle:
    def __init__(self):
        self.board = self._create_start_position()
        self._empty_cell = self._get_empty_cell()

    def _get_empty_cell(self):
        row = -1
        col = -1
        for row_index, row_tmp in enumerate(self.board):
            for col_index, col_tmp in enumerate(row_tmp):
                if col_tmp == "":
                    return row_index, col_index
        return row, col

    def _create_start_position(self):
        board = []
        all_values = [str(i) for i in range(1, 16)] + [""]
        random.shuffle(all_values)
        for row_number in range(4):
            board.append(all_values[4 * row_number: 4 * (row_number + 1)])
        return board

    def __repr__(self):
        return "\n".join(["\t".join(row) for row in self.board])

    def move(self, direction):
        row, col = self._empty_cell
        new_row, new_col = self._empty_cell

        if direction == "down" and row < 3:
            new_row = row + 1
        elif direction == "up" and row > 0:
            new_row = row - 1
        elif direction == "right" and col < 3:
            new_col = col + 1
        elif direction == "left" and col > 0:
            new_col = col - 1

        self.board[row][col], self.board[new_row][new_col] = self.board[new_row][new_col], self.board[row][col]

        self._empty_cell = new_row, new_col


class FifteenPuzzleUI:
    def __init__(self):
        self.game = FifteenPuzzle()
        self._root = Tk()
        self._root.title("15")
        self._root.geometry("275x280")
        self._root.configure(background='black')
        self._root.bind("<Left>", self._left)
        self._root.bind("<Right>", self._right)
        self._root.bind("<Up>", self._up)
        self._root.bind("<Down>", self._down)
        self._set_ui()

    def _set_ui(self):
        for row_index, row in enumerate(self.game.board):
            for col_index, col in enumerate(row):
                label = Entry(self._root, width=2, fg='white', bg='black', font=('Arial', 50, 'bold'), justify='center')
                label.config(highlightbackground="black")
                label.grid(row=row_index, column=col_index)
                label.insert(END, col)

    def _move(self, direction):
        self.game.move(direction)
        self._set_ui()

    def _left(self, event):
        self._move("left")

    def _right(self, event):
        self._move("right")

    def _up(self, event):
        self._move("up")

    def _down(self, event):
        self._move("down")

    def run(self):
        self._root.mainloop()


if __name__ == "__main__":
    fifteen = FifteenPuzzleUI()
    fifteen.run()
