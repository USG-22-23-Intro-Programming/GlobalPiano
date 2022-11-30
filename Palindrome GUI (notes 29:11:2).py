from graphics import*
from Button import*
import time

def main():

    win = GraphWin("palindrome", 800, 600)#window name, length, height
    win.setBackground("wheat1")
    '''
    wel = Text(Point(400, 250), "Welcome to the Palindrome-inator!")
    wel.draw(win)
    wel2 = Text(Point(400, 300), "Press the green button to continue")
    wel2.draw(win)
    Cont = Button(win, Point(350, 350), Point(450, 425), "PaleGreen", "Continue")
    '''
    Q = Button(win, Point(675, 500), Point(775, 575), "LavenderBlush2", "QUIT")
    Check = Button(win, Point(350, 350), Point(450, 425), "SteelBlue1", "Check")

    E = Entry(Point(400, 300), 50) #50 = width = how many characters
    E.draw(win)
    E.setSize(16)

    T = Text(Point(400, 250), "Write a potential palindrome below!")
    T.draw(win)
    Tru = Text(Point(400, 500), "It is a palindrome")
    Fal = Text(Point(400, 500), "It is not a palindrome")
    #T.setText("Not a palindrome")
    

    while True:
        m = win.getMouse()

        if Q.isClicked(m):
            break

        if Check.isClicked(m):
            pal = E.getText()
            length = len(pal)
            a = 0
            
            for i in range(length):
                if pal[i] == pal[length - 1 - i]:
                    a = a + 1

                if a == length:
                    
                    Tru.undraw()
                    Fal.undraw()
                    Tru.draw(win)
                else:
                    Tru.undraw()
                    Fal.undraw()
                    Fal.draw(win)
            
            

    win.close()

    
if __name__ == "__main__":
    main()
