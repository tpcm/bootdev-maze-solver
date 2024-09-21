from graphics import Window, Line, Point, Cell

def main():
    win = Window(800, 600)

    p1 = Point(5,5)
    p2 = Point(250,250)
    line = Line(p1, p2)
    # win.draw_line(line, fill_colour="black")

    Cell(window=win, x1=5, y1=5, x2=50, y2=50, has_bottom_wall=False).draw()
    Cell(window=win, x1=5, y1=50, x2=50, y2=100, has_top_wall=False, has_bottom_wall=False, has_right_wall=False).draw()
    Cell(window=win, x1=5, y1=100, x2=50, y2=150, has_top_wall=False).draw()

    Cell(window=win, x1=50, y1=50, x2=100, y2=100, has_left_wall=False, has_right_wall=False).draw()
    
    Cell(window=win, x1=100, y1=5, x2=145, y2=50, has_bottom_wall=False).draw()
    Cell(window=win, x1=100, y1=50, x2=145, y2=100, has_top_wall=False, has_bottom_wall=False, has_left_wall=False).draw()
    Cell(window=win, x1=100, y1=100, x2=145, y2=150, has_top_wall=False).draw()

    Cell(window=win, x1=160, y1=5, x2=200, y2=50, has_bottom_wall=False).draw()
    Cell(window=win, x1=160, y1=50, x2=200, y2=100, has_top_wall=False, has_bottom_wall=False).draw()
    Cell(window=win, x1=160, y1=100, x2=200, y2=150, has_top_wall=False).draw()
    
    win.wait_for_close()

if __name__ == "__main__":
    main()