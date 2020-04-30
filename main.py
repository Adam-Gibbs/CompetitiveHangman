from loadWords import loadFromJSON
from guess import guess

end = False
guessList = []

lengthToGuess = input("What is the word lenght: ")
wordList = loadFromJSON("finalWords.json", int(lengthToGuess))

while end != True:
    wordList, guessList, unknownSpaces = guess(wordList, guessList)

    if unknownSpaces == 0:
        end = True

        break