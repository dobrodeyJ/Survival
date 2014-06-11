from abc import abstractmethod
from pygame import*
from Modules.Images import Images
from Modules.KeyPressed import KeyPressed


class WorldObject(sprite.Sprite):
    __image = None
    __STEP = None
    __changeImage = 1
    __left = __right = __up = __down = False
    WHITE = (255, 255, 255)
    health = None

    def __init__(self, posX, posY, nameString, width, height):
        sprite.Sprite.__init__(self)
        self.initObject(posX, posY, nameString, width, height)

    def initObject(self, posX, posY, nameString, width, height):
        self.setPosition(posX, posY)
        self.setSize(width, height)
        self.rect = Rect(posX, posY, width, height)
        self.__nameString = nameString
        self.lives = True
        self.sprites = Images()
        self.keyPress = KeyPressed(KeyPressed.RIGHT)
        self.animation()

    def setPosition(self, posX, posY):
        self.__posX = posX
        self.__posY = posY

    def getPosition(self):
        return (self.__posX, self.__posY)

    def setStep(self, step):
        self.__STEP = step

    def getStep(self):
        return self.__STEP

    def setSize(self, width, height):
        self.__size = (width, height)

    def getSize(self):
        return self.__size

    def isRight(self):
        return self.__right

    def isLeft(self):
        return self.__left

    def isUp(self):
        return self.__up

    def isDown(self):
        return self.__down

    def toLeft(self):
        self.__left = True
        self.__right = self.__up = self.__down = False
        self.keyPress.setKey(KeyPressed.LEFT)

    def toRight(self):
        self.__right = True
        self.__left = self.__up = self.__down = False
        self.keyPress.setKey(KeyPressed.RIGHT)

    def toUp(self):
        self.__up = True
        self.__right = self.__left = self.__down = False
        self.keyPress.setKey(KeyPressed.UP)

    def toDown(self):
        self.__down = True
        self.__right = self.__up = self.__left = False
        self.keyPress.setKey(KeyPressed.DOWN)

    def setLeft(self, left):
        self.__left = left
        self.__changeImage = 1

    def setRight(self, right):
        self.__right = right
        self.__changeImage = 1

    def setUp(self, up):
        self.__up = up
        self.__changeImage = 1

    def setDown(self, down):
        self.__down = down
        self.__changeImage = 1

    def isLive(self):
        return self.lives

    def getImage(self):
        return self.__image

    def getWidth(self):
        return self.__size[0]

    def getHeight(self):
        return self.__size[1]

    def getRect(self):
        return self.rect

    def setRect(self, rect):
        self.rect = rect

    def getPosX(self):
        return self.__posX

    def getPosY(self):
        return self.__posY

    def getKeyPress(self):
        return self.keyPress

    def move(self):
        if self.isRight():
            self.setPosition(self.getPosX() + self.getStep(), self.getPosY())
        elif self.isLeft():
            self.setPosition(self.getPosX() - self.getStep(), self.getPosY())
        elif self.isDown():
            self.setPosition(self.getPosX(), self.getPosY() + self.getStep())
        elif self.isUp():
            self.setPosition(self.getPosX(), self.getPosY() - self.getStep())
        self.animation()

    def damage(self):
        self.health.minusHealth()
        if not self.health.isLive():
            self.lives = False

    def animation(self):
        if self.isRight():
            self.__loadImage("_right")
        elif self.isLeft():
            self.__loadImage("_left")
        elif self.isDown():
            self.__loadImage("_down")
        elif self.isUp():
            self.__loadImage("_up")
        else:
            self.__image = self.sprites.getImage(self.__nameString + "_down2")
        self.__image.set_colorkey(self.WHITE)

    def getHealth(self):
        return self.health

    def __loadImage(self, s):
        if self.__changeImage == 12:
            self.__changeImage = 1

        if self.__changeImage == 1:
            self.__image = self.sprites.getImage(self.__nameString + s + "1")
        elif self.__changeImage == 4:
            self.__image = self.sprites.getImage(self.__nameString + s + "2")
        elif self.__changeImage == 7:
            self.__image = self.sprites.getImage(self.__nameString + s + "3")
        elif self.__changeImage == 11:
            self.__image = self.sprites.getImage(self.__nameString + s + "2")
        self.__changeImage += 1