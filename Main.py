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


puzzles = ReadingFile("sample-input.txt")
board = Board(puzzles[3])
# for i in board.cars:
#     print(i.name, end="")
# print("")
board.matrixform()
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
