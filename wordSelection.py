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
    count, itm = 0, '' 

    for item in frequencyDict:
        if frequencyDict[item] >= count and item not in previous: 
            count, itm = frequencyDict[item], item 

    if itm == '':
        itm = getNextUsedLetter(previous)

    return(itm) 

def getNextUsedLetter(used):
    common = ["e", "t", "a", "o", "i", "n", "s", "h", "r", "d", "l", "c", "u", "m", "w", "f", "g", "y", "p", "b", "v", "k", "j", "x", "q", "z", ""]

    for letter in common:
        if letter not in used:
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

    return inList

