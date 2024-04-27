def main():
    typeSentence = input('Enter the sentence you want to mess around with: ')
    newSentence = changeSentence(typeSentence)

    print(typeSentence)
    print(newSentence)

def changeSentence(getSentence):
    index = 0
    editSentence = ''

    while index < len(getSentence):
        if getSentence[index] == getSentence[index].upper():
            editSentence += getSentence[index].replace(getSentence[index].upper(), getSentence[index].lower())
            index += 1
        if getSentence[index] == getSentence[index].lower():
            editSentence += getSentence[index].replace(getSentence[index].lower(), getSentence[index].upper())
            index += 1
    return editSentence

main()
