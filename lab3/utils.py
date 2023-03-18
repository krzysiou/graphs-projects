import igraph as ig
import matplotlib.pyplot as plt
import sys
import numpy as np

def generateEdgesList(neighbourList):
    edges = []

    for index, neighbours in enumerate(neighbourList):
        edges.extend(
            (index, neighbour - 1) for neighbour in neighbours if neighbour - 1 < index
        )

    return edges

def drawGraph(neighbourList, numOfEdges):
    g = ig.Graph(len(neighbourList), generateEdgesList(neighbourList))
    g.vs["id"] = [i + 1 for i in range(len(neighbourList))]
    g.es["value"] = [i + 1 for i in range(numOfEdges)]

    _, ax = plt.subplots()
    ig.plot(
        g,
        target=ax,
        layout="circle",
        vertex_size=0.25,
        vertex_color="#d9d9ff",
        vertex_frame_width=1.0,
        vertex_frame_color="#1414ff",
        vertex_label_size=16.0,
        vertex_label=g.vs["id"],
        edge_width=2,
        edge_color="#000",
        edge_label=g.es["value"],
        edge_label_color = "#FF0000",
    )

    plt.show()

def convertEdgesToNeighbourList(edges):
    maxList = map(max, edges)
    
    nodeNumber = max(maxList)
    neighbourList = []

    for _ in range(nodeNumber + 1):
        neighbourList.append([])

    for edge in edges:
        neighbourList[edge[0]].append(edge[1] + 1)
        neighbourList[edge[1]].append(edge[0] + 1)

    # print(neighbourList)

    return neighbourList

def generateGraphNL(n, l):
    if l < 0 or l > n * (n - 1) / 2: 
        sys.exit("Wrong randomization arguments")
    
    edges = []

    for i in range(l):
        while True:
            rand1 = np.random.randint(0, n)
            rand2 = rand1
            
            while rand1 == rand2:
                rand2 = np.random.randint(0, n)
            
            edge = [rand1, rand2]
            edge.sort()

            if edge not in edges:
                edges.append(edge)
                break

    return convertEdgesToNeighbourList(edges)

def generateConnectedGraph(n, l):
    isConnected = False
    while not isConnected:
        neighbourList = generateGraphNL(n, l)
        isConnected = False if min([len(neighbourList[i]) for i in range(len(neighbourList))]) == 0 else True
    return neighbourList