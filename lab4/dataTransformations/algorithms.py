import sys
import numpy as np
import copy

from utils import *
from .dijkstra import dijkstra


def generateDigraph(node_count, probability):
    if probability < 0 or probability > 1:
        sys.exit("Wrong randomization arguments")
    if node_count < 1:
        sys.exit("Wrong node count")

    edges = []

    if probability == 0 or node_count == 1:
        g = ig.Graph(node_count, directed=True)
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
        sys.exit()

    while True:
        for i in range(0, node_count):
            for j in range(0, node_count):
                if i != j:
                    rand = np.random.rand()

                    if rand < probability:
                        edges.append([i, j])

        maxList = map(max, edges)
        maxNode = max(maxList, default=-1)

        if maxNode == node_count - 1:
            break

        edges = []

    return edges


def kosaraju(edges_list):
    neighbour_list = convertEdgesToNeighbourList(edges_list)
    node_number = len(neighbour_list)

    d = []
    f = []

    for _ in range(node_number):
        d.append(-1)
        f.append(-1)

    t = 0

    for i in range(node_number):
        if d[i] == -1:
            t = DFS_visit(i, neighbour_list, d, f, t)

    reverse_edges_list = list(reverse_edges(edges_list))
    reverse_neighbour_list = convertEdgesToNeighbourList(reverse_edges_list)

    sorted_times = copy.deepcopy(f)

    sorted_nodes = []

    for i in range(node_number):
        sorted_nodes.append([i, sorted_times[i]])

    sorted_nodes = sorted(sorted_nodes, key=lambda x: x[1], reverse=True)
    sorted_nodes = [x[0] for x in sorted_nodes]

    nr = 0
    comp = []

    for _ in range(node_number):
        comp.append(-1)

    for node_index in sorted_nodes:
        if comp[node_index] == -1:
            nr = nr + 1
            comp[node_index] = nr
            components_r(nr, node_index, reverse_neighbour_list, comp)

    return comp


def swap(array):
    return [array[1], array[0]]


def reverse_edges(edgesList):
    return map(swap, edgesList)


def DFS_visit(v, neighbour_list, d, f, t):
    t = t + 1
    d[v] = t

    for u in neighbour_list[v]:
        if d[u] == -1:
            t = DFS_visit(u, neighbour_list, d, f, t)

    t = t + 1
    f[v] = t

    return t


def components_r(nr, v, reverse_neighbour_list, comp):
    for u in reverse_neighbour_list[v]:
        if comp[u] == -1:
            comp[u] = nr
            components_r(nr, u, reverse_neighbour_list, comp)


def bellman_ford(edges_list, edgesValues, s):
    edgesLen = len(edges_list)
    distance = [np.inf for _ in range(edgesLen)]
    distance[s] = 0

    for _ in range(edgesLen - 1):
        for i in range(len(edges_list)):
            if distance[edges_list[i][1]] > distance[edges_list[i][0]] + edgesValues[i]:
                distance[edges_list[i][1]] = distance[edges_list[i][0]] + edgesValues[i]

    for i in range(len(edges_list)):
        if distance[edges_list[i][1]] > distance[edges_list[i][0]] + edgesValues[i]:
            print("Graph contains negative cycle")
            return False

    return distance


def johnson(edges_list, edgesValues, nodesCount, verbose=False):
    edgesLen = len(edges_list)

    G_prim_edges, G_prim_edgesValues = add_s(edges_list, edgesValues, nodesCount)
    if verbose:
        drawGraphWithValues(G_prim_edges, G_prim_edgesValues)

    if (d := bellman_ford(G_prim_edges, G_prim_edgesValues, nodesCount)) == False:
        return False

    h = copy.deepcopy(d)
    w_prim = [
        edgesValues[i] + h[edges_list[i][0]] - h[edges_list[i][1]]
        for i in range(edgesLen)
    ]

    D = np.zeros((nodesCount, nodesCount), dtype="int")

    neighbour_list = convertEdgesToNeighbourList(edges_list)
    d_prim = [dijkstra(neighbour_list, w_prim, i)[0] for i in range(nodesCount)]

    D = [
        [d_prim[i][j] + h[j] - h[i] for j in range(nodesCount)]
        for i in range(nodesCount)
    ]

    return D


def add_s(edges_list, edgesValues, nodesCount):
    edgesLen = len(edges_list)
    G_prim = copy.deepcopy(edges_list)
    G_prim_edgesValues = copy.deepcopy(edgesValues)
    G_prim.extend([nodesCount, index] for index in range(nodesCount))
    G_prim_edgesValues.extend([0 for _ in range(nodesCount)])
    return G_prim, G_prim_edgesValues
