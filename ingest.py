import json

def LoadNoDupes(path):
    wordList = []
    count = 0

    file = open(path,"r")

    print("( 0 ) + ", end = "")

    for word in file:
        count += 1
        word = word.upper()
        word = word.strip()
        if word not in wordList:
            wordList.append(word)

        if count % 100 == 0:
            print(".", end="")

        if count % 1000 == 0:
           print(" +", word, "\n(", count, ") + ", end = "")

    print("\n")
    return wordList

def GetInfo(inList):
    infoList = []
    count = 0

    print("( 0 ) + ", end = "")

    for word in inList:
        count += 1
        wordInfo = [word, len(word), uniqueChars(word)]
        infoList.append(wordInfo)

        if count % 100 == 0:
            print("-", end="")

        if count % 1000 == 0:
            print(" +", word, "\n(", count, ") + ", end = "")

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
