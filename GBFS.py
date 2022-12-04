from Node import Node
from State import State
from queue import PriorityQueue
import timeit


class GBFS:

    def __init__(self):
        self.matrix = None

    def retracePath(self, state):
        path = []
        tempState = state
        while tempState.parent is not None:
            path.append(tempState)
            tempState = tempState.parent
        path.reverse()
        return path

    def Solve(self, state,heu):
        start = timeit.default_timer()
        node = Node(state, None, 0)
        queue = PriorityQueue()
        queue.put((node.state.h_CostMe, node))
        explored = set()
        solutionfound = True
        oldMatrix = state
        while not queue.empty() and solutionfound:
            if oldMatrix.board.isGoalPosition(oldMatrix.board.getCarName("A")):
                # path = self.retracePath(oldMatrix)
                # stop = timeit.default_timer()
                # timing = stop - start
                # print("Runtime: ", round(timing, 3), " seconds")
                # print("Search path length:", len(queue.queue), "states")
                # print("Solution path length:", len(path), "moves")
                # print("")
                # for i in range(len(path)):
                #     print(path[i].board.makingString(), end="")
                #     name = path[i].board.movedCar
                #     for x in name:
                #         fuel = path[i].board.getCarName(x)
                #         if fuel is None:
                #             continue
                #         print("", fuel.name, fuel.fuel, end="")
                #     print("\n")
                #     print("!", end=" ")
                # for name in oldMatrix.board.movedCar:
                #     car = oldMatrix.board.getCarName(name)
                #     if car is None:
                #         continue
                #     print(car.name, car.fuel, end=" ")
                # print("\n")
                # oldMatrix.board.matrixform()
                break
            node1 = queue.get()
            explored.add(node1)
            if node1[1].state.board.getCarNameAtLocation(2, 5) != "A":
                for x in node1[1].state.board.cars:
                    if x.isVertical():
                        boardup = node1[1].state.board
                        while boardup.isMoveableUp(boardup.getCarName(x.name)) and boardup.getCarName(x.name).hasFuel():
                            boardup = boardup.moveUp(boardup.getCarName(x.name))
                            state1 = State(heu, 0, node1[1].state, boardup)
                            child = Node(state1, node1[1].state, state1.h_CostMe)
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
                                queue.put((child.state.h_Cost(1, child.state.board), child))
                        boarddown = node1[1].state.board
                        while boarddown.isMoveableDown(boarddown.getCarName(x.name)) and boarddown.getCarName(
                                x.name).hasFuel():
                            boarddown = boarddown.moveDown(boarddown.getCarName(x.name))
                            state1 = State(heu, 0, node1[1].state, boarddown)
                            child = Node(state1, node1[1].state, state1.h_CostMe)
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
                                queue.put((child.state.h_Cost(1, child.state.board), child))
                    if x.isHorizontal():
                        boardright = node1[1].state.board
                        while boardright.isMoveableRight(boardright.getCarName(x.name)) and boardright.getCarName(
                                x.name).hasFuel():
                            boardright = boardright.moveRight(boardright.getCarName(x.name))
                            state1 = State(heu, 0, node1[1].state, boardright)
                            child = Node(state1, node1[1].state, state1.h_CostMe)
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
                                queue.put((child.state.h_Cost(1, child.state.board), child))
                            if boardright.getCarName(x.name) not in boardright.cars:
                                oldMatrix = state1
                                break
                        boardleft = node1[1].state.board
                        while boardleft.isMoveableLeft(boardleft.getCarName(x.name)) and boardleft.getCarName(
                                x.name).hasFuel():
                            boardleft = boardleft.moveLeft(boardleft.getCarName(x.name))
                            state1 = State(heu, 0, node1[1].state, boardleft)
                            child = Node(state1,  node1[1].state, state1.h_CostMe)
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
                                queue.put((child.state.h_Cost(1, child.state.board), child))
        # print("-----------SEARCH-------------")
        for i in explored:
            counter = 1
            if len(explored) != counter:
                print(0, 0, i[1].state.h_CostMe, i[1].state.board.makingString(), end="")
                name = i[1].state.board.movedCar
                counter += 1
                for x in name:
                    fuel = i[1].state.board.getCarName(x)
                    if fuel is None:
                        continue
                    print("", fuel.name, fuel.fuel, end="")
                print("\n")
        if queue.empty():
            print("Sorry, could not solve the puzzle as specified.")
            print("Error: no solution found")
            stop = timeit.default_timer()
            timing = stop - start
            print("Runtime: ", round(timing, 3), " seconds")
