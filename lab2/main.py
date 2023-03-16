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
        maxIntegrityNumber = calculateMaxIntegrityNumber(seqArray, neighbourList)
        print(f"Max integrity number: {maxIntegrityNumber}")
        drawGraph(constructNLFromSeq(seqArray))

    else:
        sys.exit("Please provide valide mode, [task1, task2]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 3:
        sys.exit(
            "Please provide two arguments, first is the mode [task1, task2], second one is input file name."
        )

    main(programArguments[1], programArguments[2])
