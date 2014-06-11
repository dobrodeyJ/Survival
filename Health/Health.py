from Modules.Images import Images

class Health:
    image = None
    def __init__(self, countHealth, nameImage):
        self.countHealth = countHealth
        self.nameImage = nameImage
        self.lives = True
        self.images = Images()

    def setHealth(self, countHealth):
        self.countHealth = countHealth
        self.animate()

    def getHealth(self):
        return self.countHealth

    def setPosition(self, posX, posY):
        self.__posX = posX
        self.__posY = posY

    def getPosition(self):
        return (self.__posX, self.__posY)

    def isLive(self):
        return self.lives

    def minusHealth(self):
        if self.isLive():
            if self.countHealth == 1:
                self.lives = False
            self.countHealth -= 1
        self.animate()

    def animate(self):
        pass

    def getImage(self):
        return self.image
