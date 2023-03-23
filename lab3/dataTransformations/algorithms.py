import copy
import numpy as np
import sys
from utils import *


def initializeAtributes(graphLength, s):
    ds = []
    ps = []
    for _ in range(graphLength):
        ds.append(sys.maxsize)
        ps.append(0)
    ds[s] = 0
    return ds, ps


def relax(u, v, w):
    print()


def updateMatrixWithValues(neighbourMatrix, edges, edgesValues):
    neighbourMatrixWithValues = copy.deepcopy(neighbourMatrix)
    for i, edge in enumerate(edges):
        neighbourMatrixWithValues[edge[0]][edge[1]] = edgesValues[i]
        neighbourMatrixWithValues[edge[1]][edge[0]] = edgesValues[i]

    return neighbourMatrixWithValues


def minDistance(d, S):
    minDist = sys.maxsize
    for i, dist in enumerate(d):
        if dist < minDist and S[i] == False:
            minDist = dist
            minIndex = i
    return minIndex


def getPath(start, end, p):
    if start == end:
        return [start + 1]
    path = [end + 1]
    step = p[end]
    while step != start:
        path.append(step + 1)
        step = p[step]
    path.append(start + 1)
    path.reverse()
    return path


def printSolution(d, p, start):
    print(p)
    print(f"START: s = {start+1}")
    for node in range(len(d)):
        print(f"d({node+1}) = {d[node]} ==> [", end="")
        print(" - ".join(map(str, getPath(start, node, p))), end="")
        print("]")


def dijkstra(neighbourList, edgesValues, s):
    neighbourMatrix = convertToNeighbourMatrix(neighbourList)
    edges = generateEdgesList(neighbourList)
    neighbourMatrixWithValues = updateMatrixWithValues(
        neighbourMatrix, edges, edgesValues
    )
    d, p = initializeAtributes(len(neighbourList), s)
    S = [False for _ in range(len(neighbourList))]

    for _ in range(len(neighbourList)):
        u = minDistance(d, S)
        S[u] = True
        for v in range(len(d)):
            if (
                neighbourMatrixWithValues[u][v] > 0
                and S[v] == False
                and d[v] > d[u] + neighbourMatrixWithValues[u][v]
            ):
                d[v] = d[u] + neighbourMatrixWithValues[u][v]
                p[v] = u

    return [d, p]


def convertToNeighbourMatrix(neighbourList):
    neighbourMatrix = matrixOfZeros(len(neighbourList), len(neighbourList))

    for i in range(len(neighbourList)):
        for j in range(len(neighbourList[i])):
            if int(neighbourList[i][j]) > i:
                neighbourMatrix[i][int(neighbourList[i][j])] = 1
                neighbourMatrix[int(neighbourList[i][j])][i] = 1

    return neighbourMatrix


def lengthMatrix(neighbourList, edgesValues):
    matrix = matrixOfZeros(len(neighbourList), len(neighbourList))
    for startNode in range(len(neighbourList)):
        d, _ = dijkstra(neighbourList, edgesValues, startNode)
        matrix[startNode] = d
    return matrix
