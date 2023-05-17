import sys

from dataTransformations.algorithms import *
from utils import *


def main(mode, num):
    if mode == "task1":
        print(num)
        maxWeight = int(num)
        neighbourList = generateConnectedGraph(5, 6)
        edgesValues = [
            np.random.randint(1, maxWeight)
            for _ in range(len(generateEdgesList(neighbourList)))
        ]
        drawGraph(neighbourList, edgesValues)

    elif mode == "task2":
        startNode = int(num)
        neighbourList = generateConnectedGraph(5, 8)
        edgesValues = [
            np.random.randint(1, 10)
            for _ in range(len(generateEdgesList(neighbourList)))
        ]
        d, p = dijkstra(neighbourList, edgesValues, startNode - 1)
        printSolution(d, p, startNode - 1)
        drawGraph(neighbourList, edgesValues)

    elif mode == "task3":
        neighbourList = generateConnectedGraph(5, 6)
        edgesValues = [
            np.random.randint(1, 10)
            for _ in range(len(generateEdgesList(neighbourList)))
        ]
        printMatrix(lengthMatrix(neighbourList, edgesValues))
        drawGraph(neighbourList, edgesValues)

    elif mode == "task4":
        neighbourList = generateConnectedGraph(5, 6)
        edgesValues = [
            np.random.randint(1, 10)
            for _ in range(len(generateEdgesList(neighbourList)))
        ]
        centLen, centIdx = graphCenter(neighbourList, edgesValues)
        miniMaxCentLen, miniMaxCentIdx = miniMaxGraphCenter(neighbourList, edgesValues)

        printMatrix(lengthMatrix(neighbourList, edgesValues))
        print(f"Centrum = {centIdx + 1} (suma odległości: {centLen})")
        print(
            f"Centrum minimax = {miniMaxCentIdx + 1} (odległość od najdalszego: {miniMaxCentLen})"
        )

    elif mode == "task5":
        neighbourList = generateConnectedGraph(6, 12)
        edgesValues = [
            np.random.randint(1, 10)
            for _ in range(len(generateEdgesList(neighbourList)))
        ]
        T = minimalSpanningTree(neighbourList, edgesValues)
        drawSpanningTree(T)

    else:
        sys.exit("Please provide valide mode, [task1, task2, task3, task4, task5]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) < 2 or (
        (programArguments[1] == "task1" or programArguments[1] == "task2")
        and len(programArguments) != 3
    ):
        sys.exit(
            """Please provide two arguments, first is the mode [task1, task2, task3, task4, task5]
              for [task1] second argument is max value of edge weight,
              for [task2] second argument is index of starting vertex
            """
        )
    main(
        programArguments[1], programArguments[2] if len(programArguments) == 3 else None
    )
