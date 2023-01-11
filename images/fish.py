from graphics import *
import random

class fish:

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

        self.body = Image(Point(self.location[0], self.location[1]), "fish.png")
        
        self.body.draw(win)


    def undraw(self):
        self.body.undraw()

    def randomMove(self, win):

        newCoords = []

        right = (self.location[0] + 20, self.location[1])
        left = (self.location[0] - 20, self.location[1])
        up = (self.location[0], self.location[1] - 20)
        down = (self.location[0], self.location[1] + 20)

        newCoords.append(right)
        newCoords.append(left)
        newCoords.append(up)
        newCoords.append(down)


        for movement in newCoords:
            if int(movement[0]) < 10 or int(movement[0]) > 390:
                newCoords.remove(movement)
            if int(movement[1]) < 10 or int(movement[1]) > 390:
                newCoords.remove(movement)

        self.location = random.choice(newCoords)
        self.body = Image(Point(self.location[0], self.location[1]), "fish.png")
        self.body.draw(win)

    def location(self):
        self.location

    def programmedMove(self, win):
        k = 1

        
        

        
        


        

        
        
    
