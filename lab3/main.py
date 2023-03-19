import sys

# from dataTransformations.readData import *
from dataTransformations.algorithms import *
from utils import *
import copy


def main(mode, num):
    num = int(num)
    if mode == "task1":
        neighbourList = generateConnectedGraph(5, 6)
        edgesValues = [np.random.randint(1, num) for _ in range(len(generateEdgesList(neighbourList)))]
        drawGraph(neighbourList, edgesValues)
    elif mode == "task2":
        neighbourList = generateConnectedGraph(5, 8)
        edgesValues = [np.random.randint(1, 10) for _ in range(
            len(generateEdgesList(neighbourList)))]
        d, p = dijkstra(neighbourList, edgesValues, num - 1)
        printSolution(d, p, num - 1)
        drawGraph(neighbourList, edgesValues)
        drawGraph(neighbourList, edgesValues)

    else:
        sys.exit("Please provide valide mode, [task1, task2]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 3:
        sys.exit(
            "Please provide two arguments, first is the mode [task1, task2, task3, task4, task5], second one is input file name."
        )

    main(programArguments[1], programArguments[2])
