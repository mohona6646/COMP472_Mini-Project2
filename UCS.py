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
            print(queue)
            node1 = queue.get()
            explored.add(node1)
            for i in explored:
                print("------------------------------")
                i[1].state.board.matrixform()
            print("\n")
            if node1[1].state.board.getCarNameAtLocation(2, 5) != "A":
                for x in node1[1].state.board.cars:
                    print("\n")
                    print(x.name)
                    if x.isVertical():
                        if node1[1].state.board.isMoveableUp(x):
                            y = node1[1].state.board.moveUp(x)
                            state1 = State(None, node1[1].state.g_Cost, node1[1].state, y)
                            child = Node(state1, 1, node1[1].state, node1[1].state.G_cost())
                            child.state.board.matrixform()
                            # for i in child.state.board.cars:
                            #     print(i.name,end="")
                            print('moved up', x.name)
                            isinopen=False
                            isinclosed=False
                            for k in explored:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinclosed=True
                                    break
                            for k in queue.queue:
                                if k[1].state.board.compareTwoBoards(child.state.board):
                                    isinopen = True
                                    break
                            if isinclosed or isinopen:
                              print("Not added")
                            else:
                                queue.put((child.state.G_cost(), child))
                                # queue.put((child.state.G_cost(), child))


                                    # if child.state.board.makingString() not in nodes[
                            #     1].state.board.makingString() and child.state.board.makingString() not in queue.queue:
                            #     queue.put((child.state.G_cost(), child))
                            #     explored.add(nodes)
                            # elif child.state in queue.queue:
                            #     holder = queue.get(child.state)
                            #     if child.state.gCost < holder.state.gCost:
                            #         queue.put(holder, holder.state.gCost)
                        if node1[1].state.board.isMoveableDown(x):
                            y = node1[1].state.board.moveDown(x)
                            state1 = State(None, node1[1].state.g_Cost, node1[1].state, y)
                            child = Node(state1, 1, node1[1].state, node1[1].state.G_cost())
                            child.state.board.matrixform()
                            # for i in child.state.board.cars:
                            #     print(i.name, end="")
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
                            # if child.state.board.makingString() not in nodes[
                            #     1].state.board.makingString() and child.state.board.makingString() not in queue.queue:
                            #     queue.put((child.state.G_cost(), child))
                            #     explored.add(nodes)
                            # elif child.state in queue.queue:
                            #     holder = queue.get(child.state)
                            #     if child.state.gCost < holder.state.gCost:
                            #         queue.put(holder, holder.state.gCost)

                    if x.isHorizontal():
                        if node1[1].state.board.isMoveableRight(x):
                            y = node1[1].state.board.moveRight(x)
                            car = y.getCarName("A")
                            state1 = State(None, node1[1].state.g_Cost, node1[1].state, y)
                            child = Node(state1, 1, node1[1].state, node1[1].state.G_cost())
                            child.state.board.matrixform()
                            # for i in child.state.board.cars:
                            #     print(i.name, end="")
                            print('moved right', x.name)
                            if car not in y.cars:
                                queue.queue.clear()
                                break
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
                            # if child.state.board.makingString() not in nodes[
                            #     1].state.board.makingString() and child.state.board.makingString() not in queue.queue:
                            #     queue.put((child.state.G_cost(), child))
                            #     explored.add(nodes)
                            # elif child.state in queue.queue:
                            #     holder = queue.get(child.state)
                            #     if child.state.gCost < holder.state.gCost:
                            #         queue.put(holder, holder.state.gCost)
                        if node1[1].state.board.isMoveableLeft(x):
                            y = state.board.moveLeft(x)
                            state1 = State(None, node1[1].state.g_Cost, node1[1].state, y)
                            child = Node(state1, 1, node1[1].state, node1[1].state.G_cost())
                            child.state.board.matrixform()
                            # for i in child.state.board.cars:
                            #     print(i.name,end="")
                            print('moved left', x.name)
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
                            # if child.state.board.makingString() not in nodes[
                            #     1].state.board.makingString() and child.state.board.makingString() not in queue.queue:
                            #     queue.put((child.state.G_cost(), child))
                            #     explored.add(nodes)
                            # elif child.state in queue.queue:
                            #     holder = queue.get(child.state)
                            #     if child.state.gCost < holder.state.gCost:
                            #         queue.put(holder, holder.state.gCost)
