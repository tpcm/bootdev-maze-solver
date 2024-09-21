import random
import time
from cell import Cell

class Maze:
    def __init__(
            self,
            x1,
            y1,
            num_rows,
            num_cols,
            size_x,
            size_y,
            win=None,
            seed=None,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size_x = size_x
        self.size_y = size_y
        self.win = win
        if seed is not None:
            random.seed(seed)

        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited()
    
    def _create_cells(self):
        for col in range(self.num_cols):
            row = [Cell(self.win) for num in range(self.num_rows)]
            self._cells.append(row)
        
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        
    def _draw_cell(self, i, j):
        if self.win is None:
            return
        x1=self.x1 + (i * self.size_x)
        y1=self.y1 + (j * self.size_y)
        self._cells[i][j].draw(
            x1=x1,
            y1=y1,
            x2=x1 + self.size_x,
            y2=y1 + self.size_y
        )
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0,0)
        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._draw_cell(self.num_cols-1, self.num_rows-1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        if i == 0:
            col_neighbours = [1]
        elif i == self.num_cols-1:
            col_neighbours = [-1]
        else:
            col_neighbours = [-1, 1]
        if j == 0:
            row_neighbours = [1]
        elif j == self.num_rows-1:
            row_neighbours = [-1]
        else:
            row_neighbours = [-1, 1]
        while True:
            to_visit = []
            for col_neighbour in col_neighbours:
                if self._cells[i+col_neighbour][j] and self._cells[i+col_neighbour][j].visited == False:
                    to_visit.append({"coords": (i+col_neighbour, j),"vertical":False, "direction": col_neighbour})
            for row_neighbour in row_neighbours:
                    if self._cells[i][j+row_neighbour] and self._cells[i][j+row_neighbour].visited == False:
                        to_visit.append({"coords": (i, j+row_neighbour),"vertical":True, "direction": row_neighbour})
            if not to_visit:
                return
            
            neighbour_to_visit = random.choice(to_visit)
            
            if neighbour_to_visit["vertical"]:
                if neighbour_to_visit["direction"] == -1:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j-1].has_bottom_wall = False
                else:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j+1].has_top_wall = False
            elif not neighbour_to_visit["vertical"]:
                if neighbour_to_visit["direction"] == -1:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i-1][j].has_right_wall = False
                else:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i+1][j].has_left_wall = False
            
            self._draw_cell(neighbour_to_visit["coords"][0], neighbour_to_visit["coords"][1])
            self._draw_cell(i, j)
            self._break_walls_r(neighbour_to_visit["coords"][0], neighbour_to_visit["coords"][1])

    def _reset_cells_visited(self):
        for col in self._cells:
            for cell in col:
                cell.visited = False

    def solve(self):
        return self._solve_r(0, 0)
    
    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True
        if (i == self.num_cols-1) and (j == self.num_rows-1):
            return True
        
        # left
        if (
            i > 0
            and not self._cells[i - 1][j].visited
            and not self._cells[i][j].has_left_wall
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            solved = self._solve_r(i - 1, j)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], undo=True)
        # right
        if (
            i < self.num_cols - 1
            and not self._cells[i + 1][j].visited
            and not self._cells[i][j].has_right_wall
            ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            solved = self._solve_r(i + 1, j)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], undo=True)
        # up
        if (
            j > 0
            and not self._cells[i][j - 1].visited
            and not self._cells[i][j].has_top_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            solved = self._solve_r(i, j - 1)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], undo=True)
        # down
        if (
            j < self.num_rows - 1
            and not self._cells[i][j + 1].visited
            and not self._cells[i][j].has_bottom_wall
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            solved = self._solve_r(i, j + 1)
            if solved:
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], undo=True)

        return False
        





