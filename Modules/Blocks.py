from pygame import*

class Platform(sprite.Sprite):
    WIDTH = HEIGHT = 50
    def __init__(self, posX, posY, image, values):
        sprite.Sprite.__init__(self)
        self.posX = posX
        self.posY = posY
        self.image = image
        self.__values = values
        self.rect = Rect(posX, posY, self.WIDTH, self.HEIGHT)
        self.size = 50

    def getValues(self):
        return self.__values

    def setImage(self, image, values):
        self.image = image
        self.__values = values

    def getPosX(self):
        return self.posX

    def getPosY(self):
        return self.posY

    def getSize(self):
        return self.size



