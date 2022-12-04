from Board import Board
from UCS import UCS
from State import State
from GBFS import GBFS
from AorAStart import AAS


def ReadingFile(file):
    f = open(file, 'r')
    puzzles = []
    for lines in f:
        if not lines.startswith("#") and lines.strip():
            puzzles.append(lines.replace("\n", '').strip())
    return puzzles


def getAllFuel(line):
    keyLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                  'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    dict = {key: 100 for key in keyLetters}
    eachLine = [x for x in line]
    str = ""
    for character in range(len(eachLine)):
        if eachLine[character].isdigit():
            if not eachLine[character - 1].isdigit():
                tup = tuple(eachLine)
                keyDict = tup[character - 1]
            str += eachLine[character]
            if character != len(eachLine) - 1:
                if eachLine[character + 1].isdigit():
                    continue
            fuel = int(str)
            dict[keyDict] = fuel
            str = ""
    return dict


def getFuel(line, carName):
    dict = getAllFuel(line)
    return dict[carName]


def setAllFuel(line):
    board = Board(line)
    dict = getAllFuel(line)
    for key in dict:
        for i in range(len(board.cars)):
            if board.cars[i].name == key:
                board.cars[i].fuel = dict[key]
            continue
    return board


puzzles = ReadingFile("sample-input.txt")
solvepuzzle = puzzles[0]
board = setAllFuel(solvepuzzle)
print("--------------------------------------------------------------------------------")
print("Initial board configuration :", solvepuzzle)
print()
print("!")
board.matrixform()
print("")
print("Car fuel available: ", end="")
for i in board.cars:
    print(i.name, ":", i.fuel, ",", end=" ")
print("")
state = State(1, 0, None, board)
soso = UCS()
soso.Solve(state)
print("--------------------------------------------------------------------------------")