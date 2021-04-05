from graph import *
from node import *
import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

def visualize(graph, path, dist):
    # melakukan visualisasi dari sebuah graph
    # sekaligus memvisualisasikan path dari algoritma A*
    
    # Matplotlib figure
    plt.figure(figsize=(8,7))
    plt.margins(.2, .2)
    plt.tight_layout()

    # Legend
    start_patch = mpatches.Patch(color='#BFFF80', label='Starting point')
    end_patch = mpatches.Patch(color='#FF9F80', label='Destination point')
    path_patch = mpatches.Patch(color='#FFFF99', label='Path')
    plt.legend(handles=[start_patch, end_patch, path_patch])

    # Buat graph
    G = nx.DiGraph()

    # List dari seluruh node
    all_nodes = []                          

    # Path element
    edgelist_path = []                      # Menyimpan edge yang termasuk ke dalam path
    start = [path[0]]                       # Starting node
    end = [path[len(path)-1]]               # Node tujuan
    other_path = [node for node in path if node not in start and node not in end]

    # Non-path element
    nodelist = []
    edgelist = []

    # Ambil list of nodes dan edges
    for i in range(len(path)-1):
        edgelist_path.append((path[i], path[i+1]))

    for node in graph.nodes:
        if (node.name not in path):
            nodelist.append(node.name)
        G.add_node(node.name)
        all_nodes.append(node.name)

    for i in range(len(graph.adjm)):
        for j in range(i+1, len(graph.adjm)):
            if (graph.adjm[i][j] == 1):
                if ((graph.nodes[i].name, graph.nodes[j].name) not in edgelist_path and (graph.nodes[j].name, graph.nodes[i].name) not in edgelist_path):
                    edgelist.append((graph.nodes[i].name, graph.nodes[j].name))

    # Ambil posisi dar node yang ada
    pos=nx.spring_layout(G) 

    # Draw nodes
    nx.draw_networkx_nodes(G,pos,
                         nodelist=start,
                         node_color='#BFFF80',
                         node_size=300,
                         alpha=1)
    
    nx.draw_networkx_nodes(G,pos,
                         nodelist=end,
                         node_color='#FF9F80',
                         node_size=300,
                         alpha=1)

    nx.draw_networkx_nodes(G,pos,
                         nodelist=other_path,
                         node_color='#FFFF99',
                         node_size=300,
                         alpha=1)

    nx.draw_networkx_nodes(G,pos,
                         nodelist=nodelist,
                         node_color='#E0DEDD',
                         node_size=300,
                         alpha=1)

    # Draw edges
    nx.draw_networkx_edges(G,pos,
                        edgelist=edgelist_path,
                        width=1,
                        alpha=1,
                        edge_color='red',
                        arrowsize= 10,
                        arrows=True)

    nx.draw_networkx_edges(G,pos,
                        edgelist=edgelist,
                        width=1,
                        alpha=.5,
                        edge_color='black',
                        arrows=False)

    # Draw labels
    labels={}

    for i in range(0, len(all_nodes)):
        labels[all_nodes[i]] = all_nodes[i]

    nx.draw_networkx_labels(G,pos,labels,font_size=7)

    # Set title
    plt.title(f"{start[0]} - {end[0]} : " + "%.2f"%dist + " m", x=0.4, y=0.95)
    # Show
    plt.show()