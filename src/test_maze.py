import unittest

from maze import Maze

class TestMaze(unittest.TestCase):
    def test_maze_create_cells(self):
        num_rows = 12
        num_cols = 16
        cell_size_x = 50
        cell_size_y = 50

        maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        self.assertEqual(
            len(maze._cells),
            num_cols
        )

        self.assertEqual(
            len(maze._cells[0]),
            num_rows
        )

    def test_maze_create_big_cols(self):
        num_rows = 10
        num_cols = 10
        cell_size_x = 100
        cell_size_y = 50

        maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)

        self.assertEqual(
            len(maze._cells),
            num_cols
        )

        self.assertEqual(
            len(maze._cells[0]),
            num_rows
        )

    def test_maze_break_entrance_and_exit(self):
        num_rows = 10
        num_cols = 10
        cell_size_x = 100
        cell_size_y = 50

        maze = Maze(0, 0, num_rows, num_cols, cell_size_x, cell_size_y)
        self.assertTrue(maze._cells[0][0])
        self.assertTrue(maze._cells[num_cols-1][num_rows-1])
        self.assertFalse(
            maze._cells[0][0].has_top_wall)
        self.assertFalse(
            maze._cells[num_cols-1][num_rows-1].has_bottom_wall)

if __name__ == "__main__":
    unittest.main()
