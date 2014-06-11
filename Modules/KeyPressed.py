class KeyPressed:
    RIGHT = 0
    LEFT = 1
    UP = 2
    DOWN = 3

    def __init__(self, key):
        self.__key = key

    def setKey(self, key):
        self.__key = key

    def getKey(self):
        return self.__key

