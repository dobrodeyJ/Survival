from PointRespawn import PointRespawn
from WorldObjects.Spider import Spider

class PointRespawnSpider(PointRespawn):
    def __init__(self, posX, posY):
        PointRespawn.__init__(self, posX, posY, "respawn_spider")
        self.maxCountBots = 10
        self.countBots = 0
        self.counter = 0
        for i in range(self.maxCountBots):
            spider = Spider(self.getPosX() - 45, self.getPosY() + 5)
            spider.setLive(False)
            self.bots.append(spider)


