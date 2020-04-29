from wordSelection import listFrequency, removeIfDoesNotContain, removeIfDoesContain

def guess(wordList, guesses):
    nextGuess = listFrequency(wordList)
    guesses.append(nextGuess)

    print("I guess", nextGuess)
    correct = ""

    while correct.lower() != "y" and correct.lower() != "n":
        correct = input("\nWas this guess correct? [y/n] ")

    if correct.lower() == "y":
        wordList = removeIfDoesNotContain(wordList, nextGuess)
        print(wordList)

    else:
        wordList = removeIfDoesContain(wordList, nextGuess)
        print(wordList)

    return wordList, guesses