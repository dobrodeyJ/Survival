from Health.HealthHeroe import HealthHeroe
from WorldObject import *

class Player(WorldObject):
    atack = None
    score = 0
    def __init__(self, posX, posY, path):
        width = 25
        height = 40
        WorldObject.__init__(self, posX, posY, path, width, height)
        step = 5
        self.setStep(step)
        self.health = HealthHeroe()

    def getAtack(self):
        return self.atack

    def isAtack(self):
        self.atack.setAtack(True)
        self.atack.initialStartPosition(self)

    def getScore(self):
        return self.score

    def setScore(self, score):
        self.score = score





