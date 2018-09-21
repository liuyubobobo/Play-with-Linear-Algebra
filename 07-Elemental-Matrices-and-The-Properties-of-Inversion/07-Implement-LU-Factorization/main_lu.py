from playLA.Matrix import Matrix
from playLA.LU import lu


if __name__ == "__main__":

    A = Matrix([[1, 2, 3], [4, 5, 6], [3, -3, 5]])
    L, U = lu(A)
    print(L)
    print(U)

    print(L.dot(U))
