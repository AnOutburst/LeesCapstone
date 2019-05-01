
#I DID NOT CREATE THIS MODULE. I JUST THOUGHT IT WOULD BE FUN TO ADD SINCE YOU CANT HAVE WINDOWS 95 W/O SOLITAIRE
#The github repo can be found here for this project https://gist.github.com/artexercise/814446dc03189b5e41d7d04568254597
#I claim no ownership of the code in this file

__author__ = "jjeskiewicz"
import random, sys

class Solitaire:
    def __init__(self, master):
        self.gameDeck = DeckOfCards()
        self.o_A = tableauPile()
        self.o_B = tableauPile()
        self.o_C = tableauPile()
        self.o_D = tableauPile()
        self.o_E = tableauPile()
        self.o_F = tableauPile()
        self.o_G = tableauPile()
        self.tableau = [self.o_A, self.o_B, self.o_C, self.o_D, self.o_E, self.o_F, self.o_G]
        self.o_heartGoal = goalPile(Suit.Heart)
        self.o_diamondGoal = goalPile(Suit.Diamond)
        self.o_spadeGoal = goalPile(Suit.Spade)
        self.o_clubGoal = goalPile(Suit.Club)
        self.o_draw = drawPile()
        self.o_discard = discardPile()
        self.o_temp = transaction(None)
        self.dealCards()
        self.coffeeCard = Card("Coffee", Suit.Blank, 0, "__")
        self.buttonCoffeeCard = Card("Coffee", Suit.Blank, 0, "ZZZzzz...")
        self.milkCard = Card("Milk", Suit.Milk, 0, ".")
        self.gameTopRow = 2  # for Grid Layout

        self.gameFrame = Frame(master, height=480, width=640, bg="White")
        self.gameFrame.pack()

        # Obligatory Game Label
        Label(self.gameFrame, text="SOLITAIRE - KLONDIKE", bg="White").grid(row=0, column=0, columnspan=15)
        self.returnCardLabel(self.buttonCoffeeCard, self.gameFrame).grid(row=1, column=0)
        for x in range(1, 14):
            self.returnCardLabel(self.coffeeCard, self.gameFrame).grid(row=1, column=x)
        for x in range(14, 16):
            self.returnCardLabel(self.buttonCoffeeCard, self.gameFrame).grid(row=1, column=x)

        # ***** ***** ***** ***** *****
        # Set up Tableau Buttons
        self.gB_A = Button(self.gameFrame, text="Select", name="_A", command=self.changeButtonA)
        self.gB_B = Button(self.gameFrame, text="Select", name="_B", command=self.changeButtonB)
        self.gB_C = Button(self.gameFrame, text="Select", name="_C", command=self.changeButtonC)
        self.gB_D = Button(self.gameFrame, text="Select", name="_D", command=self.changeButtonD)
        self.gB_E = Button(self.gameFrame, text="Select", name="_E", command=self.changeButtonE)
        self.gB_F = Button(self.gameFrame, text="Select", name="_F", command=self.changeButtonF)
        self.gB_G = Button(self.gameFrame, text="Select", name="_G", command=self.changeButtonG)
        self.tableauButtons = [self.gB_A, self.gB_B, self.gB_C, self.gB_D, self.gB_E, self.gB_F, self.gB_G]

        # Set up Tableau Cards
        self.gL_A = self.returnCardLabel(self.o_A.getTopCard(), self.gameFrame)
        self.gL_B = self.returnCardLabel(self.o_B.getTopCard(), self.gameFrame)
        self.gL_C = self.returnCardLabel(self.o_C.getTopCard(), self.gameFrame)
        self.gL_D = self.returnCardLabel(self.o_D.getTopCard(), self.gameFrame)
        self.gL_E = self.returnCardLabel(self.o_E.getTopCard(), self.gameFrame)
        self.gL_F = self.returnCardLabel(self.o_F.getTopCard(), self.gameFrame)
        self.gL_G = self.returnCardLabel(self.o_G.getTopCard(), self.gameFrame)
        self.tableauCards = [self.gL_A, self.gL_B, self.gL_C, self.gL_D, self.gL_E, self.gL_F, self.gL_G]

        # Tableau Other
        self.gL_AStack = [self.gL_A]
        self.gL_BStack = [self.gL_B]
        self.gL_CStack = [self.gL_C]
        self.gL_DStack = [self.gL_D]
        self.gL_EStack = [self.gL_E]
        self.gL_FStack = [self.gL_F]
        self.gL_GStack = [self.gL_G]
        for xcol in range(2, 14):
            aLabel = self.returnCardLabel(self.milkCard, self.gameFrame)
            aLabel.grid(row=2, column=xcol)
            self.gL_AStack.append(aLabel)
            bLabel = self.returnCardLabel(self.milkCard, self.gameFrame)
            bLabel.grid(row=3, column=xcol)
            self.gL_BStack.append(bLabel)
            cLabel = self.returnCardLabel(self.milkCard, self.gameFrame)
            cLabel.grid(row=4, column=xcol)
            self.gL_CStack.append(cLabel)
            dLabel = self.returnCardLabel(self.milkCard, self.gameFrame)
            dLabel.grid(row=5, column=xcol)
            self.gL_DStack.append(dLabel)
            eLabel = self.returnCardLabel(self.milkCard, self.gameFrame)
            eLabel.grid(row=6, column=xcol)
            self.gL_EStack.append(eLabel)
            fLabel = self.returnCardLabel(self.milkCard, self.gameFrame)
            fLabel.grid(row=7, column=xcol)
            self.gL_FStack.append(fLabel)
            gLabel = self.returnCardLabel(self.milkCard, self.gameFrame)
            gLabel.grid(row=8, column=xcol)
            self.gL_GStack.append(gLabel)

        # Set up Goal Buttons
        self.gB_Spades = Button(self.gameFrame, text="Place", command=self.placeSpade)
        self.gB_Hearts = Button(self.gameFrame, text="Place", command=self.placeHeart)
        self.gB_Clubs = Button(self.gameFrame, text="Place", command=self.placeClub)
        self.gB_Diamonds = Button(self.gameFrame, text="Place", command=self.placeDiamond)
        self.goalButtons = [self.gB_Spades, self.gB_Hearts, self.gB_Clubs, self.gB_Diamonds]

        # Set up Goal Spots
        self.gL_Spades = self.returnGoalLabel(self.o_spadeGoal.getTopCard(), Suit.Spade, self.gameFrame)
        self.gL_Hearts = self.returnGoalLabel(self.o_heartGoal.getTopCard(), Suit.Heart, self.gameFrame)
        self.gL_Clubs = self.returnGoalLabel(self.o_clubGoal.getTopCard(), Suit.Club, self.gameFrame)
        self.gL_Diamonds = self.returnGoalLabel(self.o_diamondGoal.getTopCard(), Suit.Diamond, self.gameFrame)
        self.goalCards = [self.gL_Spades, self.gL_Hearts, self.gL_Clubs, self.gL_Diamonds]

        # Set up Discard Spot
        Label(self.gameFrame, text="Discard", bg="White").grid(row=self.gameTopRow, column=14)
        self.gB_Discard = Button(self.gameFrame, text="Select", command=self.onClick_gB_Discard)
        self.gL_Discard = self.returnGoalLabel(self.o_discard.getTopCard(), Suit.Blank, self.gameFrame)

        # Set up Draw Spot
        Label(self.gameFrame, text="Draw Pile", bg="White").grid(row=self.gameTopRow, column=15)
        self.gB_Draw = Button(self.gameFrame, text="Draw", command=self.onClick_gB_Draw)

        # ***** ***** ***** ***** *****
        # Place Tableau Buttons
        bCount = self.gameTopRow
        for b in self.tableauButtons:
            b.grid(row=bCount, column=0)
            bCount = bCount + 1

        # Place Tableau Cards
        cCount = self.gameTopRow
        for c in self.tableauCards:
            c.grid(row=cCount, column=1)
            cCount = cCount + 1

        # Place Goal Buttons
        gCount = self.gameTopRow + 3
        for g in self.goalButtons:
            g.grid(row=gCount, column=15)
            gCount = gCount + 1

        # Place Goal Spots
        gcCount = self.gameTopRow + 3
        for gc in self.goalCards:
            gc.grid(row=gcCount, column=14)
            gcCount = gcCount + 1

        # Place Discard Spot
        self.gB_Discard.grid(row=(self.gameTopRow + 1), column=14)
        self.gL_Discard.grid(row=(self.gameTopRow + 2), column=14)

        # Place Draw Spot
        self.gB_Draw.grid(row=(self.gameTopRow + 1), column=15)

        # ***** ***** ***** ***** *****
        # Assign Discard Buttons to Object
        self.o_discard.button = self.gB_Discard
        self.o_discard.label = self.gL_Discard

        # Assign Draw Buttons to Object
        self.o_draw.button = self.gB_Draw

        # Assign Tableau Cards
        self.o_A.button = self.gB_A
        self.o_B.button = self.gB_B
        self.o_C.button = self.gB_C
        self.o_D.button = self.gB_D
        self.o_E.button = self.gB_E
        self.o_F.button = self.gB_F
        self.o_G.button = self.gB_G
        self.o_A.label = self.gL_A
        self.o_B.label = self.gL_B
        self.o_C.label = self.gL_C
        self.o_D.label = self.gL_D
        self.o_E.label = self.gL_E
        self.o_F.label = self.gL_F
        self.o_G.label = self.gL_G
        self.o_A.labelStack = self.gL_AStack
        self.o_B.labelStack = self.gL_BStack
        self.o_C.labelStack = self.gL_CStack
        self.o_D.labelStack = self.gL_DStack
        self.o_E.labelStack = self.gL_EStack
        self.o_F.labelStack = self.gL_FStack
        self.o_G.labelStack = self.gL_GStack

        # Assign Goal Spots
        self.o_spadeGoal.button = self.gB_Spades
        self.o_heartGoal.button = self.gB_Hearts
        self.o_clubGoal.button = self.gB_Clubs
        self.o_diamondGoal.button = self.gB_Diamonds
        self.o_spadeGoal.label = self.gL_Spades
        self.o_heartGoal.label = self.gL_Hearts
        self.o_clubGoal.label = self.gL_Clubs
        self.o_diamondGoal.label = self.gL_Diamonds

        # Do I Need a Transaction Space For Player to See Cards or just figure out how to higlight cells.
        # Label(self.gameFrame, text="Current Transaction").grid(row=self.gameTopRow+7, column=0, columnspan=5)
        # self.gL_TransactionLabel = Label(self.gameFrame, text="AB")
        # self.gL_TransactionLabel.grid(row=self.gameTopRow+7, column=6, columnspan=10)

    # ACTIONS
    def returnCardLabel(self, card, frame):
        return Label(frame, text=u"{0}{1} ".format(card.letter, card.symbol), fg=card.color, bg="White")

    def returnGoalLabel(self, card, suit, frame):
        if card is not None:
            return Label(frame, text=u"{0}{1} ".format(card.letter, card.symbol), fg=card.color, bg="White")
        else:
            suitCard = Card("Blank", suit, 0, ".")
            return Label(frame, text=u"{0} ".format(suitCard.symbol), fg=suitCard.color, bg="White")

    # ***** ***** ***** ***** *****
    # Populate Goals
    # ***** ***** ***** ***** *****
    def placeSpade(self):
        self.goalTransaction(self.o_spadeGoal)

    def placeHeart(self):
        self.goalTransaction(self.o_heartGoal)

    def placeClub(self):
        self.goalTransaction(self.o_clubGoal)

    def placeDiamond(self):
        self.goalTransaction(self.o_diamondGoal)

    def goalTransaction(self, o_suitGoal):
        # Did we just hit a Place Button for no reason?
        if self.o_temp.status == TransactionStatus.Closed:
            return False

        # Set the Destination
        self.o_temp.travelTo = o_suitGoal

        # Can the Transaction Happen
        if self.o_temp.validate(Stack.Foundation):
            # Perform the Transaction
            self.o_temp.performTransaction(Stack.Foundation)
            self.o_temp.closeTransaction()
            self.gui_closeTransaction()
            self.gui_Refresh()

    def updateFoundationLabel(self, aCardStack):
        aCard = Card("Blank", aCardStack.suit, 0, ".") if len(aCardStack.cards) == 0 else aCardStack.cards[
            len(aCardStack.cards) - 1]
        if len(aCardStack.cards) == 0:
            labelPrep = u"{0} ".format(aCard.symbol)
        else:
            labelPrep = u"{0}{1} ".format(aCard.letter, aCard.symbol)
        aCardStack.label["text"] = labelPrep
        aCardStack.label["fg"] = aCard.color
        aCardStack.label["bg"] = Color.White

    # ***** ***** ***** ***** *****
    # Draw a New Card Click
    # ***** ***** ***** ***** *****
    def onClick_gB_Draw(self):
        """
        Move from drawStack to discardStack
        Version 1 is 1 at a time.
        """
        # If attempting a Transaction, disable
        if self.o_temp.status == TransactionStatus.Open:
            return False

        # If Draw Stack is empty, replenish from the Discard Pile
        countDrawStack = len(self.o_draw.cards)
        if countDrawStack == 0:
            self.o_draw.cards = self.o_discard.cards[::-1]
            self.o_discard.cards = []

        # Move top of Draw Pile to Discard
        if len(self.o_draw.cards) > 0:
            self.o_discard.cards.append(self.o_draw.cards.pop())

        # UPDATE GUI
        self.gui_Refresh()

    # ***** ***** ***** ***** *****
    # Discard Button Click
    # ***** ***** ***** ***** *****
    def onClick_gB_Discard(self):
        if self.o_discard.button["text"] == "Select":
            self.select_gB_Discard()
        elif self.o_discard.button["text"] == "Cancel":
            self.o_temp.closeTransaction()
            self.gui_closeTransaction()

    def select_gB_Discard(self):
        # Ignore if there are no cards
        if len(self.o_discard.cards) == 0:
            return False

        # make a Transaction
        self.o_temp = transaction(self.o_discard)
        self.o_temp.makeTransaction(1)

        # Alter GUI Buttons
        self.gui_openTransaction(self.gB_Discard)
        self.o_discard.label["bg"] = "Yellow"

    # ***** ***** ***** ***** *****
    # Select Tableau Card
    # ***** ***** ***** ***** *****
    def changeButtonA(self):
        self.onClick_Button(self.o_A)

    def changeButtonB(self):
        self.onClick_Button(self.o_B)

    def changeButtonC(self):
        self.onClick_Button(self.o_C)

    def changeButtonD(self):
        self.onClick_Button(self.o_D)

    def changeButtonE(self):
        self.onClick_Button(self.o_E)

    def changeButtonF(self):
        self.onClick_Button(self.o_F)

    def changeButtonG(self):
        self.onClick_Button(self.o_G)

    def onClick_Button(self, o_Stack):
        if o_Stack.button["text"] == "Select":
            self.select_gB_ButtonX(o_Stack)
        elif o_Stack.button["text"] == "Place":
            self.place_gB_ButtonX(o_Stack)
        else:  # Cancel
            self.o_temp.closeTransaction()
            self.gui_closeTransaction()

    def select_gB_ButtonX(self, o_Stack):
        # Ignore if there are no cards
        if len(o_Stack.cards) == 0:
            return False

        # make a Transaction
        self.o_temp = transaction(o_Stack)
        self.o_temp.makeTransaction(o_Stack.movingcards)

        # Alter GUI Buttons
        self.gui_openTransaction(o_Stack.button)
        o_Stack.label["bg"] = "Yellow"
        pass

    def place_gB_ButtonX(self, o_Stack):
        # Set the Destination
        self.o_temp.travelTo = o_Stack

        # Can the Transaction Happen
        if self.o_temp.validate(Stack.Tableau):
            # Perform the Transaction
            self.o_temp.performTransaction(Stack.Tableau)
            self.o_temp.closeTransaction()
            self.gui_closeTransaction()
            self.gui_Refresh()

    def changeButton(self, aButton):
        if aButton["text"] == "Place":
            aButton.config(text="Select")
        else:
            aButton.config(text="Place")

    def gui_openTransaction(self, fromButton):
        self.gB_A["text"] = "Cancel" if fromButton is self.gB_A else "Place"
        self.gB_B["text"] = "Cancel" if fromButton is self.gB_B else "Place"
        self.gB_C["text"] = "Cancel" if fromButton is self.gB_C else "Place"
        self.gB_D["text"] = "Cancel" if fromButton is self.gB_D else "Place"
        self.gB_E["text"] = "Cancel" if fromButton is self.gB_E else "Place"
        self.gB_F["text"] = "Cancel" if fromButton is self.gB_F else "Place"
        self.gB_G["text"] = "Cancel" if fromButton is self.gB_G else "Place"
        self.gB_Discard["text"] = "Cancel" if fromButton is self.gB_Discard else "Select"

    def gui_closeTransaction(self):
        self.gB_A["text"] = "Select"
        self.gB_B["text"] = "Select"
        self.gB_C["text"] = "Select"
        self.gB_D["text"] = "Select"
        self.gB_E["text"] = "Select"
        self.gB_F["text"] = "Select"
        self.gB_G["text"] = "Select"
        self.gB_Discard["text"] = "Select"

    def gui_Refresh(self):
        # Automove a card to Foundation Then call Gui Refresh to do it again
        # Check Discard
        if True:
            if len(self.o_discard.cards) > 0:
                self.autoMoveToFoundation(self.o_discard)
        # Check Tableau
        if True:
            for stack in self.tableau:
                if len(stack.cards) > 0:
                    self.autoMoveToFoundation(stack)

        # update Discard Pile
        aDiscardCard = self.coffeeCard if len(self.o_discard.cards) == 0 else self.o_discard.getTopCard()
        self.o_discard.label["text"] = u"{0}{1} ".format(aDiscardCard.letter, aDiscardCard.symbol)
        self.o_discard.label["fg"] = aDiscardCard.color
        self.o_discard.label["bg"] = "White"

        # update Foundations
        self.updateFoundationLabel(self.o_spadeGoal)
        self.updateFoundationLabel(self.o_clubGoal)
        self.updateFoundationLabel(self.o_heartGoal)
        self.updateFoundationLabel(self.o_diamondGoal)

        # update Tableau
        for stack in self.tableau:
            self.updateTableauStack(stack)

        # Update Form Number of Cards in Draw Pile
        self.gL_Draw = Label(self.gameFrame, text=str(len(self.o_draw.cards))).grid(row=(self.gameTopRow + 2),
                                                                                    column=15)

    def autoMoveToFoundation(self, inStack):
        checkSuit = inStack.getTopCard().suit
        inStack.button.invoke()

        lowestLevel = 13
        if self.o_heartGoal.getTopCard() is not None and self.o_heartGoal.getTopCard().value < lowestLevel: lowestLevel = self.o_heartGoal.getTopCard().value
        if self.o_spadeGoal.getTopCard() is not None and self.o_spadeGoal.getTopCard().value < lowestLevel: lowestLevel = self.o_spadeGoal.getTopCard().value
        if self.o_clubGoal.getTopCard() is not None and self.o_clubGoal.getTopCard().value < lowestLevel: lowestLevel = self.o_clubGoal.getTopCard().value
        if self.o_diamondGoal.getTopCard() is not None and self.o_diamondGoal.getTopCard().value < lowestLevel: lowestLevel = self.o_diamondGoal.getTopCard().value
        if (self.o_heartGoal.getTopCard() is None) or (self.o_spadeGoal.getTopCard() is None) or (
                self.o_clubGoal.getTopCard() is None) or (self.o_diamondGoal.getTopCard() is None): lowestLevel = 0

        if checkSuit == Suit.Heart:
            self.o_temp.travelTo = self.o_heartGoal
        if checkSuit == Suit.Spade:
            self.o_temp.travelTo = self.o_spadeGoal
        if checkSuit == Suit.Club:
            self.o_temp.travelTo = self.o_clubGoal
        if checkSuit == Suit.Diamond:
            self.o_temp.travelTo = self.o_diamondGoal

        if self.o_temp.validate(Stack.Foundation) and self.o_temp.cards[0].value <= (lowestLevel + 2):
            self.o_temp.travelTo.button.invoke()
        if self.o_temp.status == TransactionStatus.Open: inStack.button.invoke()

    def updateTableauStack(self, aCardStack):
        shownCards = [self.coffeeCard] if len(aCardStack.cards) == 0 else aCardStack.cards[-aCardStack.movingcards:]
        # print(" -- cards in Stack: {0}".format(aCardStack.movingcards))
        for pos in range(aCardStack.movingcards):
            # print(" -- {0} of {1} cards".format(pos, aCardStack.movingcards))
            aCard = shownCards[pos]
            labelPrep = u"{0}{1} ".format(aCard.letter, aCard.symbol)
            aCardStack.labelStack[pos]["text"] = labelPrep
            aCardStack.labelStack[pos]["fg"] = aCard.color
            aCardStack.labelStack[pos]["bg"] = Color.White
        for pos in range(aCardStack.movingcards, 13):
            aCard = self.milkCard
            labelPrep = u"{0}{1} ".format(aCard.letter, aCard.symbol)
            aCardStack.labelStack[pos]["text"] = labelPrep
            aCardStack.labelStack[pos]["fg"] = aCard.color
            aCardStack.labelStack[pos]["bg"] = Color.White

    def updateTableauLabel(self, aCardStack):
        aCard = self.coffeeCard if len(aCardStack.cards) == 0 else aCardStack.cards[len(aCardStack.cards) - 1]
        labelPrep = u"{0}{1} ".format(aCard.letter, aCard.symbol)
        aCardStack.label["text"] = labelPrep
        aCardStack.label["fg"] = aCard.color
        aCardStack.label["bg"] = Color.White

    def dealCards(self):
        for i in range(len(self.tableau)):
            for j in range(i + 1):
                self.fillStack(self.tableau[i])
        self.o_draw.cards = self.gameDeck.cards

    def fillStack(self, stack):
        stack.cards.append(self.gameDeck.cards.pop())

    def displayStack(self, stack):
        stackline = ""
        for i in stack.cards:
            stackline += u"{0}{1} ".format(i.letter, i.symbol)
        return stackline

    def __str__(self):
        layout = "SOLITAIRE"
        layout += "\n---------\n"
        for i in range(len(self.tableau)):
            layout += self.displayStack(self.tableau[i])
            layout += "\n"
        return layout


# ***** ***** ***** ***** *****
# Game Object/Concepts
# ***** ***** ***** ***** *****
class cardPile:
    def __init__(self):
        self.type = "Generic"
        self.cards = []
        self.movingcards = 1
        self.button = None
        self.label = None

    def getTopCard(self):
        return None if len(self.cards) == 0 else self.cards[-1]

    def isSameSuit(self):
        return (self.cards[0].suit == self.travelTo.suit)

    def isOppositeColor(self):
        return (self.getTopCard().color != self.travelTo.getTopCard().color)

    def isNextFoundationCard(self):
        return (self.cards[0].value == (self.travelTo.getTopCard().value + 1))

    def isNextTableauCard(self):
        return (self.getTopCard().value == (self.travelTo.getTopCard().value - 1))

    def isEmptyTargetStack(self):
        return (len(self.travelTo.cards) == 0)

    def isAce(self):
        return (self.cards[0].value == 1)

    def isKing(self):
        return (self.getTopCard().value == 13)


class transaction(cardPile):
    def __init__(self, travelFrom):
        cardPile.__init__(self)
        self.type = Stack.Transaction
        self.travelFrom = travelFrom
        self.travelTo = None
        self.status = TransactionStatus.Closed

    def validate(self, inTarget):
        return self.validateFoundation() if inTarget == Stack.Foundation else self.validateTableau()

    def validateFoundation(self):
        if self.isSameSuit():
            if self.isEmptyTargetStack():
                return True if self.isAce() else False
            else:
                return True if self.isNextFoundationCard() else False
        else:
            return False

    def validateTableau(self):
        if self.isEmptyTargetStack():
            return True if self.isKing() else False
        else:
            return True if self.isNextTableauCard() and self.isOppositeColor() else False

    def makeTransaction(self, pickupCount):
        if self.status == TransactionStatus.Closed and len(self.travelFrom.cards) > 0:
            self.status = TransactionStatus.Open
            tempSet = self.travelFrom.cards[::]
            for i in range(pickupCount):
                self.cards.append(tempSet.pop())

    def performTransaction(self, stackType):
        return self.performToFoundation() if stackType == Stack.Foundation else self.performToTableau()

    def performToFoundation(self):
        self.travelTo.cards.append(self.travelFrom.cards.pop())
        self.travelFrom.movingcards = self.travelFrom.movingcards - 1

        # Adjust Numbers
        if self.travelFrom.movingcards <= 0:
            self.travelFrom.movingcards = 0

        if len(self.travelFrom.cards) > 0 and self.travelFrom.movingcards == 0:
            self.travelFrom.movingcards = 1

        self.travelTo.movingcards = self.travelTo.movingcards + 1

    def performToTableau(self):
        cardCount = len(self.cards)
        for i in range(cardCount):
            self.travelTo.cards.append(self.cards.pop())
            self.travelFrom.cards.pop()

        # Adjust Numbers
        self.travelFrom.movingcards = self.travelFrom.movingcards - cardCount

        if self.travelFrom.movingcards < 0:
            self.travelFrom.movingcards = 0

        if len(self.travelFrom.cards) > 0:
            self.travelFrom.movingcards = 1

        self.travelTo.movingcards = self.travelTo.movingcards + cardCount

        if len(self.travelTo.cards) == 1:
            self.travelTo.movingcards = 1

    def closeTransaction(self):
        self.travelTo = None
        self.travelFrom = None
        self.cards = []
        self.status = TransactionStatus.Closed


class goalPile(cardPile):
    def __init__(self, suit):
        cardPile.__init__(self)
        self.type = Stack.Foundation
        self.suit = suit


class discardPile(cardPile):
    def __init__(self):
        cardPile.__init__(self)
        self.type = Stack.Discard


class drawPile(cardPile):
    def __init__(self):
        cardPile.__init__(self)
        self.type = Stack.Draw


class tableauPile(cardPile):
    def __init__(self):
        cardPile.__init__(self)
        self.type = Stack.Tableau
        self.labelStack = None


# ***** ***** ***** ***** *****
# Base Objects
# ***** ***** ***** ***** *****
class DeckOfCards:
    def __init__(self):
        self.cards = []
        self.constructDeck()
        self.shuffled = False
        self.shuffleDeck()

    def constructDeck(self):
        cardNames = ["Ace", "Deuce", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten", "Jack", "Queen",
                     "King"]
        cardValues = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        cardLetters = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cardSuits = [Suit.Heart, Suit.Diamond, Suit.Spade, Suit.Club]
        for j in range(4):
            thisSuit = cardSuits[j]
            for i in range(13):
                newCard = Card(cardNames[i], thisSuit, cardValues[i], cardLetters[i])
                self.cards.append(newCard)

    def printDeck(self):
        for card in self.cards:
            print(card)

    def shuffleDeck(self):
        for i in range(len(self.cards)):
            rPos = random.randint(0, len(self.cards) - 1)
            tempCard = self.cards[rPos]
            self.cards[rPos] = self.cards[i]
            self.cards[i] = tempCard
        self.shuffled = True


class Card:
    def __init__(self, name, suit, value, letter):
        self.name = name
        self.suit = suit
        self.value = value
        self.letter = letter
        self.setColor()
        self.setSymbol()

    def __str__(self):
        return "{0} of {1}s".format(self.name, self.suit)

    def setColor(self):
        self.color = Color.Red if self.suit == Suit.Heart or self.suit == Suit.Diamond else Color.Black
        if self.suit == Suit.Blank:
            self.color = Color.Brown
        if self.suit == Suit.Milk:
            self.color = Color.White

    def setSymbol(self):
        if self.suit == Suit.Heart: self.symbolNumber = 2665
        if self.suit == Suit.Diamond: self.symbolNumber = 2666
        if self.suit == Suit.Spade: self.symbolNumber = 2660
        if self.suit == Suit.Club: self.symbolNumber = 2663
        if self.suit == Suit.Blank: self.symbolNumber = 2615
        if self.suit == Suit.Milk: self.symbolNumber = 2619
        if sys.version_info >= (3, 0):
            self.symbol = chr(int(str(self.symbolNumber), 16))
        else:
            self.symbol = unichr(int(str(self.symbolNumber), 16))


class Suit:
    Heart = "Heart"
    Diamond = "Diamond"
    Spade = "Spade"
    Club = "Club"
    Blank = "Blank"
    Milk = "Milk"


class Color:
    Red = "Red"
    Black = "Black"
    White = "White"
    Brown = "Brown"


class TransactionStatus:
    Open = 1
    Closed = 0


class Stack:
    Foundation = "F"
    Tableau = "T"
    Draw = "D"
    Discard = "W"
    Transaction = "X"


from tkinter import *


def initRun():

    root = Tk()
    myGame = Solitaire(root)

    root.mainloop()

    # print("Deck of Cards")
    # myDeck = DeckOfCards()
    # myDeck.printDeck()