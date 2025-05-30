class pawn:
    def __init__(self):
        self.resetpawn()
        self.pos = 0

    def resetpawn(self):
        self.boardPosition = -1
        self.safeZonePosition = -1
        self.atStart = True
        self.inSafeZone = False
        self.atHome = False

    def __eq__(self, other):
        newPawn = pawn()
        newPawn.atHome = self.atHome
        newPawn.atStart = self.atStart
        newPawn.inSafeZone = self.inSafeZone
        newPawn.boardPosition = self.boardPosition
        newPawn.safeZonePosition = self.safeZonePosition
        return newPawn
    
    def setBoardPosition(self, pos):
        self.boardPosition = pos

    def setSafeZonePosition(self, pos):
        self.safeZonePosition = pos

    def setAtStart(self, binary):
        self.atStart = binary

    def setInSafeZone(self, binary):
        self.inSafeZone = binary

    def setAtHome(self, binary):
        self.atHome = binary

    def getBoardPostition(self):
        return self.boardPosition

    def getSafeZonePostition(self):
        return self.safeZonePosition

    def getAtStart(self):
        return self.atStart

    def getInSafeZone(self):
        return self.inSafeZone

    def getAtHome(self):
        return self.atHome