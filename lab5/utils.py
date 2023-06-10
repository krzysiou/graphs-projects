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


def drawGraphWithValues(edgesList, edgesValues):
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
        edge_label=edgesValues,
    )

    plt.show()


def drawFlowNetwork(edgesList, layers, edgeValues):
    nodeCount = (layers[len(layers) - 2][len(layers[len(layers) - 2]) - 1]) + 2

    g = ig.Graph(nodeCount, edgesList, directed=True)

    g.vs["id"] = ["s"] + [i + 1 for i in range(nodeCount - 2)] + ["t"]

    g.vs["frame width"] = [2.5] + [1.0] * (nodeCount - 2) + [2.5]

    _, ax = plt.subplots()
    ig.plot(
        g,
        target=ax,
        layout="tree",
        vertex_size=0.4,
        vertex_color="#d9d9ff",
        vertex_frame_width=g.vs["frame width"],
        vertex_frame_color="#1414ff",
        vertex_label_size=16.0,
        vertex_label=g.vs["id"],
        edge_width=2,
        edge_color="rgba(0,0,0,0.3)",
        edge_label=edgeValues,
        edge_label_size=10,
        edge_curved=0.1,
    )

    plt.show()
    pass


def convertEdgesToNeighbourList(edges):
    maxList = map(max, edges)
    node_count = max(maxList)
    neighbourList = []

    for _ in range(node_count + 1):
        neighbourList.append([])

    for edge in edges:
        neighbourList[edge[0]].append(edge[1])

    return neighbourList


def printMatrix(a):
    for _, val in enumerate(a):
        print("  ".join(map(str, val)))
