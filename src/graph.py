"""
Definisi kelas Graph dan method yang berhubungan dengan pemrosesan graph
"""
from node import *

class Graph:
    def __init__ (self, size):
        self.nodes = []
        self.adjm = [] #[[0 for j in range(size)] for i in range(size)] # Adjacency matrix
    
    def addNode(self, N):
        # Menambahkan node N ke Graph
        self.nodes.append(N)

    def addAdjm(self, value):
        self.adjm.append(value)

    def printGraph(self):
        # Mencetak graph ke layar
        for n in self.nodes:
            n.printNode()
        
        print("Adjacency Matrix: ")
        self.printAdjm()
    
    def printAdjm(self):
        for row in self.adjm:
            print(row)
    
def makeGraphFromTxt(file_name):
    # Membuat graph dari file eksternal .txt
    # Variabel
    lines = []
    all_nodes = []
    
    # Open dan read file
    f = open(f"../test/{file_name}.txt", "r")

    # Iterate line file
    lines = f.readlines()

    size = int(lines[0])

    graph = Graph(size)

    # Add adjacency matrix ke graph
    for i in range(size+1, len(lines)):
        line = lines[i].split(" ")

        for i in range(len(line)):
            line[i] = int(line[i].replace(" ", "").replace(".", "").replace("\n", ""))

        graph.addAdjm(line)

    # Add node ke graph
    for i in range(1, size+1):
        line = lines[i].split(" ")

        for i in range(len(line)):
            line[i] = line[i].replace(" ", "").replace(".", "").replace("\n", "")

        curr_node = Node(line[0], int(line[1]), int(line[2]))

        graph.addNode(curr_node)
    
    # Add edge ke graph
    for i in range(len(graph.adjm)):
       for j in range(len(graph.adjm)):
           if (graph.adjm[i][j] != 0):
            (graph.nodes[i]).addNeighbors(graph.nodes[j], graph.adjm[i][j])


    return graph