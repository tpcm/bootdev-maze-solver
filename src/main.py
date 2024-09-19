from graphics import Window, Line, Point

def main():
    win = Window(800, 600)
    
    p1 = Point(5,5)
    p2 = Point(250,250)
    line = Line(p1, p2)
    win.draw_line(line, fill_colour="black")

    win.wait_for_close()

if __name__ == "__main__":
    main()