from graphics import *
from Button import *
import random
from fish import *
from shark import *



def main():
    
    grid()

#AQUATICS
    F1 = fish(win)
    F2 = fish(win)
    F3 = fish(win)
    S = shark(win)
#FISHES in a list
    fishsss = [F1, F2, F3]

#BUTTONS
    Q = Button(win, Point(500, 500), Point(550, 540), "plum1", "QUIT")
    R = Button(win, Point(500, 450), Point(550, 490), "plum1", "Reset")
    M = Button(win, Point(500, 400), Point(550, 440), "plum1", "Move")
    

    while True:
        
        m = win.getMouse()

        if R.isClicked(m):

            S.undraw()
            for fishes in fishsss:
                fishes.undraw() #undraws every fish?
            main()
            
        if M.isClicked(m):
            for fishes in fishsss:
                fishes.undraw()
                fishes.randomMove(win)
            

        if Q.isClicked(m):
            break

    win.close()
            
        

def grid():
    x = 0
    y = 0

    #vertical lines
    for i in range(21):

        verticals = Line(Point(x, 0), Point(x, 400))
        verticals.draw(win)

        x = x + 20

    #horizontal lines
    for i in range(21):

        horizontals = Line(Point(0, y), Point(400, y))
        horizontals.draw(win)

        y = y + 20


if __name__ == "__main__":

    win = GraphWin("ooo big shark scary", 600, 600)
    win.setBackground("white")

    main()
