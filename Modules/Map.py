from random import randrange

class Map:
    __width = 21
    __height = 12
    def __init__(self):
        self.__array = list()
        self.__loadFromFile()

    def __loadFromFile(self):
        values = randrange(1, 6)
        file = open("file/" + str(values), "r")
        for rows in range(self.__height):
            line = file.readline().strip().split(" ")
            row = list()
            for i in range(len(line)):
                row.append(int(line[i]))
            self.__array.append(row)
        file.close()

    def getWidth(self):
        return self.__width

    def getHeight(self):
        return self.__height

    def getMap(self):
        return self.__array

    def getValues(self, i, j):
        return self.__array[i][j]