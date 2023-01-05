
from graphics import *
from Button import *
import random

def main():

    grid()

    #buttons

    Q = Button(win, Point(500, 500), Point(550, 540), "plum1", "QUIT")
    R = Button(win, Point(500, 450), Point(550, 490), "plum1", "Reset")
    M = Button(win, Point(500, 400), Point(550, 440), "plum1", "Move")



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

    '''
    fish = Image(Point(loc1[0], loc1[1]), "ONE.png")
    fish2 = Image(Point(loc2[0], loc2[1]), "TWO.png")
    fish3 = Image(Point(loc3[0], loc3[1]), "THREE.png")
    shark = Image(Point(loc4[0], loc4[1]), "shark.png")
   
    shark.draw(win)
    fish.draw(win)
    fish2.draw(win)
    fish3.draw(win)
    
'''




    #buttons running

    while True:

        fish = Image(Point(loc1[0], loc1[1]), "ONE.png")
        fish2 = Image(Point(loc2[0], loc2[1]), "TWO.png")
        fish3 = Image(Point(loc3[0], loc3[1]), "THREE.png")
        shark = Image(Point(loc4[0], loc4[1]), "shark.png")

        shark.draw(win)
        fish.draw(win)
        fish2.draw(win)
        fish3.draw(win)


        leftFish = ((loc1[0] - 20), loc1[1])
        leftFish2 = ((loc2[0] - 20), loc2[1])
        leftFish3 = ((loc3[0] - 20), loc3[1])
        rightFish = ((loc1[0] + 20), loc1[1])
        rightFish2 = ((loc2[0] + 20), loc2[1])
        rightFish3 = ((loc3[0] + 20), loc3[1])
        upFish = (loc1[0], (loc1[1] + 20))
        upFish2 = (loc2[0], (loc2[1] + 20))
        upFish3 = (loc3[0], (loc3[1] + 20))
        downFish = (loc1[0], (loc1[1] - 20))
        downFish2 = (loc2[0], (loc2[1] - 20))
        downFish3 = (loc3[0], (loc3[1] - 20))

        #fish go random

        

        m = win.getMouse()

        if R.isClicked(m):
            fish.undraw()
            fish2.undraw()
            fish3.undraw()
            shark.undraw()
            main()

        if M.isClicked(m):
            fish.undraw()
            fish2.undraw()
            fish3.undraw()
            shark.undraw()


            #fish one 
            if (loc4[0] - loc1[0]) < (loc4[1] - loc1[1]):

                #l/r
                if loc4[0] > loc1[0]:
                    if loc1[0] == 50:
                        loc1 = rightFish
                    else:
                        loc1 = leftFish

                else:
                    if loc1[0] == 430:
                        loc1 = leftFish
                    else:
                        loc1 = rightFish

            else:
                #up/down
                if loc4[1] < loc1[1]:
                    if loc1[1] == 430:
                        loc1 = downFish
                    else:
                        loc1 = upFish

                else:
                    if loc1[1] == 50:
                        loc1 = upFish
                    else:
                        loc1 = downFish

            #fish 2
            if (loc4[0] - loc2[0]) < (loc4[1] - loc2[1]):
                
                #l/r
                if loc4[0] > loc2[0]:
                    if loc2[0] == 50:
                        loc2 = rightFish2
                    else:
                        loc2 = leftFish2
                else:
                    if loc2[0] == 430:
                        loc2 = leftFish2
                    else:
                        loc2 = rightFish2
 
            else:
                
                #up/down
                if loc4[1] < loc2[1]:
                    if loc2[1] == 430:
                        loc2 = downFish2
                    else:
                        loc2 = upFish2

                else:
                    if loc2[1] == 50:
                        loc2 = upFish2
                    else:
                        loc2 = downFish2

            #FISH 3
            if (loc4[0] - loc3[0]) < (loc4[1] - loc3[1]):

                #l/r
                if loc4[0] > loc3[0]:
                    if loc3[0] == 50:
                        loc3 = rightFish3
                    else:
                        loc3 = leftFish3
                else:
                    if loc3[0] == 430:
                        loc3 = leftFish3
                    else:
                        loc3 = rightFish3

            else:

                #up/down
                if loc4[1] < loc3[1]:
                    if loc3[1] == 430:
                        loc3 = downFish3
                    else:
                        loc3 = upFish3

                else:
                    if loc3[1] == 50:
                        loc3 = upFish3
                    else:
                        loc3 = downFish3

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
