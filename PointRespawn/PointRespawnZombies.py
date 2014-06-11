from PointRespawn import PointRespawn
from WorldObjects.Spider import Spider
from WorldObjects.Zombies import Zombies
import pygame

class PointRespawnZombies(PointRespawn):
    def __init__(self, posX, posY):
        PointRespawn.__init__(self, posX, posY, "respawn_zombies")
        self.maxCountBots = 10
        self.countBots = 0
        self.counter = 0
        for i in range(self.maxCountBots):
            zombie = Zombies(self.getPosX() - 45, self.getPosY() + 5)
            zombie.setLive(False)
            self.bots.append(zombie)




