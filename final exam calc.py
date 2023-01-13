#calculates what grade you need on your final to get an A

def calc():
    print("chem, math, english, comsci, history, french, spanish")
    subj = input("what subject is this calculation for (choose from list above, capitalization matters: ")
    currG = input("what is your current grade: ")
    perc = {"chem" : 15, "math" : 15, "english" : 20, "comsci" : 20,
            "history" : 20, "french" : 15, "spanish" : 20}
    currG = int(currG)

    percG = perc.get(subj)

    percG = int(percG)

    percG = percG / 100

    perc1 = 1 - percG

    finalG = -(currG*perc1 - 93) / percG

    finalG = round(finalG, 1)

    finalG = str(finalG)
    

    print("you need a " + finalG + "% on your " + subj + " final to get an A.")

def main():
    calc()

if __name__ == "__main__":
    main()

    
    
    
