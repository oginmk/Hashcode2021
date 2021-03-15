class Node:
    def __init__(self,index, node):
        self.index = index
        self.roadsIn = node["vlezni"]
        self.roadsOut = node["izlezni"]
        self.semafori = []

    def presmetuvanje(self):
        vkupno = 0
        for road in self.roadsIn:
            vkupno = vkupno + road.edgeWeight

        vkupno = round(vkupno / len(self.roadsIn))
        if len(self.roadsIn) == 1:
            self.semafori = [(self.roadsIn[0].ime, 1)]
        else: 
            for road in self.roadsIn:
                self.semafori.append((road.ime, 3))
    
    def __str__(self):
        string ="{}\n{}\n".format(self.index, len(self.semafori))
        for index, semafor in enumerate(self.semafori):
            string+= "{} {}".format(semafor[0], semafor[1])
            if index < len(self.semafori)-1:
                string+= "\n"
        return string