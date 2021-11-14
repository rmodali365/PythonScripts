import random

def numberGuess():
    randNum = str(random.randint(0,1000))
    count = 0
    cow = 0
    bull = 0
    while True:
        input = input("Pick a number between 0 to 1000: ")
        if input==randNum:
            break
        else:
            for x in input:
                if randNum.find(x)!=-1:
                    bull = bull+1
                    
                
                    

                

