#Bryson Shane
#Project Status: Complete
#Program writes user inputted amount of numbers to file that are random numbers 1-500
#Calculates the total value of all numbers and average

#imports custom module to write file
import write_random_num_file

def main():
    accumulateTotal = 0 #Adds the total all numbers in the file together
    countTotalNumbers = 0 #Counts the total numbers in the file
    calcAverage = 0

    #Tries all these variables for an error.
    try:
        write_random_num_file.writeFile() #Calls in the writefile function from write file module

        readFile = open('random_numlist.txt', 'r') #opens the file in read so we can read the content

        #Loops for the number lines in the file 
        for readLine in readFile:
            accumulateTotal += int(readLine)
            countTotalNumbers += 1
            print(readLine.rstrip('\n'))

        calcAverage = accumulateTotal/countTotalNumbers #defined later on to calculate avg.
        
        print('Your total value is:', accumulateTotal)
        print('Your total average is:', format(calcAverage,'.2f'))

        readFile.close() #closes file as we're finished

    #Gives generic Exception error message, if something goes wrong in the code
    except Exception as err:
        print(err)
    finally:
        readFile.close() #closes the file after displaying the error.
        
main()
