from .Matrix import Matrix
from .LinearSystem import rank


def gram_schmidt_process(basis):

    matrix = Matrix(basis)
    assert rank(matrix) == len(basis)

    res = [basis[0]]
    for i in range(1, len(basis)):
        p = basis[i]
        for r in res:
            p = p - basis[i].dot(r) / r.dot(r) * r
        res.append(p)
    return res;


def qr(A):

    assert A.row_num() == A.col_num(), "A must be square"

    basis = [A.col_vector(i) for i in range(A.col_num())];
    P = gram_schmidt_process(basis)
    Q = Matrix([v / v.norm() for v in P]).T()
    R = Q.T().dot(A)

    return Q, R
