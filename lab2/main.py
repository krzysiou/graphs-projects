import sys

from dataTransformations.readData import *
from dataTransformations.algorithms import *
from utils import *


def main(mode, file_name):
    if mode == "task1":
        seqArray = readLine(file_name)
        print(f"Graph sequence: {degree_seq(seqArray)}")
        drawGraph(constructNLFromSeq(seqArray))

    elif mode == "task2":
        seqArray = readLine(file_name)
        numberOfRands = int(input("Write number of randomizations: "))
        neighbourList = constructNLFromSeq(seqArray)
        randEdges = randomizeEdges(neighbourList, numberOfRands, verbose=True)
        drawGraph(randEdges, "EL")

    elif mode == "task3":
        seqArray = readLine(file_name)
        neighbourList = constructNLFromSeq(seqArray)

        print(neighbourList)

        comp = calculateIntegrityArray(seqArray, neighbourList)
        print(f"Max integrity number: {max(comp)}")
        drawGraph(neighbourList)

    elif mode == "task4":
        eulerNeighbourList = generateEulerGraph(5, 6)
        eulerCycle = findEulerCycle(copy.deepcopy(eulerNeighbourList))

        print(eulerCycle)

        drawGraphV2(eulerNeighbourList)

    elif mode == "task5":
        regularNeighbourList = generateRegularGraph(7, 2)

        drawGraphV2(regularNeighbourList)

    elif mode == "task6":
        neighbourList = readList(file_name)

        hamiltonianCycle = checkHamiltonian(neighbourList)
        if hamiltonianCycle:
            print(f"Graph is Hamiltonian.\nCycle: {hamiltonianCycle}")
        else:
            print("Graph is not Hamiltonian.")

    else:
        sys.exit(
            "Please provide valide mode, [task1, task2, task3, task4, task5, task6]"
        )


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 3:
        sys.exit(
            "Please provide two arguments, first is the mode [[task1, task2, task3, task4, task5, task6], second one is input file name."
        )

    main(programArguments[1], programArguments[2])
