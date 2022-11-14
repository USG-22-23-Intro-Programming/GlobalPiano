
def main():
    

    #lists are like strings in that they hold a collection of elements
    #in a specific order. use brackets

    names = ["Ava", "Max", "Cayden", "Shuhua", "Nina", "Krystal"]
    #first element
    print(names[0])
    
    #second element
    print(names[1])

    #print last element
    print(names[len(names)-1])
    print(names[-1])

    #add an element to the end of the list
    names.append("Bae")
    print(names)

    #remove an element from the list, removes first one if there's multiple
    names.remove("Krystal")
    print(names)

    #removes an element even if there's multiple

    for i in range(len(names)):
        print(names[i])
                 

    #part 2

    names = ["A", "B", "C", "D", "E"]

    for i in range(len(names)):
        print(names[i])

    #for each loop
    for name in names: #this defines name as each string in names
        if name == "A":
            print("A is absent today")
        else:
            print("No one likes you, " + name)

    #get index (position) of an element in a list

    print(names.index("B"))
    print(names.index("D"))



#Zoo

class Zoo():
    
    def __init__(self): #define constructor method
    
        self.animals = ["Tiger", "Bear", "Monkey", "Leopard"]
        self.habitats = ["Plains", "Forest", "Jungle", "Amazon Basin"]

    def getAnimal(self, pos):

        return self.animals[pos]
    
#DO IT YOURSELF

    #def getHabitat(self, animal):
       
        

    #def getAnimalFromHome(self, habitat):


        

def method():
    z = Zoo()
    animal = "Tiger"
    print("The" + animal + "lives in the" + z.getHabitat(animal))


    
if __name__ == "__main__":
    #main()
    method()




'''
QUIZ!

Idle

given skeleton code:
main(), def q1() as methods, def q2() as methods, comments - describe each question
q = questions

No internet

Mini problem set


example:
    create a method which takes in an integer as parameter and returns output as the square of the integer

    create a method that asks the user to input their name and a number, and prints the name that number of times

    create a method which takes in three numbers as parameters and prints out the average of the three numbers




