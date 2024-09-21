from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    p1 = Point(5,5)
    p2 = Point(250,250)
    line = Line(p1, p2)
    # win.draw_line(line, fill_colour="black")
    
    cell_1 = Cell(window=win)
    cell_1.has_bottom_wall = False
    cell_1.draw(x1=5, y1=5, x2=50, y2=50)

    cell_2 = Cell(window=win)
    cell_2.has_top_wall = False
    cell_2.has_bottom_wall = False
    cell_2.has_right_wall = False
    cell_2.draw(x1=5, y1=50, x2=50, y2=100)

    cell_3 = Cell(window=win)
    cell_3.has_top_wall=False
    cell_3.draw(x1=5, y1=100, x2=50, y2=150)

    cell_4 = Cell(window=win)
    cell_4.has_left_wall=False
    cell_4.has_right_wall = False
    cell_4.draw(x1=50, y1=50, x2=100, y2=100)

    cell_5 = Cell(window=win)
    cell_5.has_bottom_wall = False
    cell_5.draw(x1=100, y1=5, x2=145, y2=50)

    cell_6 = Cell(window=win)
    cell_6.has_top_wall = False
    cell_6.has_bottom_wall = False
    cell_6.has_left_wall = False
    cell_6.draw(x1=100, y1=50, x2=145, y2=100)

    cell_7 = Cell(window=win)
    cell_7.has_top_wall=False
    cell_7.draw(x1=100, y1=100, x2=145, y2=150)

    cell_1.draw_move(cell_2, True)
    cell_2.draw_move(cell_4, True)
    cell_4.draw_move(cell_6, True)
    cell_6.draw_move(cell_7)

    
    win.wait_for_close()

if __name__ == "__main__":
    main()