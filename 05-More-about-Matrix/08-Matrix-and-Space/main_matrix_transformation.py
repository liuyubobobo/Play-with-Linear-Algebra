import matplotlib.pyplot as plt
from playLA.Matrix import Matrix
from playLA.Vector import Vector
import math


if __name__ == "__main__":

    points = [[0, 0], [0, 5], [3, 5], [3, 4], [1, 4], [1, 3], [2, 3], [2, 2], [1, 2], [1, 0]]
    x = [point[0] for point in points]
    y = [point[1] for point in points]

    plt.figure(figsize=(5, 5))
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    plt.plot(x, y)
    # plt.show()

    P = Matrix(points)

    # T = Matrix([[2, 0], [0, 1.5]])
    # T = Matrix([[1, 0], [0, -1]])
    # T = Matrix([[-1, 0], [0, 1]])
    # T = Matrix([[-1, 0], [0, -1]])
    # T = Matrix([[1, 0.5], [0, 1]])
    # T = Matrix([[1, 0], [0.5, 1]])

    # theta = math.pi / 3
    # T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

    # 逆时针旋转90度
    # theta = math.pi / -2
    # T = Matrix([[math.cos(theta), math.sin(theta)], [-math.sin(theta), math.cos(theta)]])

    # 根据矩阵表示空间的法则，直接写出的逆时针旋转90度的变换矩阵
    T = Matrix([[0, -1], [1, 0]])

    P2 = T.dot(P.T())
    plt.plot([P2.col_vector(i)[0] for i in range(P2.col_num())],
             [P2.col_vector(i)[1] for i in range(P2.col_num())])
    plt.show()