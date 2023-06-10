import numpy as np

def convertEdgesToNeighbourList(edges):
    maxList = map(max, edges)
    node_count = max(maxList)
    neighbourList = []

    for _ in range(node_count + 1):
        neighbourList.append([])

    for edge in edges:
        neighbourList[edge[0]].append(edge[1])

    return neighbourList

def digraphNLToNM(neighbourList):
    nodes = len(neighbourList)
    matrix = np.zeros((nodes, nodes))
    for i in range(nodes):
        for j in neighbourList[i]:
            matrix[i][j] = 1

    return matrix

def vectorLength(vector):
    result = 0
    for i in vector:
        result+=i**2
    return np.sqrt(result)

