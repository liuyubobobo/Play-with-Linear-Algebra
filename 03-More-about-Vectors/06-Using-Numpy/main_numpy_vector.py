import numpy as np

if __name__ == "__main__":

    # np.array 基础
    lst = [1, 2, 3]
    lst[0] = "Linear Algebra"
    print(lst)

    vec = np.array([1, 2, 3])
    print(vec)
    # vec[0] = "Linear Algebra"

    # np.array的创建
    print(np.zeros(5))
    print(np.ones(5))
    print(np.full(5, 666))
    print(np.arange(0, 20, 2))
    print(np.arange(0, 10))
    print(np.arange(10))
    print(np.arange(0, 1, 0.2))
    print(np.linspace(0, 1, 10))
    print(np.linspace(0, 1, 11))

    #np.array的基本属性
    print(vec)
    print("ndim =", vec.ndim)
    print("size =", vec.size)
    print("size =", len(vec))
    print(vec[0])
    print(vec[-1])
    print(vec[0:2])

    #np.array的基本运算
    vec2 = np.array([4, 5, 6])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))
    print("{} * {} = {}".format(2, vec, 2 * vec))
    print("{} * {} = {}".format(vec, vec2, vec * vec2))
    print("{}.dot({}) = {}".format(vec, vec2, vec.dot(vec2)))

    print(np.linalg.norm(vec))
    print(vec / np.linalg.norm(vec))

    zero3 = np.zeros(3)
    print(zero3 / np.linalg.norm(zero3))
