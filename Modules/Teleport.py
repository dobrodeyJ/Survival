class Teleport:
    __indexRow = __indexCol = 0
    __portal = None
    def __init__(self, player, map):
        self.player = player
        self.map = map

    def searchPortal(self):
        for row in range(self.map.getHeight()):
            for col in range(self.map.getWidth()):
                if self.map.getValues(row, col) == self.__portal:
                    self.__indexCol = col
                    self.__indexRow = row
                    return

    def searchEmpty(self, rect):
        if(self.map.getValues(self.__indexRow - 1, self.__indexCol) == 0):
			self.changePositionPlayer(self.__indexRow - 1, self.__indexCol, rect)
        elif(self.map.getValues(self.__indexRow + 1, self.__indexCol) == 0):
			self.changePositionPlayer(self.__indexRow + 1, self.__indexCol, rect)
        elif(self.map.getValues(self.__indexRow, self.__indexCol - 1) == 0):
			self.changePositionPlayer(self.__indexRow, self.__indexCol - 1, rect)
        elif(self.map.getValues(self.__indexRow, self.__indexCol + 1) == 0):
			self.changePositionPlayer(self.__indexRow, self.__indexCol + 1, rect)

    def changePositionPlayer(self, row, col, rect):
        size = 50
        self.player.setPosition(size * col + 15, size * row + 5)
        rect.x = size * col + 15
        rect.y = size * row + 5

    def teleportation(self, portal, rect):
        self.__portal = portal
        self.searchPortal()
        self.searchEmpty(rect)

