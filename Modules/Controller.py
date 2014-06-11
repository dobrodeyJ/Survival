import pygame
from pygame import *
import sys
from Modules.StateWorld import StateWorld
from World import World


class Controller:
    def __init__(self):
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