from WorldObject import WorldObject


class Bot(WorldObject):
    __countMove = 0
    def __init__(self, posX, posY, nameImage, width, height):
        WorldObject.__init__(self, posX, posY, nameImage, width, height)

    def getCountMove(self):
        return self.__countMove

    def move(self):
        WorldObject.move(self)
        self.rect.x = self.getPosX()
        self.rect.y = self.getPosY()
        self.health.setPosition(self.getPosX() - 5, self.getPosY() - 4)
        if self.__countMove == 24:
            self.__countMove = 0
        else:
            self.__countMove += 1

    def setLive(self, lives):
        self.lives = lives
        self.getHealth().lives = lives

    def setCountMove(self, countMove):
        self.__countMove = countMove
