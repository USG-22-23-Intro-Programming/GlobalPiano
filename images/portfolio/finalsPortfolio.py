from Button import*
from graphics import*

from problemSet1 import*
from problemSet2 import*
from problemSet3 import*
from characterCreator import*
from imageEditor import*

def main():

#window
    win = GraphWin("Portfolio", 1000, 700)
    win.setBackground("#FFCDB4")

#draws a border of smiley faces  
    x = 13
    y = 13
    while x < 1000:
        smile = Image(Point(x,y), "smile.png") #it's 25x25
        smile.draw(win)
        x = x + 25
        
    x = 13
    y = 687
    while x < 1000:
        smile = Image(Point(x,y), "smile.png") #it's 25x25
        smile.draw(win)
        x = x + 25

    x = 13
    y = 13
    while y < 700:
        smile = Image(Point(x,y), "smile.png") #it's 25x25
        smile.draw(win)
        y = y + 25
        
    x = 987
    y = 13
    while y < 700:
        smile = Image(Point(x,y), "smile.png") #it's 25x25
        smile.draw(win)
        y = y + 25

#x just moves the whole thing up a bit cuz it was a bit off
    x = 50
#buttons
    PS1 = Button(win, Point(100, 100-x), Point(250, 200-x), "#F8B195", "Problem Set 1")
    PS2 = Button(win, Point(100, 225-x), Point(250, 325-x), "#F67280", "Problem Set 2")
    PS3 = Button(win, Point(100, 350-x), Point(250, 450-x), "#C06C84", "Problem Set 3")
    CC = Button(win, Point(100, 475-x), Point(250, 575-x), "#6C5B7B", "Character Creator")
    IE = Button(win, Point(100, 600-x), Point(250, 700-x), "#355C7D", "Image Editor")
    Q = Button(win, Point(900, 650), Point(975, 680), "#99B898", "Exit")

#text stuff
    
    t1 = Button(win, Point(325, 100-x), Point(850, 200-x), "#F8B195", "This file will greet you in the most polite manners, \n check if numbers are multiples of eachother, \n and check for palindromes!")
    t2 = Button(win, Point(325, 225-x), Point(850, 325-x), "#F67280", "Bonjour! This file finds factorials of numbers \n can double a phrase \n and automatically makes anything into Camel Code!")
    t3 = Button(win, Point(325, 350-x), Point(850, 450-x), "#C06C84", "Um... I think this file converts currencies\n and shows you grocery list and the final price!")
    t4 = Button(win, Point(325, 475-x), Point(850, 575-x), "#6C5B7B", "Creat a customized person here, however you want them \n with the great CHARACTER CREATOR!!!")
    t5 = Button(win, Point(325, 600-x), Point(850, 700-x), "#355C7D", "It does wonders to a beautiful picture of Mr.Considine's plant! \n Including grayscale, only red, contrast, lighten, and darken!")

#if buttons are pressed

    while True:
#each main() thing is the main() of that file
        m = win.getMouse()
        if PS1.isClicked(m):
            PS1main()
        if PS2.isClicked(m):
            PS2main()
        if PS3.isClicked(m):
            PS3main()
        if CC.isClicked(m):
            Cmain()
        if IE.isClicked(m):
            Imain()
        if Q.isClicked(m):
            break
    win.close()


if __name__ == "__main__":
    main()
