from graphics import *
import random

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
        self.x = self.location[0]
        self.y = self.location[1]

        self.body = Image(Point(self.x, self.y), "shark.png")
        
        self.body.draw(win)


        #Square = Rectangle(Point(self.location[0] - 120, self.location[1] - 120), Point(self.location[0] + 120, self.location[1] + 120))
        #Square.draw(win)


    def unDraw(self):
        self.body.undraw()
        
    def draw(self, win):
        self.body.draw(win)

    def location(self):
        self.location

    def movement(self, win, f1, f2, f3):

        #these determine the distance between the shark and each fish
        dis1 = abs(self.x - f1.location[0]) + abs(self.y - f1.location[1])
        dis2 = abs(self.x - f2.location[0]) + abs(self.y - f2.location[1])
        dis3 = abs(self.x - f3.location[0]) + abs(self.y - f3.location[1])

        #possible movements
        right = (20, 0)
        left = (-20, 0)
        up = (0, -20)
        down = (0, 20)

        newCoords = []

        #adds those movements' coords to list
        newCoords.append(right)
        newCoords.append(left)
        newCoords.append(up)
        newCoords.append(down)

        #checks for if the location is outside of the grid or not
        for movement in newCoords:
            if int(self.x + movement[0]) < 10 or int(self.x + movement[0]) > 390:
                newCoords.remove(movement)
            if int(self.y + movement[1]) < 10 or int(self.y + movement[1]) > 390:
                newCoords.remove(movement)

        chase = 1

        if self.location == f1.location:
            chase = 2
        if self.location == f2.location:
            chase = 3

        '''

        #chase 1
        #if the distance of shark1-fish1 is less than shark2-fish2 OR shark3-fish3
        if dis1 < dis2 or dis1 < dis3:
            chase = 1
        if dis1 == dis2 or dis1 == dis3:
            chase = 1
            
        #chase 2
        if dis2 < dis1 and dis2 < dis3:
            chase = 1
        if dis2 == dis3:
            chase = 1
            
        #chase 3
        if dis3 < dis2 and dis3 < dis1:
            chase = 1

        '''


        #x - 1
        k1 = f1.location[0] - self.location[0]
        #y - 1
        k2 = f1.location[1] - self.location[1]

        #x - 1
        kk1 = f2.location[0] - self.location[0]
        #y - 1
        kk2 = f2.location[1] - self.location[1]

        #x - 1
        kkk1 = f3.location[0] - self.location[0]
        #y - 1
        kkk2 = f3.location[1] - self.location[1]
        
        #chase fish 1
        if chase == 1:
            #move towards fish 1
            if k1 > 0:
                self.body.move(right[0], right[1])
                if k2 > 0:
                    self.body.move(down[0], down[1])
                elif k2 < 0:
                    self.body.move(up[0], up[1])
                else:
                    idkidk = 1
            elif k1 < 0:
                self.body.move(left[0], left[1])
                if k2 > 0:
                    self.body.move(down[0], down[1])
                elif k2 < 0:
                    self.body.move(up[0], up[1])
                else:
                    idkidk = 2

            else: #directly above / below. no side movements
                for i in range(2):
                    if k2 > 0:
                        self.body.move(down[0], down[1])
                    elif k2 < 0:
                        self.body.move(up[0], up[1])


        #chase fish 2
        if chase == 2:
            #move towards fish 2
            if kk1 > 0:
                self.body.move(right[0], right[1])
                if kk2 > 0:
                    self.body.move(down[0], down[1])
                elif k2 < 0:
                    self.body.move(up[0], up[1])
                else:
                    idkidk = 1
            elif kk1 < 0:
                self.body.move(left[0], left[1])
                if kk2 > 0:
                    self.body.move(down[0], down[1])
                elif kk2 < 0:
                    self.body.move(up[0], up[1])
                else:
                    idkidk = 2

            else: #directly above / below. no side movements
                for i in range(2):
                    if kk2 > 0:
                        self.body.move(down[0], down[1])
                    elif kk2 < 0:
                        self.body.move(up[0], up[1])
                        
        #chase fish 3
        if chase == 3:
            #move towards fish 3
            if kkk1 > 0:
                self.body.move(right[0], right[1])
                if kkk2 > 0:
                    self.body.move(down[0], down[1])
                elif k2 < 0:
                    self.body.move(up[0], up[1])
                else:
                    idkidk = 1
            elif kkk1 < 0:
                self.body.move(left[0], left[1])
                if kkk2 > 0:
                    self.body.move(down[0], down[1])
                elif kkk2 < 0:
                    self.body.move(up[0], up[1])
                else:
                    idkidk = 2

            else: #directly above / below. no side movements
                for i in range(2):
                    if kkk2 > 0:
                        self.body.move(down[0], down[1])
                    elif kkk2 < 0:
                        self.body.move(up[0], up[1])


'''

        #list of all possible movements of the shark
        
        sPosLoc = [(1, 0), (1, 1), (1, 2), (1, -1), (1, -2),
                              (2, 0), (2, -1), (2, 1),
                              (-1, 0), (-1, 1), (-1, 2), (-1, -1), (-1, -2),
                              (-2, 0), (-2, -1), (-2, 1),
                              (0, 1), (0, 2), (0, -1), (0, -2)]


        #removes coords outside of grid
        for locloc in sPosLoc:
            sNewX = self.x + locloc[0] *20
            sNewY = self.y + locloc[1] *20
            if sNewX > 390 or sNewX < 10:
                sPosLoc.remove(locloc)
            if sNewY > 390 or sNewY < 10:
                sPosLoc.remove(locloc)

        print(sPosLoc)

        

        #chase 1
        #if the distance of shark1-fish1 is less than shark2-fish2 AND shark3-fish3
        if dis1 < dis2 and dis1 < dis3:
            chase = 1
        if dis1 == dis2 or dis1 == dis3:
            chase = 1
            
        #chase 2
        if dis2 < dis1 and dis2 < dis3:
            chase = 1
        if dis2 == dis3:
            chase = 1
            
        #chase 3
        if dis3 < dis2 and dis3 < dis1:
            chase = 1

        
        #chase fish 1
        if chase == 1:
            
            possCoords = [] #list of possible coordinates from the list of movements within the grid
            print(possCoords)

            #gets the distance between the shark and the fish and the movement that makes it closer
            for locations in sPosLoc:
                xx1 = self.x + locations[0] *20
                yy1 = self.y + locations[1] *20
                closeX = abs(xx1 - f1.location[0]) 
                closeY = abs(yy1 - f1.location[1])
                possCoords.append((closeX, closeY))

            
            #sorts the list by the closest - furthest
            possCoords.sort()
            print(possCoords)

            #gets the  closest
            closestCoord = possCoords[0]
            xx = xx1
                
            yy = yy1
            

        #cannot both be greater than 2
        self.body = Image(Point(xx, yy), "shark.png")

        self.body.draw(win)
        

        
        dis1 = abs(self.location[0] - f1.location[0]) + abs(self.location[1] - f1.location[1])
        dis2 = abs(self.location[0] - f2.location[0]) + abs(self.location[1] - f2.location[1])
        dis3 = abs(self.location[0] - f3.location[0]) + abs(self.location[1] - f3.location[1])


        #CHANGE CHASE TO NORMAL LATER, THIS IS A TEST
        #fish one is closest
        if dis1 < dis2 and dis1 < dis3:
            chase = 1

        #fish two is closest
        if dis2 < dis1 and dis2 < dis3:
            chase = 2

        #fish three is closest
        if dis3 < dis2 and dis3 < dis1:
            chase = 3

        else:

            #if fish 1 = fish 2 or 3, go for 1
            if dis1 == dis2 or dis1 == dis3:
                chase = 1

            #if fish 2 = 3
            if dis3 == dis2:
                chase = 3

        #x - 1
        k1 = f1.location[0] - self.location[0]
        #y - 1
        k2 = f1.location[1] - self.location[1]

        #x - 2
        kk1 = f2.location[0] - self.location[0]
        #y - 2
        kk2 = f2.location[1] - self.location[1]


        #x - 2
        km1 = f3.location[0] - self.location[0]
        #y - 2
        km2 = f3.location[1] - self.location[1]

       
        #Notes for myself
        goDown = self.location[1] + 20
        goUp = self.location[1] - 20
        goRight = self.location[0] + 20
        goLeft = self.location[0] - 20

      


        if chase == 1:
            #move towards fish 1
            
            #fish is exactly diagonal
            if k1 == k2:
                #fish is right
                if k1 > 0:
                    #fish is below
                    if k2 > 0:
                        self.location[0] = self.location[0] + 20
                        self.location[1] = self.location[1] - 20
                    else:
                        self.location[0] = self.location[0] + 20
                        self.location[1] = self.location[1] + 20

                #fish is left
                else:
                    #fish is below
                    if k2 > 0:
                        self.location[0] = self.location[0] - 20
                        self.location[1] = self.location[1] - 20
                    else:
                        self.location[0] = self.location[0] - 20
                        self.location[1] = self.location[1] + 20
                    

            else:
                for i in range(2):
                    #fish is more to the side
                    if k1 > k2:
                        #fish is right
                        if k1 > 0:
                            self.location[0] = self.location[0] + 20
                        else:
                            self.location[0] = self.location[0] - 20
                    

                    #fish is more top/bottom
                    if k1 < k2:
                        #fish is below
                        if k2 > 0:
                            self.location[1] = self.location[1] + 20
                        else:
                            self.location[1] = self.location[1] - 20

        if chase == 2:
            #move towards fish 2

            #fish is exactly diagonal
            if kk1 == kk2:
                #fish is right
                if kk1 > 0:
                    #fish is below
                    if kk2 > 0:
                        self.location[0] = self.location[0] + 20
                        self.location[1] = self.location[1] - 20
                    else:
                        self.location[0] = self.location[0] + 20
                        self.location[1] = self.location[1] + 20

                #fish is left
                else:
                    #fish is below
                    if kk2 > 0:
                        self.location[0] = self.location[0] - 20
                        self.location[1] = self.location[1] - 20
                    else:
                        self.location[0] = self.location[0] - 20
                        self.location[1] = self.location[1] + 20
                    

            else:
                for i in range(2):
                    #fish is more to the side
                    if kk1 > kk2:
                        #fish is right
                        if kk1 > 0:
                            self.location[0] = self.location[0] + 20
                        else:
                            self.location[0] = self.location[0] - 20
                    

                    #fish is more top/bottom
                    if kk1 < kk2:
                        #fish is below
                        if kk2 > 0:
                            self.location[1] = self.location[1] + 20
                        else:
                            self.location[1] = self.location[1] - 20

        if chase == 3:
            #move towards fish 3

            #fish is exactly diagonal
            if km1 == km2:
                #fish is right
                if km1 > 0:
                    #fish is below
                    if km2 > 0:
                        self.location[0] = self.location[0] + 20
                        self.location[1] = self.location[1] - 20
                    else:
                        self.location[0] = self.location[0] + 20
                        self.location[1] = self.location[1] + 20

                #fish is left
                else:
                    #fish is below
                    if km2 > 0:
                        self.location[0] = self.location[0] - 20
                        self.location[1] = self.location[1] - 20
                    else:
                        self.location[0] = self.location[0] - 20
                        self.location[1] = self.location[1] + 20
                    

            else:
                for i in range(2):
                    #fish is more to the side
                    if km1 > km2:
                        #fish is right
                        if k1 > 0:
                            self.location[0] = self.location[0] + 20
                        else:
                            self.location[0] = self.location[0] - 20
                    

                    #fish is more top/bottom
                    if km1 < km2:
                        #fish is below
                        if km2 > 0:
                            self.location[1] = self.location[1] + 20
                        else:
                            self.location[1] = self.location[1] - 20
                            

        self.body = Image(Point(self.location[0], self.location[1]), "shark.png")
        self.body.draw(win)

'''


'''
        #fish 1 is closest
        if dis1 < dis2 and dis1 < dis3:
            self.body.undraw()
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
            self.body.undraw()
            
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
            self.body.undraw()
            
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
'''

        






        
    
