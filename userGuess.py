def userGuess(previousGuesses, compWord):
    print("It is now your turn to guess, the computer's word looks like the following: ")


    for letter in compWord:
        print(letter, end=" ")

    curGuess = input("\nWhat would you like to guess: ").upper()
    while curGuess in previousGuesses or not curGuess.isalpha():
        if not curGuess.isalpha():
            print("You must guess a letter, please guess again")
        
        else:
            print("You have guessed", curGuess, "before, please guess again")
        
        curGuess = input("What would you like to guess: ")

    previousGuesses.append(curGuess)

    return previousGuesses, compWord
