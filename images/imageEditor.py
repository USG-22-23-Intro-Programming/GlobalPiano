from graphics import*
from Button import*



def main():

    win = GraphWin("Image Editor", 700, 600)
    win.setBackground("white")

    img = Image(Point(225, 300), "signpost.png")
    img.draw(win)

    Q = Button(win, Point(500, 450), Point(600, 525), "plum1", "QUIT")
    L = Button(win, Point(500, 50), Point(600, 125), "LightSteelBlue1", "Lighten")
    D = Button(win, Point(500, 150), Point(600, 225), "LightSteelBlue1", "Darken")
    C = Button(win, Point(500, 250), Point(600, 325), "MistyRose1", "Contrast")
    G = Button(win, Point(500, 350), Point(600, 425), "grey65", "Grayscale")

    while True:
        
        m = win.getMouse()

        if D.isClicked(m):
            darken(img)
        if L.isClicked(m):
            lighten(img)
        if C.isClicked(m):
            contrast(img)
        if G.isClicked(m):
            grayscale(img)
        if Q.isClicked(m):
            break
    win.close()


def grayscale(img):
    x=img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            P=img.getPixel(i,j)

            red = P[0]
            gre = P[1]
            blu = P[2]

            gray = float(red + gre + blu)
            gray = gray / 3
            gray = round(gray)

            red = gray
            blu = gray
            gre = gray

            c = color_rgb(red, gre, blu)
            img.setPixel(i, j, c)

            

def contrast(img):
    x=img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            P=img.getPixel(i,j)

            red = P[0]
            gre = P[1]
            blu = P[2]

            if (red + blu + gre < 337.5) or red + blu + gre == 337.5:
                if red - 25 > 0:
                    red = red - 25
                else:
                    red = 0

                if blu - 25 > 0:
                    blu = blu - 25
                else:
                    blu = 0
                
                if gre - 25 > 0:
                    gre = gre - 25
                else:
                    gre = 0
            else:
                if red + 25 < 255:
                    red = red + 25
                else:
                    red = 255

                if blu + 25 < 255:
                    blu = blu + 25
                else:
                    blu = 255
                
                if gre + 25 < 255:
                    gre = gre + 25
                else:
                    gre = 255
        

            c = color_rgb(red, gre, blu)
            img.setPixel(i, j, c)

def lighten(img):
    x=img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            P=img.getPixel(i,j)

            red = P[0]
            gre = P[1]
            blu = P[2]

            if red + 50 < 255:
                red = red + 50
            else:
                red = 255

            if blu + 50 < 255:
                blu = blu + 50
            else:
                blu = 255
                
            if gre + 50 < 255:
                gre = gre + 50
            else:
                gre = 255
        

            c = color_rgb(red, gre, blu)
            img.setPixel(i, j, c)


def darken(img):
    x=img.getWidth()
    y = img.getHeight()

    for i in range(x):
        for j in range(y):
            P=img.getPixel(i,j)

            red = P[0]
            gre = P[1]
            blu = P[2]

            if red - 50 > 0:
                red = red - 50
            else:
                red = 0

            if blu - 50 > 0:
                blu = blu - 50
            else:
                blu = 0
                
            if gre - 50 > 0:
                gre = gre - 50
            else:
                gre = 0
        

            c = color_rgb(red, gre, blu)
            img.setPixel(i, j, c)

#def reset(img)
    

if __name__ == "__main__":
    main()




