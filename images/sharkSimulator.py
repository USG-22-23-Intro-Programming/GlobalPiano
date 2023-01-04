from graphics import *
from Button import *
import random

def main():

    grid()
        
    #buttons

    Q = Button(win, Point(500, 500), Point(550, 540), "plum1", "QUIT")
    R = Button(win, Point(500, 450), Point(550, 490), "plum1", "Reset")



    #fish stuff

    listOfLocations = []

    #smallest / left top coords
    x1 = 50
    y1 = 50

    while x1 < 430:
        y1 = 50

        while y1 < 430:
            y1 = y1 + 20
            coords = (x1, y1)

            listOfLocations.append(coords)
        x1 = x1 + 20
    

    loc1 = random.choice(listOfLocations)
    loc2 = random.choice(listOfLocations)
    loc3 = random.choice(listOfLocations)
    loc4 = random.choice(listOfLocations)
    
    fish = Image(Point(loc1[0], loc1[1]), "fish.png")
    fish2 = Image(Point(loc2[0], loc2[1]), "fish.png")
    fish3 = Image(Point(loc3[0], loc3[1]), "fish.png")
    shark = Image(Point(loc4[0], loc4[1]), "shark.png")
    shark.draw(win)
    fish.draw(win)
    fish2.draw(win)
    fish3.draw(win)


    #buttons running

    while True:
        
        m = win.getMouse()

        if R.isClicked(m):
            fish.undraw()
            fish2.undraw()
            fish3.undraw()
            shark.undraw()
            main()

        if Q.isClicked(m):
            break
    win.close()

def grid():
    x = 0
    y = 0

    #vertical
    for i in range(21):

        verticals = Line(Point(40 + x, 40), Point(40 + x, 440))
        verticals.draw(win)

        x = x + 20

    #horizontal
    for i in range(21):

        horizontals = Line(Point(40, 40 + y), Point(440, 40 + y))
        horizontals.draw(win)

        y = y + 20

    

if __name__ == "__main__":

    #window
    win = GraphWin("ooo big shark scary", 600, 600)
    win.setBackground("white")

    main()
