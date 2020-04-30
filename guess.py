from wordSelection import listFrequency, removeIfDoesNotContain, removeIfDoesContain

def guess(wordList, guesses):
    nextGuess = listFrequency(wordList, guesses)
    guesses.append(nextGuess)

    print("I guess", nextGuess)
    correct = ""

    while correct.lower() != "y" and correct.lower() != "n":
        correct = input("\nWas this guess correct? [y/n] ")

    if correct.lower() == "y":
        wordList = removeIfDoesNotContain(wordList, nextGuess)
        unknowns = input("How many spaces left to guess: ")

    else:
        wordList = removeIfDoesContain(wordList, nextGuess)
        unknowns = 1

    
    return wordList, guesses, int(unknowns)