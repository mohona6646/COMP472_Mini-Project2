class Car:
    def __init__(self, carName, position="", startPos=(), carLength=2, fuel=100, carsFullPosition=[]):
        self.position = position
        self.startPos = startPos
        self.carLength = carLength
        self.fuel = fuel
        self.carName = carName
        self.carFullPosition = self.initializeCarPos()
        self.gCost = 0
        self.hCost = 0
        self.parent = object

    def isHorizontal(self):
        return self.position == "Horizontal"

    def isVertical(self):
        return self.position == "Vertical"

    def useFuel(self, amount):
        self.fuel -= amount

    def hasFuel(self):
        return self.fuel > 0

    def printCarInfo(self):
        print("Car Name ", self.carName, " and it has a fuel of ", self.fuel, " and its start position is ",
              self.startPos, " and the car is ", self.position, " and has the length of ", self.carLength,
              " and its full part location is ", self.carFullPosition)

    def initializeCarPos(self):
        x = self.startPos[0]
        y = self.startPos[1]
        counter = 0
        carFullPosition=[]
        if self.isHorizontal():
                for i in range(self.carLength):
                    carFullPosition.append((x, y + counter))
                    counter = counter + 1
        elif self.isVertical():
                for i in range(self.carLength):
                    carFullPosition.append((x + counter, y))
                    counter = counter + 1
        return carFullPosition

    def getFullCarPosition(self):
        return self.carFullPosition

    def setStartPosition(self, position):
        self.startPos = position

    def setCarFullPosition(self, positions):
        self.carFullPosition = positions

    def setgCost(self, cost):
        self.gCost = cost

    def sethCost(self, cost):
        self.hCost = cost

    def setParent(self, car):
        self.parent = car