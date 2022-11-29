from queue import PriorityQueue
class AAndAStartPathFinding:
    def __init__(self, state):
        self.state = state
        self.board = self.state.board

    def getNeighborCars(self, car):
        neighboursCarName = []
        neighboursCarObj = []
        fullCarPosition = car.ReturnAllCarPositions()
        for pos in fullCarPosition:
            for x in range(1, 3):
                for y in range(1, 3):
                    tempTuple = (pos[0] + x, pos[1] + y)
                    carInTempTuple = self.board.getCarNameAtLocation(tempTuple)
                    if neighboursCarName.__contains__(carInTempTuple) or carInTempTuple == "." or tempTuple[0] < 0 or \
                            tempTuple[0] > 5 or tempTuple[1] < 0 or tempTuple[1] > 5:
                        continue
                    else:
                        neighboursCarName.append(carInTempTuple)
                        neighboursCarObj.append(self.board.getCarName(carInTempTuple))
        return neighboursCarName

    def findPath(self):
        openList = PriorityQueue
        closedList = []