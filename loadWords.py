import json

def loadFromJSON(path, length):
    with open(path,"r") as json_file:
        data = json.load(json_file)

    return getWordsOfLength(data, length)

def getWordsOfLength(words, length):
    wordList = []

    for word in words:
        if word[1] == length:
            wordList.append(word)
        
        elif word[1] > length:
            break

    return wordList

print(loadFromJSON("finalWords.json", 1))