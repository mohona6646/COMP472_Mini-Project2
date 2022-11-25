class State:
    def __init__(self, h_Cost, g_Cost, parent, board):
        self.g_Cost = g_Cost
        self.parent = parent
        self.board = board
        self.h_Cost = self.h_Cost(h_Cost, board)
        self.fCost = self.h_Cost + self.g_Cost

    def h_Cost(self, h_Cost, board):
        cost = 0
        #h1
        if h_Cost == 1:
            carList = []
            car = board.getCarName("A")
            carPositions = car.ReturnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarNameAtLocation(2, pos)
                if not carList.__contains__(nextCarName) and nextCarName != ".":
                    cost += 1
        #h2
        elif h_Cost == 2:
            car = board.getCarName("A")
            carPositions = car.ReturnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarNameAtLocation(2, pos)
                if nextCarName != ".":
                    cost += 1
        #h3
        elif h_Cost == 3:
            carList = []
            car = board.getCarName("A")
            carPositions = car.ReturnAllCarPositions()
            for pos in range(carPositions[-1][1] + 1, 6):
                nextCarName = board.getCarNameAtLocation(2, pos)
                if not carList.__contains__(nextCarName) and nextCarName != ".":
                    cost += 1
            cost *= 5  # 5 is set arbitrarily and should be adjusted after experimentation

        #h4

        return cost

    def G_cost(self):
        if self.parent.board is not None:
            parent = self.parent.board
            child = self.board
            if child.movedCar == parent.movedCar:
                self.g_Cost = self.parent.g_Cost
            else:
                self.g_Cost = self.parent.g_Cost + 1
