import pprint
import networkx as nx
import matplotlib.pyplot as plt

pp = pprint.PrettyPrinter()



def parseLine(line, isInt=True):
    if isInt:
        return [int(elem) for elem in line.split()]
    else:
        return line.split()

def readFile(fileName):
    f = open("data/{}.txt".format(fileName),"r")
    params = parseLine(f.readline(), True)

    deadline = params[0]
    numInter = params[1]
    numStreets = params[2]
    numCars = params[3]
    pointPerCar = params[4]

    roads = []
    cars = []
    for i in range(numStreets):
        street = parseLine(f.readline(), False)
        start = int(street[0])
        end = int(street[1])
        ime = street[2]
        edgeWeight = int(street[3])
        road = {
            "start": start,
            "end": end,
            "ime": ime,
            "edgeWeight": edgeWeight
        }
        roads.append(road)
    #pp.pprint(roads)
    for i in range(numCars):
        route = parseLine(f.readline(), False) 
        #Go brisham prviot posho samo kazhue kolku ulici proagja, toa mozhe samo so len(roads)
        route.pop(0)
        cars.append(route)        

    return deadline, numInter, numStreets, numCars, pointPerCar, roads, cars