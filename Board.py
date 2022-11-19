from CarClass import Car
from typing import List


class Board:

    def __init__(self):
        rows, columns = (6, 6)
        matrix = [[0 for x in range(rows)] for y in range(columns)]
        self.matrix = matrix
        self.cars: List[Car] = []
        self.parentsCar = {}

    def CreateNewCars(self, cars):
        self.cars = cars
        return self.cars

    def isGoalPos(self, nextMove):
        for cars in nextMove.cars:
            if cars.name == "A":
                # Reaching the goal
                if Car(cars).endPos == [2, 5] and Car(cars).startPos == [3, 5]:
                    return True

    def getCarName(self, name):
        for x in self.cars:
            if x.carName == name:
                return x

    def setFuelLevel(self, fuelValue):
        for fuel in fuelValue:
            car = fuel[0]
            fuel_value = int(fuel[1:])
            carName = self.getCarName(car)
            carName.gas = fuel_value

    def getCarsInfo(self):
        info = {}
        length = 0
        isHorizontal = False
        for row in range(6):
            for column in range(6):
                c = self.matrix[row][column]
                if c in info:
                    continue
                if c == ".":
                    continue
                if column + 1 < 6 and c == self.matrix[row][column + 1]:
                    isHorizontal = True
                    length = length + 1
                    for i in range(column + 1, 6):
                        if c == self.matrix[row][i]:
                            length = length + 1
                if row + 1 < 6 and c == self.matrix[row + 1][column]:
                    isHorizontal = False
                    length = length + 1
                    for i in range(row + 1, 6):
                        if c == self.matrix[i][column]:
                            length = length + 1
                info[c] = [length, isHorizontal, (row, column)]
                length = 0
                isHorizontal = False
        return info

    def MoveRight(self, car):
        if car.isHorizontal():
            last = car.getFullCarPosition()[car.carLength - 1]
            if last[1] + 1 > 5 or self.matrix[last[0]][last[1] + 1] != ".":
                print("Cant move right a car might be blocking or it is out of bounds")
                return False
            else:
                # swap idk and change the fuel
                return True
        print("Car is not horizontal!")
        return False

    def MoveLeft(self, car):
        if car.isHorizontal():
            first = car.startPos
            if first[1] - 1 < 0 or self.matrix[first[0]][first[1] - 1] != ".":
                print("Cant move left a car might be blocking or it is out of bounds")
                return False
            else:
                # swap idk and change the fuel
                return True
        print("Car is not horizontal!")
        return False

    def MoveUp(self, car):
        if car.isVertical():
            first = car.startPos
            if first[0] - 1 < 0 and self.matrix[first[0] - 1][first[1]] != ".":
                print("Cant move up a car might be blocking or it is out of bounds")
                return False
            else:
                # swap idk and change the fuel
                return True
        print("Car is not vertical!")
        return False

    def MoveDown(self, car):
        if car.isVertical():
            last = car.getFullCarPosition()()[car.carLength - 1]
            if last[0] + 1 > 5 or self.matrix[last[0] + 1][last[1]] != ".":
                print("Cant move down a car might be blocking or it is out of bounds")
                return False
            else:
                # swap idk and change the fuel
                return True
        print("Car is not vertical!")
        return False
