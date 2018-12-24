from playLA.Vector import Vector
from playLA.GramSchmidtProcess import gram_schmidt_process
from itertools import product


if __name__ == "__main__":

    basis1 = [Vector([2, 1]), Vector([1, 1])]
    res1 = gram_schmidt_process(basis1)
    for row in res1:
        print(row)

    res1 = [row / row.norm() for row in res1]
    for row in res1:
        print(row)
    print(res1[0].dot(res1[1]))
    print()


    basis2 = [Vector([2, 3]), Vector([4, 5])]
    res2 = gram_schmidt_process(basis2)
    res2 = [row / row.norm() for row in res2]
    for row in res2:
        print(row)
    print(res2[0].dot(res2[1]))
    print()


    basis3 = [Vector([1, 0, 1]), Vector([3, 1, 1]), Vector([-1, -1, -1])]
    res3 = gram_schmidt_process(basis3)
    res3 = [row / row.norm() for row in res3]
    for row in res3:
        print(row)
    print(sum(res3[i].dot(res3[j]) for i, j in product(range(3), repeat=2) if i != j))
    print()


    basis4 = [Vector([1, 1, 5, 2]), Vector([-3, 3, 4, -2]), Vector([-1, -2, 2, 5])]
    res4 = gram_schmidt_process(basis4)
    res4 = [row / row.norm() for row in res4]
    for row in res4:
        print(row)
    print(sum(res4[i].dot(res4[j]) for i, j in product(range(3), repeat=2) if i != j))
    print()


    basis5 = [Vector([1, 2, 3, 4]), Vector([2, 1, 1, 0]), Vector([3, 0, -1, 3])]
    res5 = gram_schmidt_process(basis5)
    res5 = [row / row.norm() for row in res5]
    for row in res5:
        print(row)
    print(sum(res5[i].dot(res5[j]) for i, j in product(range(3), repeat=2) if i != j))
    print()
