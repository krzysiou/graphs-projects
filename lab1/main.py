import sys

from dataTransformations.readData import *
from dataTransformations.convertData import *
from dataTransformations.displayData import *
from utils import *


def main(mode, context):
    if mode == "NM":
        neighbourMatrix = readMatrix(context)
        incidentMatrix, neighbourList = convertNeighbourMatrix(neighbourMatrix)

        displayMatrix(incidentMatrix)
        displayList(neighbourList)

        drawGraph(neighbourList)

    elif mode == "IN":
        incidentMatrix = readMatrix(context)
        neighbourList, neighbourMatrix = convertIncidentMatrix(incidentMatrix)

        displayMatrix(neighbourMatrix)
        displayList(neighbourList)

        drawGraph(neighbourList)

    elif mode == "NL":
        neighbourList = readList(context)
        neighbourMatrix, incidentMatrix = convertNeighbourList(neighbourList)

        displayMatrix(neighbourMatrix)
        displayMatrix(incidentMatrix)

        drawGraph(neighbourList)

    elif mode == "RAND":
        neighbourList1 = generateGraphNL(20, 30)
        neighbourList2 = generateGraphNP(5, 0.5)

        drawGraph(neighbourList1)
        drawGraph(neighbourList2)

    else:
        sys.exit("Please provide valide mode, [NM, IN, NL]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 3:
        sys.exit(
            "Please provide two arguments, first is the mode [NM, IN, NL], second one is input file name."
        )

    main(programArguments[1], programArguments[2])
