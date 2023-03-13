import numpy as np
from utils import sortList, sortDict, generateEdgesList


def degree_seq(A, verbose=False):
  n = len(A)
  sortList(A, mode="desc")
  A = np.array(A)
  if verbose:
    print(A)
  while True:
    if np.all(A == 0):
      return True
    if A[0] > n or np.any(A < 0):
      return False

    A[1:A[0] + 1] = A[1:A[0] + 1] - 1
    A[0] = 0
    sortList(A, mode="desc")
    if verbose:
      print(A)


def constructNLFromSeq(A, verbose=False):
  if not degree_seq(A):
    raise Exception("Wrong sequence")
  n = len(A)
  A = np.array(A)
  A = {index + 1: val for index, val in enumerate(A)}
  sortDict(A, mode="desc")
  if verbose:
    print(A)
  neighbourList = [[] for _ in range(n)]

  while True:
    if np.all(np.array(list(A.values())) == 0):
      return neighbourList

    for i in range(1, list(A.values())[0] + 1):
      A[list(A.keys())[i]] = A[list(A.keys())[i]] - 1
      neighbourList[list(A.keys())[0] - 1].append(list(A.keys())[i] - 1)

    A[list(A.keys())[0]] = 0
    sortDict(A, mode="desc")
    if verbose:
      print(A)


def randomizeEdges(NL, number, verbose=False):
  edges = generateEdgesList(NL)
  numberOfEdges = len(edges)
  if numberOfEdges == 0:
    return edges
  i = 0
  while i < number:
    randAB = np.random.randint(0, numberOfEdges)
    randCD = randAB
    while randCD == randAB:
      randCD = np.random.randint(0, numberOfEdges)

    if verbose:
      print(f'{edges[randAB]}, {edges[randCD]} => ', end="")

    AB = list(edges[randAB])
    CD = list(edges[randCD])
    AB[0], AB[1], CD[0], CD[1] = AB[0], CD[1], AB[1], CD[0]

    if tuple(AB) not in edges \
            and tuple(CD) not in edges \
            and AB[0] != AB[1] and CD[0] != CD[1]:  # check if it is not multiedge or loop
      edges[randAB], edges[randCD] = tuple(AB), tuple(CD)
      if verbose:
        print(f'{edges[randAB]}, {edges[randCD]}')
    else:
      print("Skip..")
      i -= 1
    i += 1

  return edges
