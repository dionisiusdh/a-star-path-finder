from graph import *
from node import *
import networkx as nx
import matplotlib.pyplot as plt

def visualize(graph, path):
    # melakukan visualisasi dari sebuah graph
    # sekaligus memvisualisasikan path dari algoritma A*
    G = nx.Graph()

    for node in graph.nodes:
        G.add_node(node.name)
    
    for i in range(len(graph.adjm)):
        for j in range(i+1, len(graph.adjm)):
            if (graph.adjm[i][j] == 1):
                G.add_edge(graph.nodes[i].name, graph.nodes[j].name)

    nx.draw(G, with_labels=1)
    plt.show()