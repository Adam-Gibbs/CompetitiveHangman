import json

def fileLen(path):
    with open(path) as f:
        for i, l in enumerate(f):
            pass
    return i + 1

def LoadNoDupes(path, length):
    wordList = []
    count = 0

    file = open(path,"r")

    print("( 0% ) + ", end = "")

    for word in file:
        count += 1
        word = word.upper()
        word = word.strip()
        if word not in wordList and "'" not in word:
            wordList.append(word)

        if count % 100 == 0:
            print(".", end="")

        if count % 1000 == 0:
           print(" +", word, "\n(", str(round((count/length)*100, 2)) + "% ) + ", end = "")

    print("\n")
    return wordList

def GetInfo(inList):
    length = len(inList)
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
            print(" +", word, "\n(", str(round((count/length)*100, 2)) + "% ) + ", end = "")

    print("\n")
    return infoList

def uniqueChars(inWord):
    charList = []

    for char in inWord:
        if char not in charList:
            charList.append(char)

    return len(charList)

def orderList(unorderedList):
    sortedList = unorderedList.sort(key=lambda element: element[1])
    return unorderedList

def writeToFile(inData):
    with open('sortedWords.json', 'w', encoding='utf-8') as f:
        json.dump(inData, f, ensure_ascii=False, indent=4)

def main():
    filePath = "unsorted.txt"
    writeToFile(orderList(GetInfo(LoadNoDupes(filePath, fileLen(filePath)))))

main()
