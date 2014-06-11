from CheckObjects import CheckObjects
from Display import Display
from GeneralTimer import MyTimer
from Map import Map
from StateWorld import StateWorld
from WaweAlgorithm import WaweAlgorithm
from PointRespawn.PointRespawnSpider import PointRespawnSpider
from PointRespawn.PointRespawnZombies import PointRespawnZombies
from WorldObjects.Magian import Magian
from WorldObjects.PortalWin import PortalWin

class World:
    endGame = False
    def __init__(self):
        self.__initObjects()
        self.state = StateWorld(StateWorld.GAME)

    def __initObjects(self):
        self.Generaltimer = MyTimer()
        self.map = Map()
        self.player = Magian(55, 105)
        self.portalZombies = PointRespawnZombies(950, 500)
        self.portalSpiders = PointRespawnSpider(950, 100)
        self.portalWin = PortalWin()
        self.pointesOfRespawn = [self.portalZombies, self.portalSpiders]
        self.display = Display(self.map, self.player, self.pointesOfRespawn, self.Generaltimer, self.portalWin)
        self.waweAlgoritm = WaweAlgorithm(self.player, self.display.getEntities(), self.map)
        self.checkObject = CheckObjects(self.player, self.display.getEntities(), self.map, self.pointesOfRespawn,self.portalWin, self.Generaltimer, self.waweAlgoritm)

    def checkPointOfRespawn(self):
        for pointResp in self.pointesOfRespawn:
            pointResp.process()

    def checkGame(self):
        if (self.Generaltimer.getTimeLivePortal() == 0) or (not self.player.isLive()):
            self.state.setState(StateWorld.MEAT)
        elif self.portalWin.isInput():
            self.state.setState(StateWorld.WIN)

    def stateGame(self):
        self.checkGame()
        self.checkPointOfRespawn()
        self.checkObject.checkObjects()
        self.display.draw()

    def stateMeat(self):
        if not self.endGame:
            self.display.drawMeat()
            self.endGame = True

    def stateWin(self):
        if not self.endGame:
            self.display.drawWin()
            self.endGame = True

    def timerStart(self):
        self.Generaltimer.start()

    def getState(self):
        return self.state.getState()

    def getPlayer(self):
        return self.player
