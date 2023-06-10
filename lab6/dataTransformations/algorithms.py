import sys
import numpy as np
import random

from utils import *

def generateDigraph(node_count, probability):
    if probability < 0 or probability > 1:
        sys.exit("Nieprawidłowa wartość dla prawdopodobieństwa. Podaj wartość z przedziału [0,1]")

    edges = []

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


def pageRank1(neighbourList, probability):

    if probability < 0 or probability > 1:
        raise ValueError("Nieprawidłowa wartość dla prawdopodobieństwa. Podaj wartość z przedziału [0,1]")

    nodes = len(neighbourList)
    frequencyTab = [0 for _ in range(nodes)]
    currentNodeIndex = 0
    nodeslist = [i for i in range(nodes)]

    for i in range(nodes):
        if len(neighbourList[i]) == 0:
            raise ValueError("Graf z wierzchołkiem bez krawedzi wyjsciowych. Wygeneruj ponownie")

    N = 1000000

    for _ in range(N):
        if random.random() > probability:
            currentNodeIndex = random.choice(list(neighbourList[currentNodeIndex]))
        else:
            currentNodeIndex = random.choice(list(nodeslist))

        frequencyTab[currentNodeIndex]+=1

    print("Algorytm PageRank wersja 1")
    for i, pageRank in enumerate(frequencyTab):
        print(i + 1, "==> PageRank = ", pageRank / N)


def pageRank2(neighbourList, probability):

    if probability < 0 or probability > 1:
        raise ValueError("Nieprawidłowa wartość dla prawdopodobieństwa. Podaj wartość z przedziału [0,1]")
    
    nodes = len(neighbourList)

    
    for i in range(nodes):
        if len(neighbourList[i]) == 0:
            raise ValueError("Graf z wierzchołkiem bez krawedzi wyjsciowych. Wygeneruj ponownie")
    
    P = np.zeros((nodes, nodes))
    A = digraphNLToNM(neighbourList)
    pVector = np.full(nodes, 1 / nodes)

    for i in range(nodes):
        nodeDegree = len(neighbourList[i])
        for j in range(nodes):
            P[i][j] = (1.0 - probability) * A[i][j] / nodeDegree + float(probability / nodes)

    iter = 0
    prevPVecLen = 0.
    currPVecLen = 1.
    while np.abs(currPVecLen - prevPVecLen) > 0.00000001:
        prevPVecLen = vectorLength(pVector)
        pVector = np.dot(pVector, P)
        currPVecLen = vectorLength(pVector)
        iter += 1

    print("Algorytm PageRank wersja 2")
    print(f"Zbieżność uzyskano po {iter} iteracjach.")
    for i in range(nodes):
        print(i + 1, "==> PageRank = ", pVector[i])