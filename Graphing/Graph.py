class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}   #where the key of the dictionary is Vertex， and the value is the weight of the edge

    def addNeighbour(self, nbr, weight=0):
        self.connectedTo[nbr] = weight

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):   #nbr of type Vertex
        return self.connectedTo[nbr]

    def __str__(self):
        return str(self.id) + ' connected to: ' + str([x.id for x in self.connectedTo])

class Graph:
    # implement graph as an adjency list

    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, vert):
        newVertex = Vertex(vert)
        self.vertList[vert] = newVertex
        self.numVertices += 1

    def addEdge(self, fromVert, toVert, weight=0):
        if fromVert not in self.vertList:
            self.addVertex(fromVert)
        if toVert not in self.vertList:
            self.addVertex(toVert)
        self.vertList[fromVert].addNeighbour(self.vertList[toVert],weight)
        self.vertList[toVert].addNeighbour(self.vertList[fromVert],weight)
        # should I add this two way connection?
    def getVertex(self, vertKey):
        if vertKey in self.vertList:
            return self.vertList[vertKey]
        else:
            return None

    def getVertices():
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())
        # this allows us to use in method, like for object in Graph, meaning for object in self.vertList.values()

    def __contains__(self, n):
        return n in self.vertList



