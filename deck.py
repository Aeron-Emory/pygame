import card

class deck:
    numOfCardTypes = 11
    numOfCards = 45
    cards = [None] * numOfCardTypes

    def __init__(self):
        self.cards = [card()] * self.numOfCardTypes
        self.setCards()
        self.initializeDeck()

    def setCards(self):
        for index in range(self.numOfCardTypes):
            if index == 0:
                self.cards[index].setLabel("1")
                self.cards[index].setOptionOne("Move one of your pawns forward one from START.")
                self.cards[index].setOptionTwo("If in play, move forward one space.")
                break
            elif index == 1:
                self.cards[index].setLabel("2")
                self.cards[index].setOptionOne("Move one of your pawns forward two from START.")
                self.cards[index].setOptionTwo("If in play, move forward two spaces.")
                break
            elif index == 2:
                self.cards[index].setLabel("3")
                self.cards[index].setOptionOne("Move one of your pawns forward three spaces.")
                self.cards[index].setOptionTwo("n/a")
                break
            elif index == 3:
                self.cards[index].setLabel("4")
                self.cards[index].setOptionOne("Move one of your pawns backward four spaces.")
                self.cards[index].setOptionTwo("n/a")
                break
            elif index == 4:
                self.cards[index].setLabel("5")
                self.cards[index].setOptionOne("Move one of your pawns forward five spaces.")
                self.cards[index].setOptionTwo("n/a")
                break
            elif index == 5:
                self.cards[index].setLabel("7")
                self.cards[index].setOptionOne("Move one of your pawns forward seven spaces.")
                self.cards[index].setOptionTwo("Split the forward move between two of your pawns.")
                break
            elif index == 6:
                self.cards[index].setLabel("8")
                self.cards[index].setOptionOne("Move one of your pawns forward eight spaces.")
                self.cards[index].setOptionTwo("n/a")
                break
            elif index == 7:
                self.cards[index].setLabel("10")
                self.cards[index].setOptionOne("Move one of your pawns forward ten spaces.")
                self.cards[index].setOptionTwo("Move one of your pawns backward one space.")
                break
            elif index == 8:
                self.cards[index].setLabel("11")
                self.cards[index].setOptionOne("Move one of your pawns forward 11 spaces.")
                self.cards[index].setOptionTwo("Switch any one of your pawns with an opponent's.")
                break
            elif index == 9:
                self.cards[index].setLabel("12")
                self.cards[index].setOptionOne("Move one of your pawns forward 12 spaces.")
                self.cards[index].setOptionTwo("n/a")
                break
            elif index == 10:
                self.cards[index].setLabel("SORRY!")
                self.cards[index].setOptionOne("Move a pawn from your start area to take the place of another player's pawn, which must return to its own start area.")
                self.cards[index].setOptionTwo("Move one of your pawns forward four spaces.")
                break
            else:
                break

    def getCard(self, cardNum):
        return self.pDeck[cardNum]

    def initializeDeck(self):
        self.pDeck = [card()] * self.numOfCards
        self.cardNum = 0
        for index in range(self.numOfCards):
            if index == 4:
                self.cardNum = 0
                break
            elif index == 8:
                self.cardNum = 1
                break
            elif index == 12:
                self.cardNum = 2
                break
            elif index == 16:
                self.cardNum = 3
                break
            elif index == 20:
                self.cardNum = 4
                break
            elif index == 24:
                self.cardNum = 5
                break
            elif index == 28:
                self.cardNum = 6
                break
            elif index == 32:
                self.cardNum = 7
                break
            elif index == 36:
                self.cardNum = 8
                break
            elif index == 40:
                self.cardNum = 9
                break
            elif index == 44:
                self.cardNum = 10
                break
            else:
                break
        self.pDeck[index].setLabel(self.cards[self.cardNum].getLabel())
        self.pDeck[index].setOptionOne(self.cards[self.cardNum].getOptionOne())
        self.pDeck[index].setOptionTwo(self.cards[self.cardNum].getOptionTwo())

    def printDeck(self):
        for index in range(self.numOfCards):
            print(self.pDeck[index].getLabel(), end="")
        print("")

    def shuffleDeck(self):
        import random
        switched = False
        randomCard = 0
        cardTrack = [] * self.numOfCards
        pNewDeck = [card()] * self.numOfCards
        for index in range(self.numOfCards):
            cardTrack[index] = 0
        for index in range(self.numOfCards):
            switched = False
            while switched == False:
                randomCard = random.randint(0, self.numOfCards - 1)
                if cardTrack[randomCard] == 0:
                    switched = True
                    cardTrack[randomCard] = 1
                    pNewDeck[index] = self.pDeck[randomCard]
        for index in range(self.numOfCards):
            self.pDeck[index].setLabel(pNewDeck[index].getLabel())
            self.pDeck[index].setOptionOne(pNewDeck[index].getOptionOne())
            self.pDeck[index].setOptionTwo(pNewDeck[index].getOptionTwo())