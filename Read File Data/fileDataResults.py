import readFileData #imports the read file data module and allows you to get results

def main():
    resultsUpper, resultsLower, resultsDigits, resultsSpace = readFileData.process_file_data()
    #stores each returned value in a variable to display the results by calling
    #the readFileData module
    print(f'''Uppercase Letters: {resultsUpper}
Lowercase Letters: {resultsLower}
Digits: {resultsDigits}
Spaces: {resultsSpace}''')

main()
