import numpy as np
from numpy.linalg import eig, inv
from playLA.LinearSystem import rank
from playLA.Matrix import Matrix


def diagonalize(A):

    assert A.ndim == 2
    assert A.shape[0] == A.shape[1]

    eigenvalues, eigenvectors = eig(A)

    P = eigenvectors
    if rank(Matrix(P.tolist())) != A.shape[0]:
        print("Matrix can not be diagonalized!")
        return None, None, None

    D = np.diag(eigenvalues)
    Pinv = inv(P)

    return P, D, Pinv


if __name__ == "__main__":

    A1 = np.array([[4, -2],
                   [1, 1]])
    P1, D1, Pinv1 = diagonalize(A1)
    print(P1)
    print(D1)
    print(Pinv1)
    print(P1.dot(D1).dot(Pinv1))
    print()


    A2 = np.array([[3, 1],
                   [0, 3]])
    P2, D2, Pinv2 = diagonalize(A2)
    print(P2)
    print(D2)
    print(Pinv2)
    print()
