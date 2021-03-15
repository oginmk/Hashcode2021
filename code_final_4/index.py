from inputFile import readFile 
from RoadClass import Road
from Node import Node
from Main import Main
import pprint 
pp = pprint.PrettyPrinter()
fileNames = ["a","b","c","d","e","f"]
#fileNames = ["a"]
if __name__ == "__main__":
    for fileName in fileNames:
        deadline, numInter, numStreets, numCars, pointPerCar, roads, cars = readFile(fileName)
        #pp.pprint(roads)

        main = Main(deadline, numInter, numStreets, numCars, pointPerCar)
        #flat_list = [item for sublist in cars for item in sublist]
        for road in roads:
            newRoad = Road(road)
            #print(newRoad.pati)
            main.addRoad(newRoad)

        #main.printRoads()
        
        nodeIndexes = []
        nodes = {} 
        koristeniPatishta = []
        brojNodesSoSemafori = 0

        for road in main.roads:
            if road.start not in nodes.keys():
                nodeIndexes.append(road.start)
            elif road.end not in nodes.keys():
                nodeIndexes.append(road.end)
            
        for i in nodeIndexes:
            nodes[i] = {
                "vlezni":[],
                "izlezni":[]
            }
        for road in main.roads:
            nodes[road.start]["izlezni"].append(road)
            nodes[road.end]["vlezni"].append(road)

        for key in nodes.keys():
            newNode = Node(key, nodes[key])
            newNode.presmetuvanje()
            if len(newNode.semafori) > 0:
                brojNodesSoSemafori = brojNodesSoSemafori + 1

            main.addNode(newNode)

        for node in main.nodes:
            print(node)
        f = open('outputs/{}_solution.txt'.format(fileName), "w")
        f.write("{}\n".format(brojNodesSoSemafori))
        for i in main.nodes:
            f.write("{}\n".format(i))