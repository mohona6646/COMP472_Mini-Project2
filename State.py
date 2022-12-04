class State:
    def __init__(self, cost, g_Cost, parent, board):
        self.g_Cost = g_Cost
        self.parent = parent
        self.board = board
        self.h_CostMe = self.h_Cost(cost, board)
        self.fCost = self.F_Cost(cost, g_Cost)

    def h_Cost(self, h_cost, board):
        cost = 0
        # h1
        if h_cost == 1:
            carList = []
            car = board.getCarName("A")
            if car not in board.cars:
                self.h_CostMe = 0
                return 0
            carPositions = car.ReturnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarNameAtLocation(2, pos)
                if not carList.__contains__(nextCarName) and nextCarName != ".":
                    cost += 1
        # h2
        elif h_cost == 2:
            car = board.getCarName("A")
            if car not in board.cars:
                self.h_CostMe = 0
                return 0
            carPositions = car.ReturnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarNameAtLocation(2, pos)
                if nextCarName != ".":
                    cost += 1
        # h3
        elif h_cost == 3:
            carList = []
            car = board.getCarName("A")
            if car not in board.cars:
                self.h_CostMe = 0
                return 0
            carPositions = car.ReturnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarNameAtLocation(2, pos)
                if not carList.__contains__(nextCarName) and nextCarName != ".":
                    cost += 1
            cost *= 5
        # h4
        if h_cost == 4:
            car = board.getCarName("A")
            if car not in board.cars:
                self.h_CostMe = 0
                return 0
            lastindex = car.allCarPositions[len(car.allCarPositions) - 1]
            distancebetweencarandexit = 5 - lastindex[1]
            cost = distancebetweencarandexit
        return cost

    def G_cost(self):
        if self.parent is not None:
            parent = self.parent.board
            child = self.board
            if child.movedCar == parent.movedCar:
                self.g_Cost = self.parent.g_Cost
            else:
                self.g_Cost = self.parent.g_Cost + 1
        return self.g_Cost

    def F_Cost(self, h_Cost, g_Cost):
        cost = 0
        if self.h_CostMe == 1:
            cost = self.h_Cost(1, self.board) + self.G_cost()
        if self.h_CostMe == 2:
            cost = self.h_Cost(2, self.board) + self.G_cost()
        if self.h_CostMe == 3:
            cost = self.h_Cost(3, self.board) + self.G_cost()
        if self.h_CostMe == 4:
            cost = self.h_Cost(4, self.board) + self.G_cost()
        return cost
