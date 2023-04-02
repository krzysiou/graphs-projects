import sys
import numpy as np
import copy

from utils import *


def generateDigraph(node_count, probability):
    if probability < 0 or probability > 1:
        sys.exit("Wrong randomization arguments")

    edges = []

    while True:
        for i in range(0, node_count):
            for j in range(0, node_count):
                if i != j:
                    rand = np.random.rand()

                    if rand < probability:
                        edges.append([i, j])

        maxList = map(max, edges)
        maxNode = max(maxList)

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
