import sys
import numpy as np
import copy
import random
from collections import deque


def generateFlowNetwork(N):
    if N <= 2:
        sys.exit("N must be greater than 2")

    graphLayers = generateVerticesLayers(N)
    graphEdges = generateGraphEdges(graphLayers)
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
    neighbourMatrix = np.array([[0 for _ in range(N+1)] for _ in range(N+1)])
    for i in range(len(graphEdges)):
        neighbourMatrix[graphEdges[i][0]][graphEdges[i][1]] = edgeValues[i]
    return neighbourMatrix


def bfs(graph, residual_capacity, parent, source, target):
    visited = [False] * len(graph)
    queue = deque([source])
    visited[source] = True

    while queue:
        current_node = queue.popleft()

        for neighbor in range(len(graph)):
            if not visited[neighbor] and residual_capacity[current_node][neighbor] > 0:
                queue.append(neighbor)
                visited[neighbor] = True
                parent[neighbor] = current_node

                if neighbor == target:
                    return True, parent

    return False, parent


def ford_fulkerson(G, s, t):
    num_vertices = len(G)

    residual_capacity = [[0] * num_vertices for _ in range(num_vertices)]
    for u in range(num_vertices):
        for v in range(num_vertices):
            residual_capacity[u][v] = G[u][v]

    max_flow = 0

    while True:
        parent = [-1] * num_vertices

        found_path, parent = bfs(G, residual_capacity, parent, s, t)

        if not found_path:
            break

        min_capacity = float('inf')
        node = t
        while node != s:
            min_capacity = min(min_capacity, residual_capacity[parent[node]][node])
            node = parent[node]

        node = t
        while node != s:
            residual_capacity[parent[node]][node] -= min_capacity
            residual_capacity[node][parent[node]] += min_capacity
            node = parent[node]

        max_flow += min_capacity

    return max_flow