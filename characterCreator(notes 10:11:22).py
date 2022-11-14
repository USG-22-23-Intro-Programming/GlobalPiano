from graphics import*
from Button import*

def main():

    win = GraphWin("character creator", 800, 600)#window name, length, height
    win.setBackground("DarkSeaGreen1")

    #MOVE EVERYTHING OVER!!!!!
    a = 50 # x coords

    C = Circle(Point(300 + a, 300), 150)#center xy coords,radius outside
    #object defult to be hidden, so u need to call it
    C.draw(win) # win bc it draws it in that window if theres multiple

    #R = Rectangle(Point(200,500), Point(400, 575))
    #R.draw(win)

    #L = Line(Point(0, 0), Point(800, 600))
    #L.draw(win)


    BigEye1 = Circle(Point(225 + a, 250), 50)
    BigEye2 = Circle(Point(375 + a, 250), 50)

    SmallEye1 = Circle(Point(250 + a, 250), 20)
    SmallEye2 = Circle(Point(350 + a, 250), 20)

    BigNose = Polygon(Point(300 + a,275), Point(250 + a, 325), Point(350 + a, 325))
    SmallNose = Polygon(Point(300 + a,275), Point(275 + a, 325), Point(325 + a, 325))

    HappyMouth = Rectangle(Point(250 + a, 375), Point(350 + a, 400))
    SadMouth = Line(Point(250 + a, 375), Point(350 + a, 375))

    Hair1 = Line(Point(350, 150), Point(350, 50))
    Hair2 = Line(Point(350, 150), Point(300, 75))
    Hair3 = Line(Point(350, 150), Point(400, 75))


    B = Button(win, Point(600, 100), Point(700, 175), "LightSteelBlue1", "Big eyes")
    B2 = Button(win, Point(600, 200), Point(700, 275), "LightSteelBlue1", "Small eyes")
    B3 = Button(win, Point(20, 100), Point(120, 175), "MistyRose2", "Big nose")
    B4 = Button(win, Point(20, 200), Point(120, 275), "MistyRose2", "Small nose")
    B5 = Button(win, Point(20, 300), Point(120, 375), "gold", "Closed mouth")
    B6 = Button(win, Point(20, 400), Point(120, 475), "gold", "Open mouth")
    B7 = Button(win, Point(20, 500), Point(120, 575), "plum4", "Hair")
    B8 = Button(win, Point(140, 500), Point(240, 575), "plum4", "Bald")

    Q = Button(win, Point(600, 300), Point(700, 375), "plum1", "QUIT")


    #takes in window name, two points of rectangle, color, text
    #button draws itself

    #for i in range(5): # or else only runs once
   
    while True:
        m = win.getMouse()
        if B.isClicked(m):
            BigEye1.undraw()
            BigEye2.undraw()
            
            SmallEye1.undraw()
            SmallEye2.undraw()
            
            BigEye1.draw(win)
            BigEye2.draw(win)

        if B2.isClicked(m):
            SmallEye1.undraw()
            SmallEye2.undraw()
            
            BigEye1.undraw()
            BigEye2.undraw()
            
            SmallEye1.draw(win)
            SmallEye2.draw(win)

        if B3.isClicked(m):
            BigNose.undraw()
            SmallNose.undraw()
            
            BigNose.draw(win)

        if B4.isClicked(m):
            BigNose.undraw()
            SmallNose.undraw()
            
            SmallNose.draw(win)

        if B5.isClicked(m):
            SadMouth.undraw()
            HappyMouth.undraw()
            
            SadMouth.draw(win)

        if B6.isClicked(m):
            SadMouth.undraw()
            HappyMouth.undraw()
            
            HappyMouth.draw(win)

        if B7.isClicked(m):
            Hair1.undraw()
            Hair2.undraw()
            Hair3.undraw()

            Hair1.draw(win)
            Hair2.draw(win)
            Hair3.draw(win)

        if B8.isClicked(m):
            Hair1.undraw()
            Hair2.undraw()
            Hair3.undraw()
     

        if Q.isClicked(m):
            break

    win.close()

    
if __name__ == "__main__":
    main()
