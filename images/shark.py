from graphics import *
import random
from fish import *

class shark:

    def __init__(self, win):

        listOfLocations = []

        
        x1 = 10
        y1 = 10

        while x1 <= 390:
            y1 = 10

            while y1 <= 390:
                coords = (x1, y1)
                y1 = y1 + 20

                listOfLocations.append(coords)
            x1 = x1 + 20
        
        self.location = random.choice(listOfLocations)

        self.body = Image(Point(self.location[0], self.location[1]), "shark.png")
        
        self.body.draw(win)

        #Square = Rectangle(Point(self.location[0] - 120, self.location[1] - 120), Point(self.location[0] + 120, self.location[1] + 120))
        #Square.draw(win)


    def undraw(self):
        self.body.undraw()

    def movement(self, win, f1, f2, f3):
        dis1 = abs(self.location[0] - f1.location[0]) + abs(self.location[1] - f1.location[1])
        dis2 = abs(self.location[0] - f2.location[0]) + abs(self.location[1] - f2.location[1])
        dis3 = abs(self.location[0] - f3.location[0]) + abs(self.location[1] - f3.location[1])


        #fish 1 is closest
        if dis1 < dis2 and dis1 < dis3:
            #x
            k1 = f1.location[0] - self.location[0]
            #y
            k2 = f1.location[1] - self.location[1]

            ccc = 0
            
            for i in range(2):
                kkk = 0

                
                #x is closer
                if abs(k1) < abs(k2) and kkk == 0:
                    #fish is below
                    if k2 > 0:
                        self.body = Image(Point(self.location[0] , self.location[1] + 20), "shark.png")
                    #fish is above
                    if k2 < 0:
                        self.body = Image(Point(self.location[0] , self.location[1] - 20), "shark.png")

                        
                #y is closer
                if abs(k1) > abs(k2) and kkk == 0:
                    #fish is right
                    if k1 > 0:
                        self.body = Image(Point(self.location[0] + 20, self.location[1]), "shark.png")
                    #fish is left
                    if k1 < 0:
                        self.body = Image(Point(self.location[0] - 20, self.location[1]), "shark.png")


                if (abs(k1) == abs(k2)) and (ccc == 0) and (k1 != 0) and kkk == 0:
                    ccc = 1
                    #fish is right
                    if k1 > 0:
                        
                        #fish is below
                        if k2 > 0:
                            self.body = Image(Point(self.location[0] + 20, self.location[1] + 20), "shark.png")

                        #fish is above
                        if k2 < 0:
                            self.body = Image(Point(self.location[0] + 20, self.location[1] - 20), "shark.png")

                    #fish is left
                    if k1 < 0:
                        
                        #fish is below
                        if k2 > 0:
                            self.body = Image(Point(self.location[0] -20, self.location[1] + 20), "shark.png")

                        #fish is above
                        if k2 < 0:
                            self.body = Image(Point(self.location[0] -20, self.location[1] - 20), "shark.png")

            self.body.draw(win)
                    
                    

            ccc = 0

        if dis2 < dis1 and dis1 < dis3:
            #SHARK MOVE TOWARDS F2
            
            #x
            kk1 = f2.location[0] - self.location[0]
            #y
            kk2 = f2.location[1] - self.location[1]

            ccc = 0
            
            for i in range(2):
                kkk = 0

                
                #x is closer
                if abs(kk1) < abs(kk2) and kkk == 0:
                    #fish is below
                    if kk2 > 0:
                        self.body = Image(Point(self.location[0] , self.location[1] + 20), "shark.png")
                    #fish is above
                    if kk2 < 0:
                        self.body = Image(Point(self.location[0] , self.location[1] - 20), "shark.png")

                        
                #y is closer
                if abs(kk1) > abs(kk2) and kkk == 0:
                    #fish is right
                    if kk1 > 0:
                        self.body = Image(Point(self.location[0] + 20, self.location[1]), "shark.png")
                    #fish is left
                    if kk1 < 0:
                        self.body = Image(Point(self.location[0] - 20, self.location[1]), "shark.png")


                if (abs(kk1) == abs(kk2)) and (ccc == 0) and (kk1 != 0) and kkk == 0:
                    ccc = 1
                    #fish is right
                    if kk1 > 0:
                        
                        #fish is below
                        if kk2 > 0:
                            self.body = Image(Point(self.location[0] + 20, self.location[1] + 20), "shark.png")

                        #fish is above
                        if kk2 < 0:
                            self.body = Image(Point(self.location[0] + 20, self.location[1] - 20), "shark.png")

                    #fish is left
                    if kk1 < 0:
                        
                        #fish is below
                        if kk2 > 0:
                            self.body = Image(Point(self.location[0] -20, self.location[1] + 20), "shark.png")

                        #fish is above
                        if kk2 < 0:
                            self.body = Image(Point(self.location[0] -20, self.location[1] - 20), "shark.png")

            self.body.draw(win)
                    
                    

            ccc = 0

        if dis3 < dis2 and dis3 < dis1:
            #SHARK MOVE TOWARDS F3
            
            #x
            ke1 = f3.location[0] - self.location[0]
            #y
            ke2 = f3.location[1] - self.location[1]

            ccc = 0
            
            for i in range(2):
                kkk = 0

                
                #x is closer
                if abs(ke1) < abs(ke2) and kkk == 0:
                    #fish is below
                    if ke2 > 0:
                        self.body = Image(Point(self.location[0] , self.location[1] + 20), "shark.png")
                    #fish is above
                    if ke2 < 0:
                        self.body = Image(Point(self.location[0] , self.location[1] - 20), "shark.png")

                        
                #y is closer
                if abs(ke1) > abs(ke2) and kkk == 0:
                    #fish is right
                    if ke1 > 0:
                        self.body = Image(Point(self.location[0] + 20, self.location[1]), "shark.png")
                    #fish is left
                    if ke1 < 0:
                        self.body = Image(Point(self.location[0] - 20, self.location[1]), "shark.png")


                if (abs(ke1) == abs(ke2)) and (ccc == 0) and (ke1 != 0) and kkk == 0:
                    ccc = 1
                    #fish is right
                    if ke1 > 0:
                        
                        #fish is below
                        if ke2 > 0:
                            self.body = Image(Point(self.location[0] + 20, self.location[1] + 20), "shark.png")

                        #fish is above
                        if ke2 < 0:
                            self.body = Image(Point(self.location[0] + 20, self.location[1] - 20), "shark.png")

                    #fish is left
                    if ke1 < 0:
                        
                        #fish is below
                        if ke2 > 0:
                            self.body = Image(Point(self.location[0] -20, self.location[1] + 20), "shark.png")

                        #fish is above
                        if ke2 < 0:
                            self.body = Image(Point(self.location[0] -20, self.location[1] - 20), "shark.png")

            self.body.draw(win)
                    
                    

            ccc = 0

def undraw(self):
    self.body.undraw()
        






        
    
