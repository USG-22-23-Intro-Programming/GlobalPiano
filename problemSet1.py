#Greeting


'''def greeting ():
    name = input("Create your login username:")
    print("Oh goodness! If it isn't the great " + name + "!")
    print("What a honor to meet you, good sir!")'''

#IsMultiple!


def isMultiple (num1, num2):
    outcome = num1 % num2
    if outcome==0:
        print(str(num1) + " is a multiple of " + str(num2))
    else:
        print("Nope! " + str(num1) + " is not a multiple of " + str(num2))


#Palindrome
#Help

'''def palindrome():  
    x = int(input("enter a five digit number!"))
    if x[0] == x[len(x)-1]:
        print("it's a palindrome!")
    else:
        print("it isn't a palindrome :c") 

def main():
    palindrome()

if __name__ == "__main__":
    main()'''

def palindrome1():
    s = input("Type in a palindrome you want to test: ")

    length = len(s)

    #for loop to repeat
    #i starts at 0 and adds one each time

    for i in range(length):
        if s[i] == s[length - 1 - i]:
            return False
    return True

def main():
    #answer = palindrome1()
    #print(answer)

    isMultiple(10, 5)
    
if __name__ == "__main__":
    main()
        

#Googled:

'''num=int(input("Enter a number:"))
temp=num
rev=0
while(num>0):
    dig=num%10
    rev=rev*10+dig
    num=num//10
if(temp==rev):
    print("The number is palindrome!")
else:
    print("Not a palindrome!")'''









