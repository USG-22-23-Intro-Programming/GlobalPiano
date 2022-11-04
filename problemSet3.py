
#1
def currencyConverter():

    currencies = ["1. USD", "2. Euro", "3. Chinese Yuan", "4. Turkish Lira"]
    forusercurr = {"1" : "USD", "2" : "Euro", "3" : "Chinese Yuan", "4" : "Turkish Lira"}
    forwantcurr = {"1" : "USD", "2" : "Euro", "3" : "Chinese Yuan", "4" : "Turkish Lira"}

    for currency in currencies:
        print(currency)
    usercurr = input("Choose your currency from the list above (in number): ")
    money = float(input("How much money do you have in that currency: "))
    for currency in currencies:
        print(currency)
    wantcurr = input("Choose the currency you want to convert into from the list above (in number): ")

    end = {"USD" : 1, "Euro" : .984, "Chinese Yuan" : 0.14, "Turkish Lira" : 0.054}
    end2 = {"USD" : 1, "Euro" : 1.02, "Chinese Yuan" : 7.29, "Turkish Lira" : 18.62}

    y = forusercurr.get(usercurr)
    rate = float(end.get(y))
    USD = money * rate
    
    getRate = forwantcurr.get(wantcurr)
    rate2 = float(end2.get(getRate))
    final = USD * rate2
    print(final)



#2

def groceryList(sample):

    foods = {"apple" : 1.50,
             "orange" : 1.00,
             "banana" : 1.00,
             "bagel" : 1.25,
             "cabbage" : 1.50,
             "spinach" : 4.25,
             "milk" : 2.75,
             "eggs" : 3.25,
             "cake" : 8.00,
             "pasta" : 3.50}
    print("You purchased:")
    for item in sample:
        print(item)
    money = 0
    for item in sample:
        x = foods.get(item)
        money = money + x
    print("Your total is: $" +str(money))


    




'''    #w = dict(w)

    
    #w = ["apple","orange", "banana", "bagel", "cabbage"]

    foods = {"apple" : 1.50,
             "orange" : 1.00,
             "banana" : 1.00,
             "bagel" : 1.25,
             "cabbage" : 1.50,
             "spinach" : 4.25,
             "milk" : 2.75,
             "eggs" : 3.25,
             "cake" : 8.00,
             "pasta" : 3.50}
    #m = {"apple" : 0, "banana" : 2, "cabbage" : 5}
    #w = m.get(w)

    #k = {"1.50" : "apple", "1.00" : "banana"}
    
    for i in range(len(w)):
        if w[0] == "apple":
            x = foods.get(*w)
            print(x)
        if w[0] == "banana":
            x = foods.get(*w)
            print(x)
        if w[1] == "apple":
            x = foods.get(*w)
            print(x)
        if w[1] == "banana":
            x = foods.get(*w)
            print(x)
        else:
            print("nope")



    #foods = list(foods)
    

    ###x = foods.get(*w)
    #for x in (foods):

       # foods = list(foods)
    
        #print(foods[len(foods)-1])
        #print("you purchased: " + foods)


'''

def main():
    #currencyConverter()
    L = ["apple", "banana", "spinach", "banana"]
    groceryList(L)

if __name__ == "__main__":
    main()
