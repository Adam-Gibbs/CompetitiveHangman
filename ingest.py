
def LoadNoDupes():
    wordList = []

    file = open("wordListIn.txt","r")

    for word in file:
        word = word.upper()
        if word not in wordList:
            wordList.append(word)