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
            win,
    ):
        self._cells = []
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.size_x = size_x
        self.size_y = size_y
        self.win = win

        self._create_cells()
    
    def _create_cells(self):
        for col in range(self.num_cols):
            row = [Cell(self.win) for num in range(self.num_rows)]
            self._cells.append(row)
        for i in range(self.num_cols):
            for j in range(self.num_rows):
                self._draw_cell(i, j)
        


    def _draw_cell(self, i, j):
        self._cells[i][j].draw(
            x1=(self.x1 + self.size_x) * i,
            y1=(self.y1 + self.size_y) * j,
            x2=(self.x1 + self.size_x) * i + self.size_x,
            y2=(self.y1 + self.size_y) * j + self.size_y
        )
        self._animate()
    
    def _animate(self):
        self.win.redraw()
        time.sleep(0.05)