import sys

from dataTransformations.algorithms import *
from utils import *

def main(mode, nodesCount=12, propability=0.4):
    #edges = generateDigraph(nodesCount, propability)
    #NL = convertEdgesToNeighbourList(edges)
    #zakomentowana wersja z generacją losowego digrafu
    #poniżej krawędzie i lista sąsiedztwa dla podanego przykładu 
    edges = [[0,4], [0,5], [0,8], [1,0], [1,2], [1,5], [2,1], [2,3] ,[2,4] , [2,11] ,[3,2] ,[3,4] ,[3,7] ,[3,8] ,[3,10] ,[4,2] ,[4,6] ,[4,7] ,[4,8] ,[5,1] ,[5,6] ,[6,4] , [6,5] ,[6,7] ,[7,3] ,[7,6] ,[7,8] ,[7,11] , [8,3] ,[8,4] ,[8,7] ,[8,9] ,[9,8] ,[10,3] ,[10,8] ,[11,0] ,[11,7]]
    NL = [[4,5,8], [0,2,5], [1,3,4,11], [2,4,7,8,10], [2,6,7,8], [1,6], [4,5,7], [3,6,8,11], [3,4,7,9], [8], [3,8], [0,7]]
    if mode == "pagerank1":
        #drawGraph(edges)
        pageRank1(NL, 0.15)
    elif mode == "pagerank2":
        #drawGraph(edges)
        pageRank2(NL, 0.15)
    else:
        sys.exit("Please provide valide mode, [pagerank1, pagerank2]")


if __name__ == "__main__":
    programArguments = sys.argv

    if len(programArguments) != 4:
        sys.exit(
            "Please provide three arguments, first is the mode [pagerank1, pagerank2], second is the number of nodes of a generated digraph, third is the propability of generating an edge from range [0, 1]"
        )

    main(programArguments[1], int(programArguments[2]), float(programArguments[3]))
