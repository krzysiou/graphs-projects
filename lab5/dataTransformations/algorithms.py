import sys
import numpy as np
import copy
import random
from collections import deque


def generateFlowNetwork(N):
    if N < 2:
        sys.exit("N must be greater than 2")

    graphLayers = generateVerticesLayers(N)
    graphEdges = generateGraphEdges(graphLayers)
    if N != 2:
        graphEdges = addRandomEdges(graphEdges, graphLayers)
    edgeValues = generateEdgeValues(graphEdges)

    return [graphLayers, graphEdges, edgeValues]


def generateVerticesLayers(N):
    graphLayers = {}
    graphLayers[0] = [0]  # s

    count = 1
    for i in range(1, N + 1):
        numberOfVerticesInLayer = random.randint(2, N)
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

        currentLayercount = 0
        nextLayerCount = 0
        for _ in range(max(len(currentLayerEdges), len(nextLayerEdges))):
            randomEdge = [
                currentLayerEdges[currentLayercount % len(currentLayerEdges)],
                nextLayerEdges[nextLayerCount % len(nextLayerEdges)],
            ]
            if randomEdge in edgesList:
                continue
            nextLayerCount += 1
            currentLayercount += 1
            edgesList.append(randomEdge)

    edgesList.extend([i, graphLayers[N - 1][0]] for i in graphLayers[N - 2])
    return edgesList


def addRandomEdges(graphEdges, graphLayers):
    N = len(graphLayers)
    edgesList = copy.deepcopy(graphEdges)

    newEdgesCount = 0
    while True:
        for i in range(1, N - 2):
            currentLayerVertices = graphLayers[i] + graphLayers[i + 1]

            randomEdge = [
                random.choice(currentLayerVertices),
                random.choice(currentLayerVertices),
            ]
            if (
                randomEdge in edgesList
                or randomEdge[::-1] in edgesList
                or randomEdge[0] == randomEdge[1]
            ):
                continue

            edgesList.append(randomEdge)
            newEdgesCount += 1
            if newEdgesCount == 2 * N:
                return edgesList


def generateEdgeValues(edgesList):
    edgeValues = []
    for _ in range(len(edgesList)):
        edgeValues.append(random.randint(1, 10))
    return edgeValues


def convertToNeighbourMatrix(graphEdges, edgeValues, N):
    neighbourMatrix = np.array([[0 for _ in range(N + 1)]
                               for _ in range(N + 1)])
    for i in range(len(graphEdges)):
        neighbourMatrix[graphEdges[i][0]][graphEdges[i][1]] = edgeValues[i]
    return neighbourMatrix


def bfs(G, residualCapacity, parent, s, t):
    visited = [False] * len(G)
    queue = deque([s])
    visited[s] = True
    while queue:
        currentNode = queue.popleft()
        for neighbour in range(len(G)):
            if not visited[neighbour] and residualCapacity[currentNode][neighbour] > 0:
                queue.append(neighbour)
                visited[neighbour] = True
                parent[neighbour] = currentNode
                if neighbour == t:
                    return True, parent
    return False, parent


def fordFulkerson(G, s, t):
    numOfVertices = len(G)
    residualCapacity = [[0] * numOfVertices for _ in range(numOfVertices)]
    for u in range(numOfVertices):
        for v in range(numOfVertices):
            residualCapacity[u][v] = G[u][v]
    maxFlow = 0
    flowPath = []
    while True:
        parent = [-1] * numOfVertices
        foundPath, parent = bfs(G, residualCapacity, parent, s, t)
        if not foundPath:
            break
        minCapacity = float('inf')
        node = t
        while node != s:
            minCapacity = min(
                minCapacity, residualCapacity[parent[node]][node])
            node = parent[node]
        node = t
        while node != s:
            flowPath.append(([parent[node], node], minCapacity))
            residualCapacity[parent[node]][node] -= minCapacity
            residualCapacity[node][parent[node]] += minCapacity
            node = parent[node]
        maxFlow += minCapacity
    return maxFlow, flowPath


def calculateMaxFlowPath(G, flowPath, capacities):
    flows = []
    for graphEdge in G:
        graphEdgeSum = sum([t[1] for t in flowPath if t[0] == graphEdge])
        flows.append(graphEdgeSum)
    return [str(flow) + "/" + str(capacity) for flow, capacity in zip(flows, capacities)]
