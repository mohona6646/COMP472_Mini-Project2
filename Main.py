import re

from Board import Board


def ReadingFile(file):
    f = open(file, 'r')
    puzzles = []
    for lines in f:
        if not lines.startswith("#") and lines.strip():
            puzzles.append(lines.replace("\n", '').strip())
    return puzzles


puzzles = ReadingFile("sample-input.txt")
board = Board(puzzles[0])
board.matrixform()
print("\n")
carsInfo = board.getCarsInfo()
AllCars = board.createCars()
boardCars = board.CreateNewCars(AllCars)
car2 = board.getCarName("M")
board2 = board.moveDown(car2)
trial = board2.getCarName("A")
board3 = board2.moveRight(board2.getCarName("A"))
board3.matrixform()
for i in range(len(board3.cars)):
    print(board3.cars[i].carName, end=" ")


print("\n\n")

def getAllFuel(line):
     keyLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
                      'T', 'U', 'V', 'X', 'Y', 'Z']
     dict = {key: None for key in keyLetters}
     eachLine = [x for x  in line]
     str = ""
     for character in range(len(eachLine)):
         if eachLine[character].isdigit():
             if not eachLine[character-1].isdigit():
                 tup = tuple(eachLine)
                 keyDict = tup[character-1]
             str += eachLine[character]
             if character != len(eachLine)-1:
                  if eachLine[character+1].isdigit():
                      continue
             dict[keyDict] = str
             str = ""
     return dict

def getFuel(carName):
    dict = getAllFuel(line)
    return dict[carName]

for line in puzzles:
    print(getFuel('B'))







