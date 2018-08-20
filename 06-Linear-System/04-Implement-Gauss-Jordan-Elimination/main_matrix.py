from playLA.Vector import Vector
from playLA.Matrix import Matrix


if __name__ == "__main__":

    matrix = Matrix([[1, 2], [3, 4]])
    print(matrix)
    print("matrix.shape = {}".format(matrix.shape()))
    print("matrix.size = {}".format(matrix.size()))
    print("len(matrix) = {}".format(len(matrix)))
    print("matrix[0][0] = {}".format(matrix[0, 0]))

    matrix2 = Matrix([[5, 6], [7, 8]])
    print(matrix2)
    print("add: {}".format(matrix + matrix2))
    print("subtract: {}".format(matrix - matrix2))
    print("scalar-mul: {}".format(2 * matrix))
    print("scalar-mul: {}".format(matrix * 2))
    print("zero_2_3: {}".format(Matrix.zero(2, 3)))

    T = Matrix([[1.5, 0], [0, 2]])
    p = Vector([5, 3])
    print("T.dot(p) = {}".format(T.dot(p)))

    P = Matrix([[0, 4, 5], [0, 0, 3]])
    print("T.dot(P) = {}".format(T.dot(P)))

    print("A.dot(B) = {}".format(matrix.dot(matrix2)))
    print("B.dot(A) = {}".format(matrix2.dot(matrix)))

    print("P.T = {}".format(P.T()))

    I = Matrix.identity(2)
    print(I)
    print("A.dot(I) = {}".format(matrix.dot(I)))
    print("I.dot(A) = {}".format(I.dot(matrix)))
