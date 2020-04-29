def listFrequency(wordList):
    frequencies = {}

    for wordInfo in wordList:
        frequencies = wordFrequency(wordInfo[0], frequencies)

    return getHighest(frequencies)

def wordFrequency(word, frequencyDict):
    for item in reversed(word): 
        frequencyDict[item] = frequencyDict.get(item, 0) + 1

    return frequencyDict

def getHighest(frequencyDict):
    count, itm = 0, '' 

    for item in frequencyDict:
        if frequencyDict[item] >= count : 
            count, itm = frequencyDict[item], item 
    return(itm) 
