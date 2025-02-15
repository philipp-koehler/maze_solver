import unittest
from point import Point
from maze import Maze


class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 2
        num_rows = 3
        m1 = Maze(Point(0, 0), num_rows, num_cols, 10, 10)
        self.assertEqual(
            len(m1.cells),
            num_cols,
        )
        self.assertEqual(
            len(m1.cells[0]),
            num_rows,
        )


if __name__ == "__main__":
    unittest.main()
