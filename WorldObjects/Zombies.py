from Bot import Bot
from Health.HealthBot import HealthBot


class Zombies(Bot):
    def __init__(self, posX = None, posY = None):
        width = 25
        height = 32
        Bot.__init__(self, posX, posY, "zombie", width, height)
        self.setStep(2)
        hp = 3
        self.health = HealthBot(hp)
