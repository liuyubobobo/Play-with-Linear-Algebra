from .Matrix import Matrix
from .Vector import Vector
from ._globals import is_zero


class LinearSystem:

    def __init__(self, A, b):

        assert A.row_num() == len(b), "row number of A must be equal to the length of b"
        self._m = A.row_num()
        self._n = A.col_num()
        # assert self._m == self._n  # TODO: no this restriction

        self.Ab = [Vector(A.row_vector(i).underlying_list() + [b[i]])
                   for i in range(self._m)]
        self.pivots = []

    def _max_row(self, index_i, index_j, n):

        best, ret = self.Ab[index_i][index_j], index_i
        for i in range(index_i + 1, n):
            if self.Ab[i][index_j] > best:
                best, ret = self.Ab[i][index_j], i
        return ret

    def _forward(self):

        i, k = 0, 0
        while i < self._m and k < self._n:
            # 看Ab[i][k]位置是否可以是主元
            max_row = self._max_row(i, k, self._m)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            if is_zero(self.Ab[i][k]):
                k += 1
            else:
                # 将主元归为一
                self.Ab[i] = self.Ab[i] / self.Ab[i][k]
                for j in range(i + 1, self._m):
                    self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]
                self.pivots.append(k)
                i += 1

    def _backward(self):

        n = len(self.pivots)
        for i in range(n - 1, -1, -1):
            k = self.pivots[i]
            # Ab[i][k]为主元
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][k] * self.Ab[i]

    def gauss_jordan_elimination(self):
        """如果有解，返回True；如果没有解，返回False"""
        self._forward()
        self._backward()

        for i in range(len(self.pivots), self._m):
            if not is_zero(self.Ab[i][-1]):
                return False
        return True

    def fancy_print(self):

        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])
