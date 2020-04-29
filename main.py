from loadWords import loadFromJSON

lengthToGuess = input("What is the word lenght: ")

wordList = loadFromJSON("finalWords.json", lengthToGuess)