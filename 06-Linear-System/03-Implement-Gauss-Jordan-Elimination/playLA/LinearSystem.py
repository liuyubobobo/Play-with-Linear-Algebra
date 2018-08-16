from .Matrix import Matrix
from .Vector import Vector


class LinearSystem:

    def __init__(self, matrix, vector):

        self._m = matrix.row_num()
        self._n = matrix.col_num()
        self.Ab = []

        for i in range(self._m):
            row = matrix.row_vector(i)
            self.Ab.append(Vector(row.underlying_list() + [vector[i]]))

    def _max_pivot(self, index, n):

        best, ret = self.Ab[index][index], index
        for i in range(index + 1, n):
            if self.Ab[i][index] > best:
                best, ret = self.Ab[i][index], i
        return ret

    def _forward(self):

        n = min(self._m, self._n)
        for i in range(n):
            # Ab[i][i]为主元
            max_row = self._max_pivot(i, n)
            self.Ab[i], self.Ab[max_row] = self.Ab[max_row], self.Ab[i]

            self.Ab[i] = self.Ab[i] / self.Ab[i][i] # TODO self.Ab[i][i] == 0?
            for j in range(i + 1, n):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    def _backward(self):

        n = min(self._m, self._n)
        for i in range(n - 1, -1, -1):
            # Ab[i][i]为主元
            for j in range(i - 1, -1, -1):
                self.Ab[j] = self.Ab[j] - self.Ab[j][i] * self.Ab[i]

    def gauss_jordan_elimination(self):

        self._forward()
        self._backward()

    def fancy_print(self):

        for i in range(self._m):
            print(" ".join(str(self.Ab[i][j]) for j in range(self._n)), end=" ")
            print("|", self.Ab[i][-1])
