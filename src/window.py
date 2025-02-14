from tkinter import Tk, BOTH, Canvas
from line import Line
from maze import Maze
from maze import Maze

class Window:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.root = Tk()
        self.root.title("Maze Solver")
        self.canvas = Canvas()
        self.canvas.pack()
        self.running = False
        self.root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self) -> None:
        self.root.update_idletasks()
        self.root.update()

    def wait_for_close(self) -> None:
        self.running = True
        while self.running:
            self.redraw()

    def close(self) -> None:
        self.running = False 

    def draw_line(self, line: Line, fill_color: str) -> None:
        line.draw(self.canvas, fill_color)

    def draw_maze(self, maze) -> None:
        Maze.create_cells(self.canvas)
