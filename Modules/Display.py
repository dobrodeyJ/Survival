import pygame
from pygame import*
from Blocks import Platform
from Images import Images

class Display:
    color = (200, 2, 2)

    def __init__(self, map, player, pointOfRespawn, generalTimer, portalWin):
        self.initWindow()
        self.player = player
        self.portalWin = portalWin
        self.image = Images()
        self.loadTexture(map)
        self.generalTimer = generalTimer
        self.pointofRespawn = pointOfRespawn



    def loadTexture(self, map):
        self.initBlocks(map)
        self.background = self.image.getImage("background").convert()
        self.topBar = self.image.getImage("top_bar").convert()
        self.meat =  self.image.getImage("MEAT")
        self.win = self.image.getImage("WIN")

    def initBlocks(self, map):
        size = 50
        imageUnConvert = [100, 800, 700, 300, 400]
        empty = [0, 500]
        self.entities = pygame.sprite.Group()
        for row in range(map.getHeight()):
            for col in range(map.getWidth()):
                if not map.getValues(row, col) in empty:
                    if map.getValues(row, col) in imageUnConvert:
                        platform = Platform(col * size, row * size, self.image.getImage(map.getValues(row, col)), map.getValues(row, col))
                    else:
                        platform = Platform(col * size, row * size, self.image.getImage(map.getValues(row, col)).convert(), map.getValues(row, col))
                    self.entities.add(platform)


    def initWindow(self):
        pygame.font.init()
        self.screen = pygame.display.get_surface()
        pygame.display.set_caption("GAME")

    def draw(self):
        self.drawBackGround()
        self.drawScore()
        self.drawBots()
        self.drawPortalWin()
        self.drawMap()
        self.drawGeneralTimer()
        self.drawPlayer()
        self.drawPortalsRespawn()
        self.drawAtacks()
        pygame.display.flip()

    def drawBackGround(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.topBar, (0, 0))

    def drawScore(self):
        (posX, posY, fontSize) = (800, 5, 50)
        myFont = pygame.font.Font("fonts/Plasma Drip.ttf", fontSize)
        fontImage = myFont.render("Score:" + str(self.player.getScore()), 0, (self.color))
        downImage = myFont.render("Score:" + str(self.player.getScore()), 0, ((0, 0, 0)))
        self.screen.blit(downImage, (posX + 3, posY + 3))
        self.screen.blit(fontImage, (posX, posY))


    def drawPlayer(self):
        if self.player.isLive():
            self.screen.blit(self.player.getImage(), self.player.getPosition())
        self.screen.blit(self.player.getHealth().getImage(), self.player.getHealth().getPosition())

    def drawAtacks(self):
        if self.player.getAtack().isAtack():
            self.screen.blit(self.player.getAtack().getImage(), self.player.getAtack().getPosition())

    def drawMap(self):
        self.entities.draw(self.screen)

    def getEntities(self):
        return self.entities

    def drawBots(self):
        for portal in self.pointofRespawn:
            bots = portal.getBots()
            for bot in bots:
                if bot.isLive():
                    self.screen.blit(bot.getImage(), bot.getPosition())
                    self.screen.blit(bot.getHealth().getImage(), bot.getHealth().getPosition())

    def drawPortalsRespawn(self):
        for pointRespawn in self.pointofRespawn:
            self.screen.blit(pointRespawn.getImage(), pointRespawn.getPosition())

    def drawGeneralTimer(self):
        (posX, posY, fontSize) = (650, 5, 50)
        myFont = pygame.font.Font("fonts/Plasma Drip.ttf", fontSize)
        if self.generalTimer.getTimeOpenPortal() == 0:
            fontImage = myFont.render(self.generalTimer.getStrTimeLivePortal(), 0, (self.color))
        else:
            fontImage = myFont.render(self.generalTimer.getStrTimeOpenPortal(), 0, (self.color))
        self.screen.blit(fontImage, (posX, posY))

    def drawPortalWin(self):
        if self.portalWin.isOpen():
            self.screen.blit(self.portalWin.getImage(), self.portalWin.getPosition())

    def drawMeat(self):
        self.screen.blit(self.meat, (0, 50))
        pygame.display.flip()

    def drawWin(self):
        self.screen.blit(self.win, (0, 50))
        pygame.display.flip()

