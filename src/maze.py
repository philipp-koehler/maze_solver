from point import Point
from line import Line
from cell import Cell
import time


class Maze:

    def __init__(
        self, start, num_rows, num_cols, cell_size_x, cell_size_y, win=None
    ):
        self.start = start
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self.cells = self.create_cells()

    def create_cells(self):
        cells = []
        left = Point(self.cell_size_x, 0)
        down = Point(0, self.cell_size_y)
        for i in range(0, self.num_cols):
            cols = []
            for j in range(0, self.num_rows):
                cell = Cell(
                    False,
                    False,
                    False,
                    False,
                    self.start + down * i + left * j,
                    self.start + down * (i + 1) + left * (j + 1),
                    self.win,
                )
                cols.append(cell)
                print(cols)
                self.draw_cells(cell)
            cells.append(cols)
            print(cells)
        return cells

    def draw_cells(self, cell):
        cell.draw("black")

    def animate(self):
        if self.win is not None:
            self.win.redraw()
            time.sleep(0.05)
