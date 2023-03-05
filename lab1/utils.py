import igraph as ig
import matplotlib.pyplot as plt


def generateEdgesList(neighbourList):
  edges = []
  for index, neighbours in enumerate(neighbourList):
    edges.extend((index, neighbour - 1)
                 for neighbour in neighbours if neighbour - 1 < index)
  return edges


def drawGraph(neighbourList):
  g = ig.Graph(len(neighbourList), generateEdgesList(neighbourList))
  g.vs['id'] = [i + 1 for i in range(len(neighbourList))]

  fig, ax = plt.subplots()
  ig.plot(
    g,
    target=ax,
    layout="circle",  # print nodes in a circular layout
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
