from graph import *
from node import *

G = Graph(3)
N1 = Node("A", -6.89006959981307, 107.60966824339609)
N2 = Node("B", -6.890100644204194, 107.6106636788004)
N3 = Node("C", 3, 2)

N1.addNeighbors(N2, 200)
N1.addNeighbors(N3, 400)
N2.addNeighbors(N1, 200)
N3.addNeighbors(N1, 400)

G.addNode(N1)
G.addNode(N2)
G.addNode(N3)

G2 = makeGraphFromTxt("1")
G2.printGraph()

# haversineDistance(N1, N2)