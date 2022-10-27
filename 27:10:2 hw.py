

#def factorial(num):

'''
def factorial(x):
    y = 1

    for i in range(2, x+1):
        y = y * i
    
        
    print("Its factorial is: " + str(y))


'''

'''
x=4, z= 3, y = 12

 for i in range(x - 1):
        z = (x - i - 1)
        for i in range(x):
            y = x * z

y1 = 1
y2 = 2
y3 = 6
y4 = 24
'''    

#Double it!

def doubleIt():
    l = input("double a phrase here: ")
    s=" "

    for i in l:
        s = s + i + i
        
    print(s)

'''
k = (input("Give me a word: "))

for i in range(len(k)):
    
    print(k.replace(k[i], k[i] + k[i]))


    newS2 = "   !qrekhgggggHEll0!wu  "
    newS2 = newS2.strip(" !qrekhgwu")
    print(newS2)
    
    #replaces all instances
    print(newS2.replace("l", "L"))
'''



#CamelCode

'''
def camelCode():

    cry = input(str("Enter file name:"))

    y = cry.title()
        
    a = y.replace(" ", "")

    b = a.replace("/", "-")

    c = b[0].lower() + b[1:]

    print(c)
'''



def main():
    #x = int(input("Give me a number: "))
    #factorial(x)

    #camelCode()

    doubleIt()

if __name__ == "__main__":
    main()




