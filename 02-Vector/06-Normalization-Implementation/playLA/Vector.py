import math
from ._globals import EPSILON

class Vector:

    def __init__(self, lst):
        self._values = lst;

    def __add__(self, another):
        """向量加法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in adding. Length of vectors must be same."

        # return Vector([a + b for a, b in zip(self._values, another._values)])
        return Vector([a + b for a, b in zip(self, another)])

    def __sub__(self, another):
        """向量减法，返回结果向量"""
        assert len(self) == len(another), \
            "Error in subtracting. Length of vectors must be same."

        return Vector([a - b for a, b in zip(self, another)])

    def norm(self):
        return math.sqrt(sum(e**2 for e in self))

    def normalize(self):
        if self.norm() < EPSILON:
            raise ZeroDivisionError("Normalize error! norm is zero.")
        return Vector([e / self.norm() for e in self])

    def __mul__(self, k):
        return Vector([k * e for e in self])

    def __rmul__(self, k):
        return self * k;

    def __pos__(self):
        return 1 * self

    def __neg__(self):
        return -1 * self

    def __iter__(self):
        return self._values.__iter__();

    def __getitem__(self, index):
        return self._values[index]

    def __len__(self):
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(str(self._values))

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))