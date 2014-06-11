from Teleport import Teleport
from Teleports import Teleports
from WorldObjects.Player import *
from random import randrange


class CheckObjects:
    def __init__(self, player, platform, map, pointesOfRespawn, portalWin, generalTimer,  waweAlgorithm):
        self.player = player
        self.platform = platform
        self.portalWin = portalWin
        self.images = Images()
        self.teleport = Teleport(player, map)
        self.waweAlgorithm = waweAlgorithm
        self.generalTimer = generalTimer
        self.pointesOfRespawn = pointesOfRespawn
        self.woodBlocks = (100, 700, 800)
        self.startPositionPortalWin()

    def checkObjects(self):
        self.checkPlayer()
        self.checkBots()
        self.checkAtack()
        self.checkPortalWin()

    def checkPlayer(self):
        rect = Rect(self.player.getRect())
        if self.player.isRight():
            self.player.getRect().x += self.player.getStep()
        elif self.player.isLeft():
            self.player.getRect().x -= self.player.getStep()
        elif self.player.isDown():
            self.player.getRect().y += self.player.getStep()
        elif self.player.isUp():
            self.player.getRect().y -= self.player.getStep()
        if not self.collidePlayer(rect):
            self.player.move()
        else:
            self.player.setRect(rect)
        self.waweAlgorithm.startWay()
        self.player.animation()


    def collidePlayerBlock(self, rect):
        for block in self.platform:
            if block.getValues() != 0:
                if sprite.collide_rect(self.player, block):
                    if block.getValues() == Teleports.Teleport_In:
                        self.teleport.teleportation(Teleports.Teleport_Out, rect)
                    elif block.getValues() == Teleports.Teleport_Out:
                        self.teleport.teleportation(Teleports.Teleport_In, rect)
                    return True
        return False

    def collidePlayerBots(self):
        for point in self.pointesOfRespawn:
            bots = point.getBots()
            for bot in bots:
                if bot.isLive():
                    if sprite.collide_rect(self.player, bot):
                        return True
        return False

    def collidePlayer(self, rect):
        if self.portalWin.isOpen():
            if sprite.collide_rect(self.player, self.portalWin):
                self.portalWin.setInput(True)
        if self.collidePlayerBlock(rect):
            return True
        if self.collidePlayerBots():
            return True
        return False

    def checkAtack(self):
        if self.player.getAtack().isAtack():
            atack = self.player.getAtack()
            if atack.isRight():
                atack.getRect().x += atack.getStep()
            elif atack.isLeft():
                atack.getRect().x -= atack.getStep()
            elif atack.isDown():
                atack.getRect().y += atack.getStep()
            elif atack.isUp():
                atack.getRect().y -= atack.getStep()
            if not self.collideAtack(atack):
                atack.move()
            else:
                atack.setAtack(False)

    def collideAtack(self, atack):
        if self.checkAtackBots(atack):
            return True
        for block in self.platform:
            if block.getValues() != 0:
                    if sprite.collide_rect(atack, block):
                        if block.getValues() == 100:
                            self.player.setScore(self.player.getScore() + 5)
                            block.setImage(self.images.getImage(700), 700)
                        elif block.getValues() == 700:
                            self.player.setScore(self.player.getScore() + 5)
                            block.setImage(self.images.getImage(800), 800)
                        elif block.getValues() == 800:
                            self.player.setScore(self.player.getScore() + 10)
                            self.platform.remove(block)
                        return True
        return False

    def checkAtackBots(self, atack):
        for point in self.pointesOfRespawn:
            bots = point.getBots()
            for bot in bots:
                if bot.isLive():
                    if sprite.collide_rect(atack, bot):
                        bot.damage()
                        self.player.setScore(self.player.getScore() + 10)
                        return True
        return False


    def checkBots(self):
        for point in self.pointesOfRespawn:
            bots = point.getBots()
            for bot in bots:
                if bot.isLive():
                    self.checkBot(bot)

    def checkBot(self, bot):
        if sprite.collide_rect(self.player, bot):
            self.player.damage()
        else:
            if bot.getCountMove() == 0:
                self.waweAlgorithm.next(bot)
            bot.move()

    def getCountWoodBlock(self):
        count = 0
        for block in self.platform:
            if block.getValues() in self.woodBlocks:
                count += 1
        return count

    def startPositionPortalWin(self):
        value = randrange(1, self.getCountWoodBlock())
        count = 0
        for block in self.platform:
            if block.getValues() in self.woodBlocks:
                count += 1
                if count == value:
                    self.portalWin.setPosition(block.getPosX(), block.getPosY())
                    return

    def searchBlock(self, posX, posY):
        for block in self.platform:
            if block.getPosX() == posX and block.getPosY() == posY:
                return True
        return False

    def checkPortalWin(self):
        if self.generalTimer.getTimeOpenPortal() == 0:
            if not self.portalWin.isOpen():
                if not self.searchBlock(self.portalWin.getPosX(), self.portalWin.getPosY()):
                    self.portalWin.setOpen(True)





