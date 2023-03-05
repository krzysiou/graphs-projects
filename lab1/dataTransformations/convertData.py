from dataTransformations.helperMethods import *

def convertNeighbourMatrix(neighbourMatrix):
    #####  NM -> IN
    incidentMatrix = nm2in(neighbourMatrix)
    #####  NM -> NL
    neighbourList = in2nl(incidentMatrix)
    return incidentMatrix, neighbourList


def convertIncidentMatrix(incidentMatrix):
    #####  IN -> NL
    neighbourList = in2nl(incidentMatrix)
    #####  IN -> NM
    neighbourMatrix = nl2nm(neighbourList)
    return neighbourList, neighbourMatrix

def convertNeighbourList(neighbourList):
    ######  NL -> NM
    neighbourMatrix = nl2nm(neighbourList)
    #####  NL -> IN
    incidentMatrix = nm2in(neighbourMatrix)
    return neighbourMatrix, incidentMatrix
