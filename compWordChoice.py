from loadWords import loadFromJSON
import itertools
import operator

class compWord:

    def __init__(self, length, wordList):
        self.word = ["_"]*length
        self.guesses = []
        self.posWords = wordList


    def checkCorrect(self, letter):
        correctPos = []
        incorrectNum = 0

        for word in self.posWords:
            positions = self._checkInWord(letter, word[0])
            if len(positions) == 0:
                incorrectNum += 1

            else:
                correctPos.append(positions)

        posCount, chosenPos = self._mostCommon(correctPos)

        if posCount >= incorrectNum:
            print("That is in the word, now it looks like this:")
            self._addToWord(letter, chosenPos)
            self._removeIfDoesNotContain(letter, chosenPos)

        else:
            print("\nthat is not in the word, it still looks like this:")
            self._removeIfDoesContain(letter)

        self.printWord()


    def _mostCommon(self, lst):
          # get an iterable of (item, iterable) pairs
        SL = sorted((x, i) for i, x in enumerate(lst))
        groups = itertools.groupby(SL, key=operator.itemgetter(0))
        group = groups
        # auxiliary function to get "quality" for an item

        def _auxfun(g):
            item, iterable = g
            count = 0
            min_index = len(lst)
            for _, where in iterable:
                count += 1
                min_index = min(min_index, where)
            return count, item

        groLst = []
        for gro in group:
            groLst.append(_auxfun(gro))

        # pick the highest-count/earliest item
        return self._getMaxAndCount(groLst)


    def _getMaxAndCount(self, lst):
        count = 0
        itm = [0, ""]

        for item in lst:

            if item[0] > count:
                count = item[0]
                itm = item

        return itm


    def _checkInWord(self, letter, word):
        positions = []

        for pos, char in enumerate(word):
            if char == letter:
                positions.append(pos)

        return positions


    def _addToWord(self, chr, positions):
        for pos in positions:
            self.word[pos] = chr


    def _removeIfDoesNotContain(self, letter, positions):
        removeList = []

        for wordInfo in self.posWords:
            for position in positions:
                if wordInfo[0][position] != letter:
                    removeList.append(wordInfo)
                    break

        for item in removeList:
            self.posWords.remove(item)

        self._removeForOtherPositions(letter, positions)        

    
    def _removeForOtherPositions(self, letter, positions):
        removeList = []

        for wordInfo in self.posWords:
            for pos, char in enumerate(wordInfo[0]):
                if char == letter and pos not in positions:
                    removeList.append(wordInfo)

        for item in removeList:
            self.posWords.remove(item)

    
    def _removeIfDoesContain(self, letter):
        removeList = []

        for wordInfo in self.posWords:
            for char in wordInfo[0]:
                if char == letter:
                    removeList.append(wordInfo)
                    break

        for item in removeList:
            self.posWords.remove(item)


    def printWord(self):
        for letter in self.word:
            print(letter, end=" ")



CompWord = compWord(4, wordList = loadFromJSON("finalWords.json", 4))
CompWord.printWord()
while True:
    CompWord.checkCorrect(input("\nWhat Letter: "))