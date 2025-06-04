import pawn

class player:
    NO_OF_PAWNS = 4

    def __init__(self):
        self.resetPlayer()
        # Initialize independent pawn instances for this player
        self.playerPawns = [pawn.pawn() for _ in range(self.NO_OF_PAWNS)]

    def resetPlayer(self):
        self.color = ""
        self.setPositionStart(0)
        self.setPositionHome(0)

    def setColor(self, newColor):
        self.color = newColor

    def setPositionStart(self, pos):
        self.positionStart = pos

    def setPositionHome(self, pos):
        self.positionHome = pos

    def getPawn(self, index):
        return self.playerPawns[index]

    def getColor(self):
        return self.color

    def getPositionStart(self):
        return self.positionStart

    def getPositionHome(self):
        return self.positionHome
