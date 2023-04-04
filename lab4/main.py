import sys

from utils import *
from dataTransformations.algorithms import *


def main(mode, input_file):
    if mode == "task1":
        edgesList = generateDigraph(5, 0.3)
        drawGraph(edgesList)

    elif mode == "task2":
        edges_list = generateDigraph(5, 0.4)
        result = kosaraju(edges_list)

        print(result)
        drawGraph(edges_list)

    elif mode == "task3":
        nodesCount = 5
        while True:
            edges_list = generateDigraph(nodesCount, 0.2)
            result = kosaraju(edges_list)
            if len(set(result)) == 1:
                break

        edgesValues = [np.random.randint(-5, 10) for _ in range(len(edges_list))]

        drawGraphWithValues(edges_list, edgesValues)

    else:
        sys.exit("Please provide valide mode, [task1, task2, task3, task4, task5]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 3:
        sys.exit(
            "Please provide two arguments, first is the mode [task1, task2, task3, task4, task5], second one is input file name."
        )

    main(programArguments[1], programArguments[2])
