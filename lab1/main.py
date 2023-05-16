import sys

from dataTransformations.readData import *
from dataTransformations.convertData import *
from dataTransformations.displayData import *
from utils import *


def main(mode, context=None):
    if mode == "NM":
        neighbourMatrix = readMatrix(context)
        incidentMatrix, neighbourList = convertNeighbourMatrix(neighbourMatrix)

        displayMatrix(incidentMatrix)
        displayList(neighbourList)

        drawGraph(neighbourList)

    elif mode == "IM":
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
        neighbourList1 = generateGraphNL(5, 6)
        neighbourList2 = generateGraphNP(5, 0.5)

        drawGraph(neighbourList1)
        drawGraph(neighbourList2)

    else:
        sys.exit("Please provide valide mode, [NM, IM, NL, RAND]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) == 2 and programArguments[1] == "RAND":
        main(programArguments[1])
    elif len(programArguments) != 3:
        sys.exit(
            "Please provide appropriate number of arguments, if your mode is [RAND] just type mode name but if your mode is one of: [NM, IM, NL] you also have to provide input file name."
        )
    else:
        main(programArguments[1], programArguments[2])
