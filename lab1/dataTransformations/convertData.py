from dataTransformations.helperMethods import *

def convertNeighbourMatrix(neighbourMatrix):
    incidentMatrix = nm2in(neighbourMatrix)
    neighbourList = in2nl(incidentMatrix)
    
    return incidentMatrix, neighbourList


def convertIncidentMatrix(incidentMatrix):
    neighbourList = in2nl(incidentMatrix)
    neighbourMatrix = nl2nm(neighbourList)

    return neighbourList, neighbourMatrix

def convertNeighbourList(neighbourList):
    neighbourMatrix = nl2nm(neighbourList)
    incidentMatrix = nm2in(neighbourMatrix)

    return neighbourMatrix, incidentMatrix
