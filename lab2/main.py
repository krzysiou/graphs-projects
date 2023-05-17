import sys

from dataTransformations.readData import *
from dataTransformations.algorithms import *
from utils import *


def main(mode, second_argument):
    if mode == "task1":
        seqArray = readLine(second_argument)
        print(f"Graph sequence: {degree_seq(seqArray)}")
        drawGraph(constructNLFromSeq(seqArray))

    elif mode == "task2":
        seqArray = readLine(second_argument)
        numberOfRands = int(input("Write number of randomizations: "))
        neighbourList = constructNLFromSeq(seqArray)
        randEdges = randomizeEdges(neighbourList, numberOfRands, verbose=True)
        drawGraph(randEdges, "EL")

    elif mode == "task3":
        seqArray = readLine(second_argument)
        neighbourList = constructNLFromSeq(seqArray)

        print(neighbourList)

        comp = calculateIntegrityArray(seqArray, neighbourList)
        connectedComponents(comp)
        drawGraph(neighbourList)

    elif mode == "task4":
        numOfEdges = int(input("Write number of edges: "))
        eulerNeighbourList = generateEulerGraph(int(second_argument), numOfEdges)
        eulerCycle = findEulerCycle(copy.deepcopy(eulerNeighbourList))

        print(eulerCycle)

        drawGraphV2(eulerNeighbourList)

    elif mode == "task5":
        k = int(input("Write number of edges from each vertex: "))
        regularNeighbourList = generateRegularGraph(int(second_argument), k)

        drawGraphV2(regularNeighbourList)

    elif mode == "task6":
        neighbourList = readList(second_argument)

        hamiltonianCycle = checkHamiltonian(neighbourList)
        if hamiltonianCycle:
            print(f"Graph is Hamiltonian.\nCycle: {hamiltonianCycle}")
        else:
            print("Graph is not Hamiltonian.")

    else:
        sys.exit(
            "Please provide valid mode, [task1, task2, task3, task4, task5, task6]"
        )


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 3:
        sys.exit(
            "Please provide two arguments, for modes [task1, task2, task3, task6] second one is input file name, for [task4, task5] second one is number of vertexes."
        )

    main(programArguments[1], programArguments[2])
