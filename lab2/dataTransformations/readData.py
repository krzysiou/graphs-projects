def readMatrix(file_name):
    with open(file_name, "r") as file:
        result = [[int(num) for num in line.split()] for line in file]

    return result


def readList(file_name):
    with open(file_name, "r") as file:
        result = [[int(num) for num in line.split()[1:]] for line in file]

    return result


def readLine(file_name):
    with open(file_name, "r") as file:
        result = [int(num) for num in file.readline().split()]

    return result
