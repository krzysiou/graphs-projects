import sys
import numpy as np
import copy
import random


def generateFlowNetwork(N):
    graphLayers = generateVerticesLayers(N)
    graphEdges = generateGraphEdges(graphLayers)

    return [graphLayers, graphEdges]


def generateVerticesLayers(N):
    graphLayers = {}
    graphLayers[0] = [0]  # s

    count = 1
    for i in range(1, N + 1):
        numberOfVerticesInLayer = random.randint(1, N)
        graphLayers[i] = []
        for j in range(numberOfVerticesInLayer):
            graphLayers[i].append(count)
            count += 1

    graphLayers[N + 1] = [count]  # t
    return graphLayers


def generateGraphEdges(graphLayers):
    edgesList = []
    N = len(graphLayers)
    edgesList.extend([0, i] for i in graphLayers[1])
    for i in range(1, N - 2):
        currentLayerEdges = graphLayers[i]
        nextLayerEdges = graphLayers[i + 1]

        for _ in range(len(currentLayerEdges)):
            randomEdge = [
                random.choice(currentLayerEdges),
                random.choice(nextLayerEdges),
            ]
            if randomEdge in edgesList:
                continue
            edgesList.append(randomEdge)

    edgesList.extend([i, graphLayers[N - 1][0]] for i in graphLayers[N - 2])
    return edgesList
