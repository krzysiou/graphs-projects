import sys

from dataTransformations.readData import *
from dataTransformations.convertData import *
from utils import *


def main(mode, file_name):
  # apply proper convert method based on execution flag
  if(mode == "NM"):
    data = readMatrix(file_name)
    converted = convertNeighbourMatrix(data)

  elif(mode == "IN"):
    data = readMatrix(file_name)
    converted = convertIncidentMatrix(data)

  elif(mode == "NL"):
    data = readList(file_name)
    converted = convertNeighbourList(data)
    
  else:
    sys.exit('Please provide valide mode, [NM, IN, NL]')
  
  # two other representations other than provided one
  result1, result2 = converted

  # print converted representations
  displayRsult(result1)
  displayRsult(result2)

  # draw the graph
  drawGraph(data)

if __name__ == '__main__':
  programArguments = sys.argv

  if(len(programArguments) != 3):
    sys.exit('Please provide two arguments, first is the mode [NM, IN, NL], second one is input file name.')
  
  main(programArguments[1], programArguments[2])