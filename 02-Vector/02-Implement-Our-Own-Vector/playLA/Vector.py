class Vector:

    def __init__(self, lst):
        self._values = lst

    def __getitem__(self, index):
        """取向量的第index个元素"""
        return self._values[index]

    def __len__(self):
        """返回向量长度（有多少个元素）"""
        return len(self._values)

    def __repr__(self):
        return "Vector({})".format(self._values)

    def __str__(self):
        return "({})".format(", ".join(str(e) for e in self._values))
