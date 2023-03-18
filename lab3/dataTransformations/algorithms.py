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

def printSolution(d):
    print("Vertex \t Distance from Source")
    for node in range(len(d)):
        print(node + 1, "\t\t", d[node])

def dijkstra(neighbourList, edgesValues, s):
    neighbourMatrix = convertToNeighbourMatrix(neighbourList)
    edges = generateEdgesList(neighbourList)
    neighbourMatrixWithValues = updateMatrixWithValues(neighbourMatrix, edges, edgesValues)
    d, p = initializeAtributes(len(neighbourList), s)
    S = [False for _ in range(len(neighbourList))]

    for _ in range(len(neighbourList)):
        u = minDistance(d, S)
        S[u] = True
        for v in range(len(d)):
            if (neighbourMatrixWithValues[u][v] > 0 and S[v] == False
                    and d[v] > d[u] + neighbourMatrixWithValues[u][v]):
                d[v] = d[u] + neighbourMatrixWithValues[u][v]
    printSolution(d)    

def convertToNeighbourMatrix(neighbourList):
    neighbourMatrix = matrixOfZeros(len(neighbourList), len(neighbourList))

    for i in range(len(neighbourList)):
        for j in range(len(neighbourList[i])):
            if int(neighbourList[i][j]) > i:
                neighbourMatrix[i][int(neighbourList[i][j])] = 1
                neighbourMatrix[int(neighbourList[i][j])][i] = 1

    return neighbourMatrix