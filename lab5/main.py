import sys

from dataTransformations.algorithms import *
from utils import *


def main(mode):
    if mode == "task1":
        [graphVertices, graphEdges] = generateFlowNetwork(3)
    else:
        sys.exit("Please provide valide mode, [task1, task2, task3, task4, task5]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 2:
        sys.exit(
            "Please provide two arguments, first is the mode [task1, task2, task3, task4, task5]"
        )

    main(programArguments[1])
