from graphics import *
import random

class fish:

    def __init__(self, win):

        
        #empty list of all coords in grid
        listOfLocations = []

        
        x1 = 10
        y1 = 10

        #loop that adds all coords in the list (append)

        #for each x value
        while x1 <= 390:
            y1 = 10

            #for each y value
            while y1 <= 390:
                coords = (x1, y1)
                y1 = y1 + 20

                listOfLocations.append(coords)
            x1 = x1 + 20

        #sets its location to a random one within the list
        self.location = random.choice(listOfLocations)

        self.x = self.location[0]
        self.y = self.location[1]
        
        #draws fish with random location x and y ([0] and [1])
        self.body = Image(Point(self.location[0], self.location[1]), "fish.png")
        
        self.body.draw(win)


    def undraw(self):
        self.body.undraw()

    def randomMove(self, win):

        #empty list of possible coords to move to
        newCoords = []

        #possible movements
        right = (20, 0)
        left = (-20, 0)
        up = (0, -20)
        down = (0, 20)

        #adds those movements' coords to list
        newCoords.append(right)
        newCoords.append(left)
        newCoords.append(up)
        newCoords.append(down)

        #checks for if the location is outside of the grid or not
        for movement in newCoords:
            if int(self.x + movement[0]) < 10 or int(self.x + movement[0]) > 390:
                newCoords.remove(movement)
            elif int(self.y + movement[1]) < 10 or int(self.y + movement[1]) > 390:
                newCoords.remove(movement)



        #moves to a random location
        newLocation = random.choice(newCoords)
        self.body.move(newLocation[0], newLocation[1])

        #updates the location
        self.x = self.x + self.location[0]
        self.y = self.y + self.location[1]
        

    def location(self):
        self.location

    def programmedMove(self, win):
        k = 1
        #ugh

    def eaten(self):
        self.undraw()

        
        

        
        


        

        
        
    
