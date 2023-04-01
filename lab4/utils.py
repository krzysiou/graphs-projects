import igraph as ig
import matplotlib.pyplot as plt


def drawGraph(edgesList):
    maxList = map(max, edgesList)
    node_count = max(maxList) + 1

    g = ig.Graph(node_count, edgesList, directed=True)
    g.vs["id"] = [i + 1 for i in range(node_count)]

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
        vertex_label=g.vs["id"],
        edge_width=2,
        edge_color="#000",
    )

    plt.show()


def convertEdgesToNeighbourList(edges):
    maxList = map(max, edges)
    node_count = max(maxList)
    neighbourList = []

    for _ in range(node_count + 1):
        neighbourList.append([])

    for edge in edges:
        neighbourList[edge[0]].append(edge[1])

    return neighbourList
