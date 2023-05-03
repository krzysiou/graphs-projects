import numpy as np
from utils import sortList, sortDict, generateEdgesList, isEdgeExists, drawGraphV2
import sys
import copy


def degree_seq(A, verbose=False):
    n = len(A)
    sortList(A, mode="desc")
    A = np.array(A)
    if verbose:
        print(A)
    while True:
        if np.all(A == 0):
            return True
        if A[0] > n or np.any(A < 0):
            return False

        A[1 : A[0] + 1] = A[1 : A[0] + 1] - 1
        A[0] = 0
        sortList(A, mode="desc")
        if verbose:
            print(A)


def constructNLFromSeq(A, verbose=False):
    if not degree_seq(A):
        raise Exception("Wrong sequence")
    n = len(A)
    A = np.array(A)
    A = {index + 1: val for index, val in enumerate(A)}
    sortDict(A, mode="desc")
    if verbose:
        print(A)
    neighbourList = [[] for _ in range(n)]

    while True:
        if np.all(np.array(list(A.values())) == 0):
            return neighbourList

        for i in range(1, list(A.values())[0] + 1):
            A[list(A.keys())[i]] = A[list(A.keys())[i]] - 1
            neighbourList[list(A.keys())[0] - 1].append(list(A.keys())[i] - 1)

        A[list(A.keys())[0]] = 0
        sortDict(A, mode="desc")
        if verbose:
            print(A)


def randomizeEdges(NL, number, verbose=False):
    edges = generateEdgesList(NL)
    numberOfEdges = len(edges)
    if numberOfEdges == 0:
        return edges
    i = 0
    while i < number:
        randAB = np.random.randint(0, numberOfEdges)
        randCD = randAB
        while randCD == randAB:
            randCD = np.random.randint(0, numberOfEdges)

        if verbose:
            print(f"{edges[randAB]}, {edges[randCD]} => ", end="")

        AB = list(edges[randAB])
        CD = list(edges[randCD])
        AB[0], AB[1], CD[0], CD[1] = AB[0], CD[1], AB[1], CD[0]

        if (
            not isEdgeExists(AB, edges)
            and not isEdgeExists(CD, edges)
            and AB[0] != AB[1]
            and CD[0] != CD[1]
            and AB != CD
        ):  # check if it is not multiedge or loop
            edges[randAB], edges[randCD] = tuple(AB), tuple(CD)
            if verbose:
                print(f"{edges[randAB]}, {edges[randCD]}")
        else:
            print("Skip..")
            i -= 1
        i += 1

    return edges


def calculateIntegrityArray(sequence, neighbourList):
    numberOfNodes = len(sequence)
    comp = []
    integrityNumber = 0

    for i in range(numberOfNodes):
        comp.append(-1)

    for i in range(numberOfNodes):
        if comp[i] == -1:
            integrityNumber += 1
            comp[i] = integrityNumber
            components(integrityNumber, i, neighbourList, comp)

    return comp


def components(integrityNumber, index, neighbourList, comp):
    neighbours = neighbourList[index]

    for i in neighbours:
        if comp[i] == -1:
            comp[i] = integrityNumber
            componentsV2(integrityNumber, i, neighbourList, comp)


def calculateIntegrityArrayV2(sequence, neighbourList):
    while [] in neighbourList:
        emptyArrayIndex = neighbourList.index([])

        neighbourList.pop(emptyArrayIndex)

        for i in range(len(neighbourList)):
            for j in range(len(neighbourList[i])):
                if neighbourList[i][j] > emptyArrayIndex + 1:
                    neighbourList[i][j] = neighbourList[i][j] - 1

        sequence = [len(neighbourList[i]) for i in range(len(neighbourList))]

    numberOfNodes = len(sequence)
    comp = []
    integrityNumber = 0

    for i in range(numberOfNodes):
        comp.append(-1)

    for i in range(numberOfNodes):
        if comp[i] == -1:
            integrityNumber += 1
            comp[i] = integrityNumber
            componentsV2(integrityNumber, i, neighbourList, comp)

    return comp


def componentsV2(integrityNumber, index, neighbourList, comp):
    neighbours = neighbourList[index]

    for i in neighbours:
        if comp[i - 1] == -1:
            comp[i - 1] = integrityNumber
            componentsV2(integrityNumber, i - 1, neighbourList, comp)


def convertEdgesToNeighbourList(edges):
    maxList = map(max, edges)

    nodeNumber = max(maxList)
    neighbourList = []

    for _ in range(nodeNumber):
        neighbourList.append([])

    for edge in edges:
        neighbourList[edge[0] - 1].append(edge[1])
        neighbourList[edge[1] - 1].append(edge[0])

    return neighbourList


def generateGraphNL(n, l):
    if l < 0 or l > n * (n - 1) / 2:
        sys.exit("Wrong randomization arguments")

    edges = []

    for i in range(l):
        while True:
            rand1 = np.random.randint(1, n + 1)
            rand2 = rand1

            while rand1 == rand2:
                rand2 = np.random.randint(1, n + 1)

            edge = [rand1, rand2]
            edge.sort()

            if edge not in edges:
                edges.append(edge)
                break

    return convertEdgesToNeighbourList(edges)


def generateEulerGraph(n, l):
    while True:
        neighbourList = generateGraphNL(n, l)
        sequence = [len(neighbourList[i]) for i in range(len(neighbourList))]

        if max(calculateIntegrityArrayV2(sequence, neighbourList)) == 1 and all(
            sequence[i] % 2 == 0 for i in range(len(sequence))
        ):
            return neighbourList


def isNeighbourListEmpty(neighbourList):
    for i in range(len(neighbourList)):
        if neighbourList[i] != []:
            return False

    return True


def deleteEdge(node1, node2, neighbourList):
    neighbourList[node1 - 1].remove(node2)
    neighbourList[node2 - 1].remove(node1)


def makeMove(fromIndex, toIndex, eulerNeighbourList, eulerCycle):
    isLastNeighbour = (
        eulerNeighbourList[fromIndex - 1].index(toIndex)
        == len(eulerNeighbourList[fromIndex - 1]) - 1
    )

    decoyNeighbourList = copy.deepcopy(eulerNeighbourList)
    deleteEdge(fromIndex, toIndex, decoyNeighbourList)
    decoySequence = [len(decoyNeighbourList[i]) for i in range(len(decoyNeighbourList))]

    if not isNeighbourListEmpty(decoyNeighbourList):
        isStillIntegrated = (
            max(calculateIntegrityArrayV2(decoySequence, decoyNeighbourList)) == 1
        )

        if isStillIntegrated or isLastNeighbour:
            eulerCycle.append(fromIndex)
            deleteEdge(fromIndex, toIndex, eulerNeighbourList)

            if len(eulerNeighbourList[toIndex - 1]) != 0:
                makeMove(
                    toIndex,
                    eulerNeighbourList[toIndex - 1][0],
                    eulerNeighbourList,
                    eulerCycle,
                )

        else:
            index = eulerNeighbourList[fromIndex - 1].index(toIndex)
            makeMove(
                fromIndex,
                eulerNeighbourList[index + 1][0],
                eulerNeighbourList,
                eulerCycle,
            )
    else:
        eulerCycle.append(fromIndex)
        eulerCycle.append(toIndex)


def findEulerCycle(eulerNeighbourList):
    eulerCycle = []

    makeMove(1, eulerNeighbourList[0][0], eulerNeighbourList, eulerCycle)

    return eulerCycle


def generateGraphNP(n, probability):
    if probability < 0 or probability > 1:
        sys.exit("Wrong randomization arguments")

    while True:
        edges = []

        for i in range(1, n + 1):
            for j in range(i + 1, n + 1):
                rand = np.random.rand()

                if rand < probability:
                    edges.append([i, j])

        if edges != []:
            if max(map(max, edges)) == n:
                return convertEdgesToNeighbourList(edges)


def generateRegularGraph(nodes, level):
    if level >= nodes or (level % 2 == 1 and not nodes % 2 == 0):
        sys.exit("Wrong randomization arguments")

    while True:
        neighbourList = generateGraphNP(nodes, level / nodes)
        sequence = [len(neighbourList[i]) for i in range(len(neighbourList))]

        if all(sequence[i] == level for i in range(len(sequence))):
            return neighbourList

def checkIfHamiltonian(neighbourList):
    n = len(neighbourList)
    path = []
    path.append(0)
    unvisited = set(range(1, n))
    
    while unvisited:
        neighbours = neighbourList[path[-1]]

        for neighbour in neighbours:
            if neighbour in unvisited:
                path.append(neighbour)
                unvisited.remove(neighbour)
                break

        else:
            if len(path) == 1:
                print("This graph is not Hamiltonian!\n")
                return False
            unvisited.add(path.pop())

    if path[-1] in neighbourList[path[0]]:
        print("This graph is Hamiltonian!\n")
        print(f"Hamiltonian cycle: {path}\n")
        return True
    else:
        print("This graph is not Hamiltonian!\n")
        return False