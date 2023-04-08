import sys

from dataTransformations.algorithms import *
from utils import *


def main(mode):
    if mode == "task1":
        vertPosDict, layerList = generateVertices(7)
        generateMinimalEdges(layerList)
    else:
        sys.exit("Please provide valid mode, [task1, task2]")