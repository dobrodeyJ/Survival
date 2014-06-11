from Atack import Atack
from Modules.KeyPressed import KeyPressed


class Air(Atack):

    def __init__(self, nameImage,  step, width, height):
        Atack.__init__(self, nameImage, step, width, height)
        self.keyPress = KeyPressed(KeyPressed.RIGHT)

    def initialStartPosition(self, player):
        self.keyPress.setKey(player.keyPress.getKey())
        if self.keyPress.getKey() == KeyPressed.RIGHT or self.keyPress.getKey() == KeyPressed.LEFT:
            posY = player.getPosY() + ((player.getHeight() - self.getHeight()) / 2)
            if self.keyPress.getKey() == KeyPressed.RIGHT:
                self.setPosition(player.getPosX() + player.getWidth(), posY)
                self.goRight()
            elif self.keyPress.getKey() == KeyPressed.LEFT:
                self.setPosition(player.getPosX() - self.getWidth(), posY)
                self.goLeft()
        elif self.keyPress.getKey() == KeyPressed.DOWN or self.keyPress.getKey() == KeyPressed.UP:
            posX = player.getPosX() + ((player.getWidth() - 20) / 2)
            if self.keyPress.getKey() == KeyPressed.DOWN:
                self.setPosition(posX, player.getPosY() + 32)
                self.goDown()
            elif self.keyPress.getKey() == KeyPressed.UP:
                self.setPosition(posX, player.getPosY() - 32)
                self.goUp()
        self.animation()

    def move(self):
        if self.keyPress.getKey() == KeyPressed.RIGHT:
            self.setPosition(self.getPosX() + self.getStep(), self.getPosY())
        elif self.keyPress.getKey() == KeyPressed.LEFT:
            self.setPosition(self.getPosX() - self.getStep(), self.getPosY())
        elif self.keyPress.getKey() == KeyPressed.DOWN:
            self.setPosition(self.getPosX(), self.getPosY() + self.getStep())
        elif self.keyPress.getKey() == KeyPressed.UP:
            self.setPosition(self.getPosX(), self.getPosY() - self.getStep())
        self.animation()





