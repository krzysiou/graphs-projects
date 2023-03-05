import numpy as np


def convertNeighbourMatrix(neighbourMatrix):
  # code here
  print(1)


def convertIncidentMatrix(incidentMatrix):
  # code here
  print(1)


def convertNeighbourList(neighbourList):
  numberOfVertices = len(neighbourList)

  neighbourMatrix = np.zeros(
      (numberOfVertices, numberOfVertices), dtype='int')
  for vertexIndex, vertexNeighbours in enumerate(neighbourList):
    for neighbour in vertexNeighbours:
      if neighbour - 1 >= numberOfVertices:
        raise ValueError("Wrong neighbour list matrix")
      neighbourMatrix[vertexIndex][neighbour - 1] = 1

  numberOfEdges = np.count_nonzero(neighbourMatrix == 1) // 2
  incidentMatrix = np.zeros((numberOfVertices, numberOfEdges), dtype='int')

  edgeCount = 0
  edgesOfVertex = {}
  for vertexIndex, vertexNeighbours in enumerate(neighbourList):
    edgesOfVertex[vertexIndex + 1] = {}
    for neighbour in vertexNeighbours:
      if neighbour - 1 > vertexIndex:
        incidentMatrix[vertexIndex][edgeCount] = 1
        edgesOfVertex[vertexIndex + 1][neighbour] = edgeCount + 1
        edgeCount += 1
      else:
        edgeIndex = edgesOfVertex[neighbour][vertexIndex + 1]
        incidentMatrix[vertexIndex][edgeIndex - 1] = 1

  return [neighbourMatrix, incidentMatrix]
