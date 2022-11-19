import queue as queue
from CarClass import Car
from Board import Board


def ReadingFile(file):
    f = open(file, 'r')
    puzzles = []
    for lines in f:
        if not lines.startswith("#") and lines.strip():
            puzzles.append(lines.replace("\n", '').strip())
    return puzzles


def printMatrix(board, puzzles):
    ctr = 0
    for i in range(6):
        for x in range(6):
            board.matrix[i][x] = puzzles[ctr]
            ctr = ctr + 1


def matrixform(board):
    for row in board.matrix:
        for col in row:
            print(col, end=" ")
        print(" ")


def createCars(x):  # have to add the fuel once we figure it out
    carList = []
    count = 0
    listOfKeys = list(x.keys())
    for values in x.values():
        if not values[1]:
            carList.append(Car((listOfKeys[count]), "Vertical", values[2], values[0]))

        else:
            carList.append(Car((listOfKeys[count]), "Horizontal", values[2], values[0]))
        count += 1
    return carList


puzzles = ReadingFile("sample-input.txt")
board = Board()
newCars = {}
printMatrix(board, puzzles[1])
matrixform(board)
print("\n")
carsInfo = board.getCarsInfo()
AllCars = createCars(carsInfo)
boardCars=board.CreateNewCars(AllCars)
trial=board.getCarName("A")
# do the swap method
# get the fuel
