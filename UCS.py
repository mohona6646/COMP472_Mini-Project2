from Node import Node
from State import State
from queue import PriorityQueue


class UCS:

    def __init__(self):
        self.zebi = ''

    def Solve(self, state):
        node = Node(state, None, None, 0)
        queue = PriorityQueue()
        queue.put((node.state.G_cost(), node))
        explored = set()
        while not queue.empty():
            print(queue.queue)
            node1 = queue.get()
            explored.add(node1)
            print("----------closed list--------------------")
            counter = 1
            for i in explored:
                i[1].state.board.matrixform()
                print("-----------------Matrix ", counter, "--------------")
                counter += 1
            print("\n")
            print("----------closed list--------------------")
            if node1[1].state.board.getCarNameAtLocation(2, 5) != "A":
                for x in node1[1].state.board.cars:
                    print("\n")
                    print(x.name)
                    if x.isVertical():
                        boardup = node1[1].state.board
                        print("----------move up---------------")
                        while boardup.isMoveableUp(boardup.getCarName(x.name)):
                            boardup = boardup.moveUp(boardup.getCarName(x.name))
                            state1 = State(None, node1[1].state.g_Cost, node1[1].state, boardup)
                            child = Node(state1, 1, node1[1].state, node1[1].state.G_cost())
                            child.state.board.matrixform()
                            print('moved up', x.name)
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
                                print("Not added")
                            else:
                                queue.put((child.state.G_cost(), child))
                        print("------------move up-------------")
                        print("-------------------------")
                        boarddown = node1[1].state.board
                        while boarddown.isMoveableDown(boarddown.getCarName(x.name)):
                            print("a7a")
                            boarddown = boarddown.moveDown(boarddown.getCarName(x.name))
                            state1 = State(None, node1[1].state.g_Cost, node1[1].state, boarddown)
                            child = Node(state1, 1, node1[1].state, node1[1].state.G_cost())
                            child.state.board.matrixform()
                            print('moved Down', x.name)
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
                                print("Not added")
                            else:
                                queue.put((child.state.G_cost(), child))

                    print("-------------------------")
                    print("-------------------------")
                    if x.isHorizontal():
                        boardright = node1[1].state.board
                        while boardright.isMoveableRight(boardright.getCarName(x.name)):
                            boardright = boardright.moveRight(boardright.getCarName(x.name))
                            state1 = State(None, node1[1].state.g_Cost, node1[1].state, boardright)
                            child = Node(state1, 1, node1[1].state, node1[1].state.G_cost())
                            child.state.board.matrixform()
                            print('moved right', x.name)
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
                                print("Not added")
                            else:
                                queue.put((child.state.G_cost(), child))
                            car = boardright.getCarName("A")
                            if car not in boardright.cars:
                                break

                        if boardright.getCarName("A") not in boardright.cars:
                            queue.queue.clear()
                            break

                        print("-------------------------")
                        print("-------------------------")
                        boardleft = node1[1].state.board
                        while boardleft.isMoveableLeft(boardleft.getCarName(x.name)):
                            boardleft = boardleft.moveLeft(boardleft.getCarName(x.name))
                            state1 = State(None, node1[1].state.g_Cost, node1[1].state, boardleft)
                            child = Node(state1, 1, node1[1].state, node1[1].state.G_cost())
                            child.state.board.matrixform()
                            print('moved right', x.name)
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
                                print("Not added")
                            else:
                                queue.put((child.state.G_cost(), child))
                        print("-------------------------")
                        print("-------------------------")
        print("LOSER")
        return True
