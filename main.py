from loadWords import loadFromJSON
from guess import guess

end = False
guessList = []

lengthToGuess = int(input("What is the word length: "))
wordList = loadFromJSON("finalWords.json", lengthToGuess)
word = ["_"] * lengthToGuess

while end != True:
    wordList, guessList, word = guess(wordList, guessList, word)

    if "_" not in word:
        end = True
        break

print("The word is,", "".join(word))