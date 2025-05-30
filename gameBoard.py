class gameBoard:
    def __init__(self):
        self.position = 0
        self.pos = {
            0: (20, 20),
            1: (20, 20),
            2: (20, 20),
            3: (20, 20)
        }

class gameBoard2:
    def __init__(self):
        self.position = 0
        self.pos = [[0 for i in range(17)] for i in range(17)]
        self.boardPosX = 0
        self.boardPosY = 0

    def MovePawn(self):
        if self.boardPosX <= 16:
            self.boardPosY += 1