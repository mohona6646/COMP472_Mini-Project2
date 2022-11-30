from Board import Board
from UCS import UCS
from State import State
from Node import Node


def ReadingFile(file):
    f = open(file, 'r')
    puzzles = []
    for lines in f:
        if not lines.startswith("#") and lines.strip():
            puzzles.append(lines.replace("\n", '').strip())
    return puzzles

#
# def getAllFuel(line):
#     keyLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
#                   'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
#     dict = {key: 100 for key in keyLetters}
#     eachLine = [x for x in line]
#     str = ""
#     for character in range(len(eachLine)):
#         if eachLine[character].isdigit():
#             if not eachLine[character - 1].isdigit():
#                 tup = tuple(eachLine)
#                 keyDict = tup[character - 1]
#             str += eachLine[character]
#             if character != len(eachLine) - 1:
#                 if eachLine[character + 1].isdigit():
#                     continue
#             dict[keyDict] = str
#             str = ""
#     return dict
#
#
# def getFuel(line, carName):
#     dict = getAllFuel(line)
#     return dict[carName]
#
#
# def setAllFuel(line):
#     board = Board(line)
#     dict = getAllFuel(line)
#     for key in dict:
#         for i in range(len(board.cars)):
#             if board.cars[i].name == key:
#                 board.cars[i].fuel = dict[key]
#             continue
#     return board


puzzles = ReadingFile("sample-input.txt")
board = Board(puzzles[0])
# for i in board.cars:
#     print(i.name, end="")
# print("")
# board.matrixform()
# board = setAllFuel(puzzles[4])
#print(board.getCarName("F").fuel)
# car = board.getCarName("SF")
# print(car.fuel)

state = State(0, 0, None, board)
soso= UCS()
soso.Solve(state)
# node=Node(state,1,None,0)
# expolored=set()
# expolored.add((0,node))
# expolored.add((1,node))
# board2 = board.moveDown(board.getCarName("M"))
# for i in board2.cars:
#     print(i.name,end="")
#
# print("")
# print(board2.compareTwoBoards(board2))
# y=board2.makingString()
# l=expolored.pop()
# print(l)
# print("")
# l[1].state.board.matrixform()
# board2.matrixform()
# if y not in l[1].state.board.makingString():
#     print("LOVE")
# expolored.add(l)
# print(expolored)
# state2= State(0,0,state,board2)
# print(state2.G_cost())

# carsInfo = board.getCarsInfo()
# AllCars = board.createCars()
# boardCars = board.CreateNewCars(AllCars)
# board2= board.moveDown(board.getCarName("M"))
# board2.matrixform()
# car2 = board.getCarName("M")
# board2 = board.moveUp(car2)
# board3 = board2.moveRight(board2.getCarName("F"))
# board4 = board3.moveRight(board3.getCarName("F"))
# print(board4.getCarName("F").fuel)
