from Bot import Bot
from Health.HealthBot import HealthBot


class Spider(Bot):
    __hp = 3
    def __init__(self, posX, posY):
        width = 40
        height = 40
        Bot.__init__(self, posX, posY, "spider", width, height)
        self.setStep(2)
        hp = 3
        self.health = HealthBot(hp)
