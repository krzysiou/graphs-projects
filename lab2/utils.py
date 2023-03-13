import igraph as ig
import matplotlib.pyplot as plt
import numpy as np


def generateEdgesList(neighbourList):
  edges = []
  for index, neighbours in enumerate(neighbourList):
    edges.extend((index, neighbour) for neighbour in neighbours)

  return edges


def matrixOfZeros(sizeX, sizeY):
  matrix = []

  for _ in range(sizeX):
    temp = []
    for _ in range(sizeY):
      temp.append(0)
    matrix.append(temp)

  return matrix


def drawGraph(list, inputType="NL"):
  if inputType == "NL":
    g = ig.Graph(len(list), generateEdgesList(list))
    g.vs['id'] = [i + 1 for i in range(len(list))]
  elif inputType == "EL":
    g = ig.Graph(len(list), list)
    g.vs['id'] = [i + 1 for i in range(len(list))]
  _, ax = plt.subplots()
  ig.plot(
    g,
    target=ax,
    layout="circle",
    vertex_size=0.25,
    vertex_color="#d9d9ff",
    vertex_frame_width=1.0,
    vertex_frame_color="#1414ff",
    vertex_label_size=16.0,
    vertex_label=g.vs['id'],
    edge_width=2,
    edge_color="#000"
      )

  plt.show()


def sortList(A, mode="asc"):
  mode = 1 if mode == "asc" else -1 if mode == "desc" else 0
  A[:] = list(mode * np.sort(mode * np.array(A)))


def sortDict(A, mode="asc"):
  reverse = True if mode == "desc" else False
  B = {k: v for k, v in sorted(
    A.items(), reverse=reverse, key=lambda item: item[1])}
  A.clear()
  A.update(B)


def isEdgeExists(edge, listOfEdges):
  reversed = edge[::-1]
  return tuple(edge) in listOfEdges or tuple(reversed) in listOfEdges
