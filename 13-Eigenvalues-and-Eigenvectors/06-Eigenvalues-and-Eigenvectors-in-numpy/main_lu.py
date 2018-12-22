from playLA.Matrix import Matrix
from playLA.LU import lu


if __name__ == "__main__":
    A1 = Matrix([[1, 2, 3], [4, 5, 6], [3, -3, 5]])
    L1, U1 = lu(A1)
    print(L1)
    print(U1)
    print(L1.dot(U1))

    print()

    A2 = Matrix([[1, 4, 5, 3], [5, 22, 27, 11], [6, 19, 27, 31], [5, 28, 35, -8]])
    L2, U2 = lu(A2)
    print(L2)
    print(U2)
    print(L2.dot(U2))

    print()

    A3 = Matrix([[1, 2, 3], [3, 7, 14], [4, 13, 38]])
    L3, U3 = lu(A3)
    print(L3)
    print(U3)
    print(L3.dot(U3))

    print()
