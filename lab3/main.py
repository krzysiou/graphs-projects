import sys

# from dataTransformations.readData import *
# from dataTransformations.algorithms import *
from utils import *


# def main(mode, file_name):
def main(mode):
    if mode == "task1":
        numOfEdges = 21
        neighbourList = generateConnectedGraph(20, numOfEdges)
        drawGraph(neighbourList, numOfEdges)
    else:
        sys.exit("Please provide valide mode, [task1, task2]")


if __name__ == "__main__":
    programArguments = sys.argv

    # if len(programArguments) != 3:
    #     sys.exit(
    #         "Please provide two arguments, first is the mode [task1, task2, task3, task4, task5], second one is input file name."
    #     )

    if len(programArguments) != 2:
        sys.exit(
            "Please provide minimum one argument, first is the mode [task1, task2, task3, task4, task5], second one is input file name."
        )

    # main(programArguments[1], programArguments[2])
    main(programArguments[1])
