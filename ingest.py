def LoadNoDupes(path):
    wordList = []

    file = open(path,"r")

    for word in file:
        word = word.upper()
        word = word.strip()
        if word not in wordList:
            wordList.append(word)

    print("\n")
    return wordList

def GetInfo(inList):
    infoList = []

    for word in inList:
        wordInfo = [word, len(word), uniqueChars(word)]
        infoList.append(wordInfo)

    return infoList

def uniqueChars(inWord):
    charList = []

    for char in inWord:
        if char not in charList:
            charList.append(char)

    return len(charList)

def main():
    filePath = "smallTest.txt"
    print(GetInfo(LoadNoDupes(filePath)))

main()
