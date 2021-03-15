class Road:
    def __init__(self,params):
        self.ime = params["ime"]
        self.start = params["start"]
        self.end = params["end"]
        self.edgeWeight = params["edgeWeight"]
        self.numCars = 0
    
    def __str__(self):
        return "Ime:{} Start:{} End:{} EdgeWeight:{} ".format(self.ime, self.start, self.end, self.edgeWeight)