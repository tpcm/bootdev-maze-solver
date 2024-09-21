from graphics import Line, Point

class Cell:
    def __init__(self, window) -> None:
        self._window = window
        self._x1 = None
        self._y1 = None
        self._x2 = None
        self._y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        if self.has_left_wall:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self._window.draw_line(left_line, fill_colour="black")
        if self.has_right_wall:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self._window.draw_line(right_line, fill_colour="black")
        if self.has_top_wall:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self._window.draw_line(top_line, fill_colour="black")
        if self.has_bottom_wall:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self._window.draw_line(bottom_line, fill_colour="black")
    
    def draw_move(self, to_cell, undo=False):
        x_midpoint_1 = self._x1 + 0.5*(self._x2 - self._x1)
        y_midpoint_1 = self._y1 - 0.5*(self._y1 - self._y2)

        x_midpoint_2 = to_cell._x1 + 0.5*(to_cell._x2 - to_cell._x1)
        y_midpoint_2 = to_cell._y1 - 0.5*(to_cell._y1 - to_cell._y2)

        line = Line(
            Point(x_midpoint_1, y_midpoint_1),
            Point(x_midpoint_2, y_midpoint_2)
        )
        if undo:
            fill_colour = "grey"
        else:
            fill_colour = "red"

        self._window.draw_line(line, fill_colour)