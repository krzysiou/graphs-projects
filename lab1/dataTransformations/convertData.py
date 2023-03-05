import numpy as np


def convertNeighbourMatrix(neighbourMatrix):
    # code here
    print(1)

def convertIncidentMatrix(incidentMatrix):
    #code here
    print(1)
def convertNeighbourList(neighbourList):
  numberOfVertices = len(neighbourList)
  neighbourMatrix = np.zeros((numberOfVertices, numberOfVertices))
  for vertexIndex, vertexNeighbours in enumerate(neighbourList):
    for neighbour in vertexNeighbours:
      neighbourMatrix[vertexIndex][neighbour - 1] = 1

  print(neighbourMatrix)
  return [neighbourMatrix, [0]]
