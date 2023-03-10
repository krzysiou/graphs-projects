import sys

from dataTransformations.readData import *
from dataTransformations.convertData import *
from dataTransformations.displayData import *
from utils import *


def main(mode, file_name):
    if mode == "NM":
        neighbourMatrix = readMatrix(file_name)
        incidentMatrix, neighbourList = convertNeighbourMatrix(neighbourMatrix)

        displayMatrix(incidentMatrix)
        displayList(neighbourList)

        drawGraph(neighbourList)

    elif mode == "IN":
        incidentMatrix = readMatrix(file_name)
        neighbourList, neighbourMatrix = convertIncidentMatrix(incidentMatrix)

        displayMatrix(neighbourMatrix)
        displayList(neighbourList)

        drawGraph(neighbourList)

    elif mode == "NL":
        neighbourList = readList(file_name)
        neighbourMatrix, incidentMatrix = convertNeighbourList(neighbourList)

        displayMatrix(neighbourMatrix)
        displayMatrix(incidentMatrix)

        drawGraph(neighbourList)

    else:
        sys.exit("Please provide valide mode, [NM, IN, NL]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 3:
        sys.exit(
            "Please provide two arguments, first is the mode [NM, IN, NL], second one is input file name."
        )

    main(programArguments[1], programArguments[2])
