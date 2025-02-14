from window import Window
from point import Point
from line import Line
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    maze = Maze(Point(0, 0), 5, 5, 50, 50, win)
    maze.create_cells()
    win.wait_for_close()
        
if __name__ == "__main__":
    main()
