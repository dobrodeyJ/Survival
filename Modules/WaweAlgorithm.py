from Map import Map
from Blocks import Platform
from random import randrange

class WaweAlgorithm:
    def __init__(self, player, entities, map):
        self.player = player
        self.entities = entities
        self.WIDTH = map.getWidth()
        self.HEIGHT = map.getHeight()
        self.maxIterator = (self.WIDTH * self.HEIGHT) / 2

    def refreshMap(self):
        arrayValues = [100, 700, 800]
        map = list()
        for row in range(self.HEIGHT):
            rows = list()
            for col in range(self.WIDTH):
                rows.append(0)
            map.append(rows)
        for block in self.entities:
            if block.getValues() in arrayValues:
                map[block.getPosY()/block.getSize()][block.getPosX() / block.getSize()] = 0
            else:
                map[block.getPosY()/block.getSize()][block.getPosX() / block.getSize()] = block.getValues()
        return map

    def startWay(self):
        iterator = 1
        IndexRow = self.player.getPosY() / 50
        IndexCol = self.player.getPosX() / 50
        self.map = self.refreshMap()
        self.map[IndexRow][IndexCol] = iterator
        while iterator < self.maxIterator:
            for row in range(self.HEIGHT):
                for col in range(self.WIDTH):
                    if self.map[row][col] == iterator:
                        if row + 1 < self.HEIGHT:
                            if self.map[row + 1][col] == 0:
                                self.map[row + 1][col] = iterator + 1
                        if row - 1 > 0:
                            if self.map[row - 1][col] == 0:
                                self.map[row - 1][col] = iterator + 1
                        if col - 1 > 0:
                            if self.map[row][col - 1] == 0:
                                self.map[row][col - 1] = iterator + 1
                        if col + 1 < self.WIDTH:
                            if self.map[row][col + 1] == 0:
                                self.map[row][col + 1] = iterator + 1
            iterator += 1

    def getNextStep(self, bot):
        row = bot.getPosY() / 50
        col = bot.getPosX() / 50
        step = list()
        if row + 1 < self.HEIGHT:
            if self.map[row + 1][col] < self.map[row][col]:
                step.append("down")
        if row - 1 > 0:
            if self.map[row - 1][col] < self.map[row][col]:
                step.append("up")
        if col - 1 > 0:
            if self.map[row][col - 1] < self.map[row][col]:
                step.append("left")
        if col + 1 < self.WIDTH:
            if self.map[row][col + 1] < self.map[row][col]:
                step.append("right")
        return self.randGo(step)

    def randGo(self, step):
        if len(step) == 0:
            pass
        elif len(step) == 1:
            return step[0]
        else:
            value = randrange(0, 2)
            return step[value]

    def next(self, bot):
        string = self.getNextStep(bot)
        if string == "left":
            bot.toLeft()
        elif string == "right":
            bot.toRight()
        elif string == "down":
            bot.toDown()
        elif string == "up":
            bot.toUp()

    def getCopyValue(self, row, col):
        return self.map[row][col]

    def getWidth(self):
        return self.WIDTH

    def getHeight(self):
        return self.HEIGHT
