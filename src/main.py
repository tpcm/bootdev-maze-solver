from graphics import Window, Line, Point
from cell import Cell

def main():
    win = Window(800, 600)

    p1 = Point(5,5)
    p2 = Point(250,250)
    line = Line(p1, p2)
    # win.draw_line(line, fill_colour="black")
    
    cell = Cell(window=win)
    cell.has_bottom_wall = False
    cell.draw(x1=5, y1=5, x2=50, y2=50)

    cell = Cell(window=win)
    cell.has_top_wall = False
    cell.has_bottom_wall = False
    cell.has_right_wall = False
    cell.draw(x1=5, y1=50, x2=50, y2=100)

    cell = Cell(window=win)
    cell.has_top_wall=False
    cell.draw(x1=5, y1=100, x2=50, y2=150)

    cell = Cell(window=win)
    cell.has_left_wall=False
    cell.has_right_wall = False
    cell.draw(x1=50, y1=50, x2=100, y2=100)

    cell = Cell(window=win)
    cell.has_bottom_wall = False
    cell.draw(x1=100, y1=5, x2=145, y2=50)

    cell = Cell(window=win)
    cell.has_top_wall = False
    cell.has_bottom_wall = False
    cell.has_left_wall = False
    cell.draw(x1=100, y1=50, x2=145, y2=100)

    cell = Cell(window=win)
    cell.has_top_wall=False
    cell.draw(x1=100, y1=100, x2=145, y2=150)

    
    win.wait_for_close()

if __name__ == "__main__":
    main()