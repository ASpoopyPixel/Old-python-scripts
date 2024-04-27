import random #imports random module so we can use the random function.

STARTINGLOOP = 1 #global constant for the starting value of the loop.

def writeFile():
    #tries all these variables for errors
    try:
        askForAmountOfNumbers = int(input('Enter the amount of numbers' +
                                      'you would like to write to the file: '))
    
        randomFile = open('random_numlist.txt', 'w')

        #loops user inputted amount of times and writes random numbers into
        #the file valued 1-500 
        for writeLine in range(STARTINGLOOP, askForAmountOfNumbers + 1):
            randomInt = random.randint(1, 500)
            randomFile.write(str(randomInt) + '\n')

        print('File is complete') #Lets user know the file was successfully written to.
        randomFile.close() 

    #if any error is occured this displays generic error message instead of crashing.
    except Exception as err:
        print(err)
    finally:
        randomFile.close() #closes the file after error has been displayed.

    
