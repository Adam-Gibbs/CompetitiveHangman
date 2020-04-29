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
  
print(getHighest(wordFrequency("Hello", {})))
