from graph import *
from node import *
import networkx as nx
import matplotlib.pyplot as plt

def visualize(graph, path):
    # melakukan visualisasi dari sebuah graph
    # sekaligus memvisualisasikan path dari algoritma A*
    # G = nx.Graph()

    # for node in graph.nodes:
    #     G.add_node(node.name)
    
    # for i in range(len(graph.adjm)):
    #     for j in range(i+1, len(graph.adjm)):
    #         if (graph.adjm[i][j] == 1):
    #             G.add_edge(graph.nodes[i].name, graph.nodes[j].name, weight=5)

    # pos = nx.spring_layout(G, k=0.5, iterations=20)

    # nx.draw(G, with_labels=1)
    plt.figure(figsize=(8,6))
    plt.margins(.2, .2)
    plt.tight_layout()

    G=nx.Graph()

    nodelist = []
    edgelist = []

    for node in graph.nodes:
         nodelist.append(node.name)
         G.add_node(node.name)

    for i in range(len(graph.adjm)):
        for j in range(i+1, len(graph.adjm)):
            if (graph.adjm[i][j] == 1):
                edgelist.append((graph.nodes[i].name, graph.nodes[j].name))

    pos=nx.spring_layout(G) # positions for all nodes

    # # nodes
    nx.draw_networkx_nodes(G,pos,
                         nodelist=nodelist,
                         node_color='#ffff99',
                         node_size=1500,
                         alpha=1)

    # edges
    nx.draw_networkx_edges(G,pos,
                        edgelist=edgelist,
                        width=1,alpha=.5,edge_color='black')


    # some math labels
    labels={}

    for i in range(0, len(nodelist)):
        labels[nodelist[i]] = nodelist[i]

    nx.draw_networkx_labels(G,pos,labels,font_size=7)

    plt.show()