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
