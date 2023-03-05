def generateEdgesList(neighbourList):
  edges = []
  for index, neighbours in enumerate(neighbourList):
    edges.extend((index, neighbour - 1)
                 for neighbour in neighbours if neighbour - 1 < index)
  return edges


