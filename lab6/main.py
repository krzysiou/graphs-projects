import sys

from dataTransformations.algorithms import *
from utils import *

def main(mode, nodesCount=12, propability=0.4):
    edges = generateDigraph(nodesCount, propability)
    NL = convertEdgesToNeighbourList(edges)
    #NL = [[4,5,8], [0,2,5], [1,3,4,11], [2,4,7,8,10], [2,6,7,8], [1,6], [4,5,7], [3,6,8,11], [3,4,7,9], [8], [3,8], [0,7]]
    if mode == "pagerank1":
        pageRank1(NL, 0.15)
    elif mode == "pagerank2":
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
