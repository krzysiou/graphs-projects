import numpy as np
from utils import sortList, sortDict


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

