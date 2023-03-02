def displayMatrix(data):
  for row in data:
    for element in row:
      print(element + " ", end="")
    print()

def displayList(data):
  n = 1
  for row in data:
    print(str(n) + ". ", end="")
    n += 1
    for element in row:
      print(element + " ", end="")
    print()