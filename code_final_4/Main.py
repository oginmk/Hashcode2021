class Main:
    def __init__(self,deadline, numInter, numStreets, numCars, pointPerCar):
        self.deadline = deadline
        self.numInter = numInter
        self.numStreets = numStreets
        self.numCars = numCars
        self.pointPerCar = pointPerCar
        self.roads = []
        self.nodes = []

    def addRoad(self, road):
        self.roads.append(road)
    
    def printRoads(self):
        for i in self.roads:
            print(i)

    def addNode(self,node):
        self.nodes.append(node)
