import sys
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


def generateDigraph(node_count, probability):
    if probability < 0 or probability > 1:
        sys.exit("Wrong randomization arguments")

    edges = []

    while True:
        for i in range(0, node_count):
            for j in range(0, node_count):
                if i != j:
                    rand = np.random.rand()

                    if rand < probability:
                        edges.append([i, j])

        maxList = map(max, edges)
        maxNode = max(maxList)

        if maxNode == node_count - 1:
            break

        edges = []

    return edges
