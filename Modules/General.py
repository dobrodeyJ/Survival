import pygame
from pygame import *
import sys
from Images import Images
from StateWorld import StateWorld
from World import World

class General():
    WIDTH = 1050
    HEIGHT = 600
    display = (WIDTH, HEIGHT)
    location = None
    def __init__(self):
        pygame.init()
        pygame.display.set_mode(self.display)

    def events(self, event):
        if event.type == QUIT:
            sys.exit()

    def getWidth(self):
        return self.WIDTH

    def getHeight(self):
        return self.HEIGHT

class Location(object):
    def __init__(self):
        self.windows = pygame.display.get_surface()

    def events(self, event):
        pass

    def process(self):
        pass

class Menu_Location(Location):
    indikator = 1
    def __init__(self):
        Location.__init__(self)
        pygame.font.init()
        self.fontSize = 25
        self.font = pygame.font.Font(None, self.fontSize)
        self.images = Images()
        self.BG = self.images.getImage("menuBG").convert()
        self.initButton()

    def initButton(self):
        self.startUp = self.images.getImage("startUp")
        self.startDown = self.images.getImage("startDown")
        self.exitUp = self.images.getImage("exitUp")
        self.exitDown = self.images.getImage("exitDown")

    def draw(self):
        self.drawBG()
        self.drawMenu()
        pygame.display.flip()

    def drawMenu(self):
        if self.indikator == 1:
            self.windows.blit(self.startDown, (446, 200))
            self.windows.blit(self.exitUp, (446, 270))
        elif self.indikator == 2:
            self.windows.blit(self.startUp, (446, 200))
            self.windows.blit(self.exitDown, (446, 270))

    def drawBG(self):
        self.windows.blit(self.BG, (0, 0))

    def events(self, event):
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if self.indikator == 1:
                   self.indikator = 2
                else:
                    self.indikator -= 1
            if event.key == K_DOWN:
                if self.indikator == 2:
                    self.indikator = 1
                else:
                    self.indikator += 1
            if event.key == K_RETURN:
                if self.indikator == 1:
                    general.location = gameLocation
                    general.location.startTime()
                else:
                    sys.exit()

    def process(self):
        self.draw()

class Game_Location(Location):
    def __init__(self):
        Location.__init__(self)
        self.world = World()

    def events(self, event):
            self.__eventExit(event)
            self.__eventKey(event)

    def __eventExit(self, event):
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            sys.exit()

    def __eventKey(self, event):
        self.__eventKeyDown(event)
        self.__eventKeyUp(event)

    def __eventKeyDown(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                self.world.getPlayer().toLeft()
            elif event.key == pygame.K_RIGHT:
                self.world.getPlayer().toRight()
            elif event.key == pygame.K_DOWN:
                self.world.getPlayer().toDown()
            elif event.key == pygame.K_UP:
                self.world.getPlayer().toUp()
            elif event.key == pygame.K_SPACE:
                if self.world.getPlayer().isLive():
                    if not self.world.getPlayer().getAtack().isAtack():
                        self.world.getPlayer().isAtack()

    def __eventKeyUp(self, event):
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                self.world.getPlayer().setLeft(False)
            elif event.key == pygame.K_RIGHT:
                self.world.getPlayer().setRight(False)
            elif event.key == pygame.K_DOWN:
                self.world.getPlayer().setDown(False)
            elif event.key == pygame.K_UP:
                self.world.getPlayer().setUp(False)

    def startTime(self):
        self.world.timerStart()

    def process(self):
        if self.world.getState() == StateWorld.GAME:
            self.world.stateGame()
        if self.world.getState() == StateWorld.MEAT:
            self.world.stateMeat()
        if self.world.getState() == StateWorld.WIN:
            self.world.stateWin()


general = General()
menuLocation = Menu_Location()
general.location = menuLocation
gameLocation = Game_Location()

clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        general.events(event)
        general.location.events(event)
    general.location.process()
    clock.tick(40)
pygame.quit()
