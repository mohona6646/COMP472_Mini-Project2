from CarClass import Car
from typing import List
import copy


class Board:
    def __init__(self, puzzles):
        rows, columns = (6, 6)
        matrix = [[0 for x in range(rows)] for y in range(columns)]
        self.matrix = matrix
        self.cars = []
        self.parentsCar = {}
        self.MakingMatrix(puzzles)

    def clone(self):
        boardCopy = copy.deepcopy(self)
        return boardCopy

    def CreateNewCars(self, cars):
        self.cars = cars
        return self.cars

    def isGoalPos(self, car):
        if car not in self.cars:
            return True
        else:
            return False

    def getCarName(self, name):
        for x in self.cars:
            if x.carName == name:
                return x

    def getCarNameAtLocation(self, x, y):
        return self.matrix[x][y]

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

    def isMoveableRight(self, car):
        if car.isHorizontal():
            last = car.getFullCarPosition()[car.carLength - 1]
            if last[1] + 1 > 5 or self.matrix[last[0]][last[1] + 1] != ".":
                print(last)
                print("Cant move right a car might be blocking or it is out of bounds")
                return False
            else:
                # swap idk and change the fuel
                return True
        print("Car is not horizontal!")
        return False

    def isMoveableLeft(self, car):
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

    def isMoveableUp(self, car):
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

    def isMoveableDown(self, car):
        if car.isVertical():
            last = car.getFullCarPosition()[car.carLength - 1]
            if last[0] + 1 > 5 or self.matrix[last[0] + 1][last[1]] != ".":
                print("Cant move down a car might be blocking or it is out of bounds")
                return False
            else:
                # swap idk and change the fuel
                return True
        print("Car is not vertical!")
        return False

    def moveRight(self, car):
        board = self.clone()
        carNewBoard = board.getCarName(car.carName)
        isMovable = self.isMoveableRight(car)
        if isMovable:
            fullCarPosition = carNewBoard.getFullCarPosition()
            board.matrix[fullCarPosition[0][0]][fullCarPosition[0][1]] = "."
            board.matrix[fullCarPosition[-1][0]][fullCarPosition[-1][1] + 1] = car.carName
            newFullCarPosition = []
            for pos in fullCarPosition:
                pos = (pos[0], pos[1] + 1)
                newFullCarPosition.append(pos)
            carNewBoard.setCarFullPosition(newFullCarPosition)
            car.startPos = newFullCarPosition[0]
            if carNewBoard.carFullPosition[car.carLength - 1][0] == 2 and \
                    carNewBoard.carFullPosition[car.carLength - 1][1] == 5:
                board.remove(carNewBoard)
                board.cars.remove(carNewBoard)
                print("Car is removed because it is the exit position ", carNewBoard.carName)
                return board  # goal state
            return board
        else:
            return self

    def moveLeft(self, car):
        isMovable = self.isMoveableLeft(car)
        if isMovable:
            board = self.clone()
            carNewBoard = board.getCarName(car.carName)
            fullCarPosition = carNewBoard.getFullCarPosition()
            board.matrix[fullCarPosition[0][0]][fullCarPosition[0][1] - 1] = car.carName
            board.matrix[fullCarPosition[-1][0]][fullCarPosition[-1][1]] = "."
            newFullCarPosition = []
            for pos in fullCarPosition:
                pos = (pos[0], pos[1] - 1)
                newFullCarPosition.append(pos)
            carNewBoard.setCarFullPosition(newFullCarPosition)
            car.startPos = newFullCarPosition[0]
            return board
        else:
            return self

    def moveUp(self, car):
        isMovable = self.isMoveableUp(car)
        if isMovable:
            board = self.clone()
            carNewBoard = board.getCarName(car.carName)
            fullCarPosition = carNewBoard.getFullCarPosition()
            board.matrix[fullCarPosition[0][0] - 1][fullCarPosition[0][1]] = car.carName
            board.matrix[fullCarPosition[-1][0]][fullCarPosition[-1][1]] = "."
            newFullCarPosition = []
            for pos in fullCarPosition:
                pos = (pos[0] - 1, pos[1])
                newFullCarPosition.append(pos)
            carNewBoard.setCarFullPosition(newFullCarPosition)
            car.startPos = newFullCarPosition[0]
            return board
        else:
            return self

    def moveDown(self, car):
        isMovable = self.isMoveableDown(car)
        if isMovable:
            board = self.clone()
            carNewBoard = board.getCarName(car.carName)
            fullCarPosition = carNewBoard.getFullCarPosition()
            board.matrix[fullCarPosition[0][0]][fullCarPosition[0][1]] = "."
            board.matrix[fullCarPosition[-1][0] + 1][fullCarPosition[-1][1]] = car.carName
            newFullCarPosition = []
            for pos in fullCarPosition:
                pos = (pos[0] + 1, pos[1])
                newFullCarPosition.append(pos)
            carNewBoard.setCarFullPosition(newFullCarPosition)
            car.startPos = newFullCarPosition[0]
            return board
        else:
            return self

    def remove(self, car):
        for i in range(len(car.getFullCarPosition())):
            x = car.getFullCarPosition()[i][0]
            y = car.getFullCarPosition()[i][1]
            self.matrix[x][y] = "."
        return self

    def createCars(self):
        count = 0
        listOfKeys = list(self.getCarsInfo().keys())
        for values in self.getCarsInfo().values():
            if not values[1]:
                self.cars.append(Car((listOfKeys[count]), "Vertical", values[2], values[0]))
            else:
                self.cars.append(Car((listOfKeys[count]), "Horizontal", values[2], values[0]))
            count += 1
        return self.cars

    def matrixform(self):
        for row in self.matrix:
            for col in row:
                print(col, end=" ")
            print(" ")

    def MakingMatrix(self, puzzles):
        ctr = 0
        for i in range(6):
            for x in range(6):
                self.matrix[i][x] = puzzles[ctr]
                ctr = ctr + 1
