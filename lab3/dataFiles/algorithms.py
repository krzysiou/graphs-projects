import numpy as np

def calculateMaxIntegrityNumber(sequence, neighbourList):
    numberOfNodes = len(sequence)
    comp = []
    integrityNumber = 0

    for i in range(numberOfNodes):
        comp.append(-1)

    for i in range(numberOfNodes):
        if comp[i] == -1:
            integrityNumber += 1
            comp[i] = integrityNumber
            components(integrityNumber, i, neighbourList, comp)

    return max(comp)