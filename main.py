from wordSelection import listFrequency
from loadWords import loadFromJSON

lengthToGuess = input("What is the word lenght: ")

wordList = loadFromJSON("finalWords.json", int(lengthToGuess))
print(listFrequency(wordList))
