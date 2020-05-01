def listFrequency(wordList, previous):
    frequencies = {}

    for wordInfo in wordList:
        frequencies = wordFrequency(wordInfo[0], frequencies)

    return getHighest(frequencies, previous)

def wordFrequency(word, frequencyDict):
    for item in reversed(word): 
        frequencyDict[item] = frequencyDict.get(item, 0) + 1

    return frequencyDict

def getHighest(frequencyDict, previous):
    count = 0
    itmList = [] 

    for item in frequencyDict:
        if frequencyDict[item] >= count and item not in previous: 
            itmLst = [item]
            count = frequencyDict[item]

        elif frequencyDict[item] == count and item not in previous:
            itmLst.append(item)

    if len(itmList) == 0:
        itm = getNextUnusedLetter(previous)

    elif len(itmList) > 1:
        itm = getMostCommon(itmList)

    elif len(itmList) == 1:
        itm = itmList[0]

    return(itm) 

def getNextUnusedLetter(used):
    common = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z", ""]

    for letter in common:
        if letter not in used:
            return letter

def getMostCommon(posLetters):
    common = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z"]

    for letter in common:
        for posLetter in posLetters:
            if posLetter == letter:
                return letter


def removeIfDoesContain(inList, letter):
    removeList = []

    for wordInfo in inList:
        for char in wordInfo[0]:
            if char == letter:
                removeList.append(wordInfo)
                break

    for item in removeList:
        inList.remove(item)

    return inList

def removeIfDoesNotContain(inList, letter, positions):
    removeList = []

    for wordInfo in inList:
        for position in positions:
            if wordInfo[0][position] != letter:
                removeList.append(wordInfo)
                break

    for item in removeList:
        inList.remove(item)

    return removeForOtherPositions(inList, letter, positions)
    

    
def removeForOtherPositions(inList, letter, positions):
    removeList = []

    for wordInfo in inList:
        for pos, char in enumerate(wordInfo[0]):
            if char == letter and pos not in positions:
                removeList.append(wordInfo)

    for item in removeList:
        inList.remove(item)

    return inList
