#Bryson Shane
#Project Status: Complete
#Program reads a file and counts total amount of spaces, upper and lower cases,
#and digits.


def process_file_data():
    #Intialize accumulator variables
    upperCaseTotal, lowerCaseTotal, digitsTotal, spaceTotal = 0, 0, 0 ,0

    openBook = open('abookpassage.txt', 'r') #opens file in read
    readBook = openBook.read() #reads entire file and stores it in string
    
    #Loops through entire string char by char checking for uppercase, lowercase
    #digits, and spaces.
    for char in readBook:
        if char.islower():
            lowerCaseTotal += 1
        elif char.isupper():
            upperCaseTotal += 1
        elif char.isdigit() :
            digitsTotal += 1
        elif char.isspace():
            spaceTotal += 1

    return upperCaseTotal, lowerCaseTotal, digitsTotal, spaceTotal

    openBook.close() #closes file to save data
    
   
