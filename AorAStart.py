from queue import PriorityQueue
from Node import Node
from State import State
import timeit


class AAS:
    def retracePath(self, state):
        path = []
        tempState = state
        while tempState.parent is not None:
            path.append(tempState)
            tempState = tempState.parent
        path.reverse()
        return path

    def Solve(self, state):
        start = timeit.default_timer()
        node = Node(state, None, None, 0)
        queue = PriorityQueue()
        queue.put((node.state.fCost, node))
        explored = set()
        solutionfound = True
        oldMatrix = state
        print("")
        while not queue.empty() and solutionfound:
            if oldMatrix.board.isGoalPosition(oldMatrix.board.getCarName("A")):
                path = self.retracePath(oldMatrix)
                stop = timeit.default_timer()
                timing = stop - start
                print("Runtime: ", round(timing, 3), " seconds")
                print("Search path length:", len(queue.queue), "states")
                print("Solution path length:", len(path), "moves")
                print("")
                for i in range(len(path)):
                    print(path[i].board.makingString(), end="")
                    name = path[i].board.movedCar
                    for x in name:
                        fuel = path[i].board.getCarName(x)
                        if fuel is None:
                            continue
                        print("", fuel.name, fuel.fuel, end="")
                    print("\n")
                print("!", end=" ")
                for name in oldMatrix.board.movedCar:
                    car = oldMatrix.board.getCarName(name)
                    if car is None:
                        continue
                    print(car.name, car.fuel, end=" ")
                print("\n")
                oldMatrix.board.matrixform()
                break
            node1 = queue.get()
            explored.add(node1)
            if node1[1].state.board.getCarNameAtLocation(2, 5) != "A":
                for x in node1[1].state.board.cars:
                    if x.isVertical():
                        boardup = node1[1].state.board
                        while boardup.isMoveableUp(boardup.getCarName(x.name)) and boardup.getCarName(x.name).hasFuel():
                            boardup = boardup.moveUp(boardup.getCarName(x.name))
                            state1 = State(1, 1, node1[1].state, boardup)
                            child = Node(state1, 1, node1[1].state, state1.fCost)
                            isinopen = False
                            isinclosed = False
                            for k in explored:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinclosed = True
                                    break
                            for k in queue.queue:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinopen = True
                                    break
                            if isinclosed or isinopen:
                                break
                            else:
                                queue.put((child.state.fCost, child))
                        boarddown = node1[1].state.board
                        while boarddown.isMoveableDown(boarddown.getCarName(x.name)) and boarddown.getCarName(
                                x.name).hasFuel():
                            boarddown = boarddown.moveDown(boarddown.getCarName(x.name))
                            state1 = State(1, 1, node1[1].state, boarddown)
                            child = Node(state1, 1, node1[1].state, state1.fCost)
                            isinopen = False
                            isinclosed = False
                            for k in explored:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinclosed = True
                                    break
                            for k in queue.queue:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinopen = True
                                    break
                            if isinclosed or isinopen:
                                break
                            else:
                                queue.put((child.state.fCost, child))
                    if x.isHorizontal():
                        boardright = node1[1].state.board
                        while boardright.isMoveableRight(boardright.getCarName(x.name)) and boardright.getCarName(
                                x.name).hasFuel():
                            boardright = boardright.moveRight(boardright.getCarName(x.name))
                            state1 = State(1, 1, node1[1].state, boardright)
                            child = Node(state1, 1, node1[1].state, state1.fCost)
                            isinopen = False
                            isinclosed = False
                            for k in explored:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinclosed = True
                                    break
                            for k in queue.queue:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinopen = True
                                    break
                            if isinclosed or isinopen:
                                break
                            else:
                                queue.put((child.state.fCost, child))
                            if boardright.getCarName(x.name) not in boardright.cars:
                                oldMatrix = state1
                                break
                        boardleft = node1[1].state.board
                        while boardleft.isMoveableLeft(boardleft.getCarName(x.name)) and boardleft.getCarName(
                                x.name).hasFuel():
                            boardleft = boardleft.moveLeft(boardleft.getCarName(x.name))
                            state1 = State(1, 1, node1[1].state, boardleft)
                            child = Node(state1, 1, node1[1].state, state1.fCost)
                            isinopen = False
                            isinclosed = False
                            for k in explored:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinclosed = True
                                    break
                            for k in queue.queue:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinopen = True
                                    break
                            if isinclosed or isinopen:
                                break
                            else:
                                queue.put((child.state.fCost, child))
        if queue.empty():
            stop = timeit.default_timer()
            timing = stop - start
            print("")
            print("Sorry, could not solve the puzzle as specified.")
            print("Error: no solution found")
            print("")
            print("Runtime: ", round(timing, 3), " seconds")
