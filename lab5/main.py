import sys

from dataTransformations.algorithms import *
from utils import *


def main(mode, numberOfLayers=4):
    if mode == "task1":
        [graphLayers, graphEdges, edgeValues] = generateFlowNetwork(numberOfLayers)
        drawFlowNetwork(graphEdges, graphLayers, edgeValues)
    elif mode == "task2":
        [graphLayers, graphEdges, edgeValues] = generateFlowNetwork(numberOfLayers)
        neighbourMatrix = convertToNeighbourMatrix(graphEdges, edgeValues, graphLayers[numberOfLayers+1][0])
        maxFlow = ford_fulkerson(neighbourMatrix, graphLayers[0][0], graphLayers[numberOfLayers+1][0])
        print(maxFlow)
        drawFlowNetwork(graphEdges, graphLayers, edgeValues)
    else:
        sys.exit("Please provide valide mode, [task1, task2]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 3:
        sys.exit(
            "Please provide two arguments, first is the mode [task1, task2], second is the number of layers"
        )

    main(programArguments[1], int(programArguments[2]))
