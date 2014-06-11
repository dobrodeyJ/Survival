from Modules.Images import Images
from pygame import sprite, Rect

class PortalWin(sprite.Sprite):
    __image = None
    __open = False
    input = False

    def __init__(self):
        sprite.Sprite.__init__(self)
        self.rect = Rect(0, 0, 50, 50)
        self.images = Images()
        self.animate()

    def setPosition(self, posX, posY):
        (self.rect.x, self.rect.y) = (posX, posY)

    def getPosition(self):
        return (self.rect.x, self.rect.y)

    def animate(self):
        self.__image = self.images.getImage("portalWin")

    def getImage(self):
        return self.__image

    def setOpen(self, open):
        self.__open = open

    def isOpen(self):
        return self.__open

    def getPosX(self):
        return self.rect.x

    def getPosY(self):
        return self.rect.y

    def setInput(self, input):
        self.input = input

    def isInput(self):
        return self.input