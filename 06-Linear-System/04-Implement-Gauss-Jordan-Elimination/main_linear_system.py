from playLA.Matrix import Matrix
from playLA.Vector import Vector
from playLA.LinearSystem import LinearSystem


if __name__ == "__main__":

    A1 = Matrix([[1, -3, 5], [2, -1, -3], [3, 1, 4]])
    b1 = Vector([-9, 19, -13])
    ls1 = LinearSystem(A1, b1)
    ls1.gauss_jordan_elimination()
    ls1.fancy_print()
    print()

    A2 = Matrix([[1, 1, 1], [1, -1, -1], [2, 1, 5]])
    b2 = Vector([3, -1, 8])
    ls2 = LinearSystem(A2, b2)
    ls2.gauss_jordan_elimination()
    ls2.fancy_print()
    print()

    A3 = Matrix([[1, 2, -2], [2, -3, 1], [3, -1, 3]])
    b3 = Vector([6, -10, -16])
    ls3 = LinearSystem(A3, b3)
    ls3.gauss_jordan_elimination()
    ls3.fancy_print()
    print()

    A4 = Matrix([[3, 1, -2], [5, -3, 10], [7, 4, 16]])
    b4 = Vector([4, 32, 13])
    ls4 = LinearSystem(A4, b4)
    ls4.gauss_jordan_elimination()
    ls4.fancy_print()
    print()

    A5 = Matrix([[6, -3, 2], [5, 1, 12], [8, 5, 1]])
    b5 = Vector([31, 36, 11])
    ls5 = LinearSystem(A5, b5)
    ls5.gauss_jordan_elimination()
    ls5.fancy_print()
    print()
