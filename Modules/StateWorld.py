
class StateWorld:
    WIN = 0
    MEAT = 1
    GAME = 2

    def __init__(self, state):
        self.__state = state

    def setState(self, state):
        self.__state = state

    def getState(self):
        return self.__state
