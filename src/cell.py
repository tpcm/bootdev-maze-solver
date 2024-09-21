from graphics import Line, Point

class Cell:
    def __init__(self, window) -> None:
        self.__window = window
        self.__x1 = None
        self.__y1 = None
        self.__x2 = None
        self.__y2 = None
        self.has_left_wall = True
        self.has_right_wall = True
        self.has_top_wall = True
        self.has_bottom_wall = True

    def draw(self, x1, y1, x2, y2):
        self.__x1 = x1
        self.__y1 = y1
        self.__x2 = x2
        self.__y2 = y2
        if self.has_left_wall:
            left_line = Line(Point(x1, y1), Point(x1, y2))
            self.__window.draw_line(left_line, fill_colour="black")
        if self.has_right_wall:
            right_line = Line(Point(x2, y1), Point(x2, y2))
            self.__window.draw_line(right_line, fill_colour="black")
        if self.has_top_wall:
            top_line = Line(Point(x1, y1), Point(x2, y1))
            self.__window.draw_line(top_line, fill_colour="black")
        if self.has_bottom_wall:
            bottom_line = Line(Point(x1, y2), Point(x2, y2))
            self.__window.draw_line(bottom_line, fill_colour="black")