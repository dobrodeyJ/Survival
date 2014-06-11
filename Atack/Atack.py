from abc import abstractmethod
from Modules.Images import Images
from pygame import sprite, Rect, transform


class Atack(sprite.Sprite):
    __atack = False
    __width = __height = None
    __image = None
    __nameImage = None
    __step = None
    __left = __right = __down = __up = False
    rect = None
    __changeImage = 1


    def __init__(self, nameImage, step, width, height):
        sprite.Sprite.__init__(self)
        self.__initialObject(nameImage, step, width, height)
        self.sprites = Images()

    def __initialObject(self, nameImage, step, width, height):
        self.__nameImage = nameImage
        self.__step = step
        self.setSize(width, height)
        self.rect = Rect(0, 0, width, height)
        self.goRight()

    @abstractmethod
    def initialStartPosition(self):
        pass

    @abstractmethod
    def move(self):
        pass

    def setPosition(self, posX, posY):
        self.rect.x = posX
        self.rect.y = posY

    def getPosition(self):
        return (self.rect.x, self.rect.y)

    def getStep(self):
        return self.__step

    def isAtack(self):
        return self.__atack

    def setAtack(self, atack):
        self.__atack = atack

    def getImage(self):
        return self.__image

    def setSize(self, width, height):
        self.__size = (width, height)

    def getWidth(self):
        return self.__size[0]

    def getHeight(self):
        return self.__size[1]

    def getRect(self):
        return self.rect

    def setRect(self, rect):
        self.rect = rect

    def getPosX(self):
        return self.rect.x

    def getPosY(self):
        return self.rect.y

    def animation(self):
        if self.isAtack():
            if self.__changeImage == 6:
                self.__changeImage = 1
            self.__image = self.sprites.getImage(self.__nameImage + str(self.__changeImage))
            self.__changeImage += 1
            self.rotationImage()

    def rotationImage(self):
        if self.isLeft():
            self.rotationLeft()
        elif self.isRight():
            self.rotationRight()
        elif self.isDown():
            self.rotationDown()
        else:
            self.rotationUp()
        self.rect = self.__image.get_rect(center = self.rect.center)

    def rotationLeft(self):
        pass

    def rotationRight(self):
        self.__image = transform.rotate(self.__image, 180)


    def rotationUp(self):
        self.__image = transform.rotate(self.__image, -90)

    def rotationDown(self):
        self.__image = transform.rotate(self.__image, 90)


    def isLeft(self):
        return self.__left

    def isRight(self):
        return self.__right

    def isDown(self):
        return self.__down

    def isUp(self):
        return self.__up


    def goLeft(self):
        self.__left = True
        self.__right = self.__down = self.__up = False

    def goRight(self):
        self.__right = True
        self.__left = self.__down = self.__up = False

    def goDown(self):
        self.__down = True
        self.__right = self.__left = self.__up = False

    def goUp(self):
        self.__up = True
        self.__right = self.__down = self.__left = False
