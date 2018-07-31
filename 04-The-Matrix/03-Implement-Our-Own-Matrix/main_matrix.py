from playLA.Matrix import Matrix


if __name__ == "__main__":

    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print("matrix.shape = {}".format(matrix.shape()))
    print("matrix.size = {}".format(matrix.size()))
    print("matrix[0][0] = {}".format(matrix[0, 0]))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print(matrix2)
    print("add: {}".format(matrix + matrix2))
    print("substract: {}".format(matrix - matrix2))
    print("scalar-mul: {}".format(2 * matrix))
    print("scalar-mul: {}".format(matrix * 2))
