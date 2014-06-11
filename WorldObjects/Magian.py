from Atack.FireBall import FireBall
from Health.HealthBot import HealthBot
from Player import *

class Magian(Player):
    def __init__(self, posX, posY):
        path = "magian"
        self.atack = FireBall()
        Player.__init__(self, posX, posY, path)
