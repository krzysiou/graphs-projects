from utils import *


def nm2in(neighbourMatrix):
    edges = int(sum(sum(neighbourMatrix, [])) / 2)
    incidentMatrix = matrixOfZeros(len(neighbourMatrix), edges)
    e = 0

    for i in range(len(neighbourMatrix)):
        for j in range(len(neighbourMatrix)):
            if i < j and neighbourMatrix[i][j] == 1:
                incidentMatrix[i][e] = 1
                incidentMatrix[j][e] = 1
                e = e + 1

    return incidentMatrix


def in2nl(incidentMatrix):
    neighbourList = []
    edges = int(sum(sum(incidentMatrix, [])) / 2)

    for _ in range(len(incidentMatrix)):
        neighbourList.append([])

    for e in range(edges):
        edge = []
        for i in range(len(incidentMatrix)):
            if incidentMatrix[i][e] == 1:
                edge.append(i)
        neighbourList[edge[0]].append(edge[1] + 1)
        neighbourList[edge[1]].append(edge[0] + 1)

    return neighbourList


def nl2nm(neighbourList):
    neighbourMatrix = matrixOfZeros(len(neighbourList), len(neighbourList))

    for i in range(len(neighbourList)):
        for j in range(len(neighbourList[i])):
            if int(neighbourList[i][j]) > i + 1:
                neighbourMatrix[i][int(neighbourList[i][j]) - 1] = 1
                neighbourMatrix[int(neighbourList[i][j]) - 1][i] = 1
    return neighbourMatrix


def convertNeighbourMatrix(neighbourMatrix):
    incidentMatrix = nm2in(neighbourMatrix)
    neighbourList = in2nl(incidentMatrix)

    return incidentMatrix, neighbourList


def convertIncidentMatrix(incidentMatrix):
    neighbourList = in2nl(incidentMatrix)
    neighbourMatrix = nl2nm(neighbourList)

    return neighbourList, neighbourMatrix


def convertNeighbourList(neighbourList):
    neighbourMatrix = nl2nm(neighbourList)
    incidentMatrix = nm2in(neighbourMatrix)

    return neighbourMatrix, incidentMatrix
