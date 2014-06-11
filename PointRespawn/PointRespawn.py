from Modules.Images import Images


class PointRespawn:
    __image = None
    def __init__(self, posX, posY, nameImage):
        self.__posX = posX
        self.__posY = posY
        self.nameImage = nameImage
        self.animate()
        self.bots = list()
        self.counter = 0
        self.countBots = 0
        self.maxCountBots = 10

    def setPosition(self, posX, posY):
        self.__posX = posX
        self.__posY = posY

    def getPosition(self):
        return (self.__posX, self.__posY)

    def animate(self):
        images = Images()
        self.__image = images.getImage(self.nameImage)

    def getBots(self):
        return self.bots

    def getPosX(self):
        return self.__posX

    def getPosY(self):
        return self.__posY

    def getImage(self):
        return self.__image

    def process(self):
        if self.counter == 21:
            self.counter = 0
        if self.counter == 20:
            if self.countBots < self.maxCountBots:
                for bot in self.bots:
                    if not bot.isLive():
                        self.refreshBot(bot)
                        break
                self.countBots += 1
        self.counter += 1
        self.checkCountSpider()

    def refreshBot(self, bot):
        bot.setPosition(self.getPosX() - 45, self.getPosY() + 5)
        bot.setLive(True)
        bot.getHealth().setHealth(3)
        bot.setCountMove(0)

    def checkCountSpider(self):
        count = 0
        for bot in self.bots:
            if not bot.isLive():
                count += 1
            self.countBots = self.maxCountBots - count

