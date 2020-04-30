from wordSelection import listFrequency, removeIfDoesNotContain, removeIfDoesContain

def guess(wordList, guesses, word):
    nextGuess = listFrequency(wordList, guesses)
    guesses.append(nextGuess)

    print("I guess", nextGuess)
    correct = ""

    while correct.lower() != "y" and correct.lower() != "n":
        correct = input("\nWas this guess correct? [y/n] ")

    if correct.lower() == "y":
        spaces = int(input("How many times did it appear? "))

        positions = []
        for lopp in range(spaces):
            word, position = changeWord(word, nextGuess)
            positions.append(position)

        wordList = removeIfDoesNotContain(wordList, nextGuess, positions)

    else:
        wordList = removeIfDoesContain(wordList, nextGuess)

    return wordList, guesses, word

def changeWord(word, letter):
    printPositions(word)
    position = int(input("In what empty position did it appear? "))
    word, position = addToWord(position, word, letter)

    return word, position


def addToWord(position, word, letter):
    if word[position] == "_":
        word[position] = letter
    
    else:
        overwrite = input("This position already contains the letter", word[position], "are you sure you wish to overwrite it? [y/N]")

        if overwrite.lower() == "y":
            word[position] = letter

        else:
            word, position = changeWord(word, letter)
    
    return word, position

def printPositions(word):
    print("\nThe word is below, with positions shown beneath, ('_' means unkown letter)\n")

    for letter in word:
        print(letter, end=" ")

    print("\n")

    for index, letter in enumerate(word):
        print(index, end=" ")

    print("\n")
