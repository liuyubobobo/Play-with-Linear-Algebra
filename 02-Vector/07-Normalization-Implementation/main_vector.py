from playLA.Vector import Vector

if __name__ == "__main__":

    vec = Vector([5, 2])
    print(vec)
    print("len(vec) = {}".format(len(vec)))
    print("vec[0] = {}, vec[1] = {}".format(vec[0], vec[1]))

    vec2 = Vector([3, 1])
    print("{} + {} = {}".format(vec, vec2, vec + vec2))
    print("{} - {} = {}".format(vec, vec2, vec - vec2))

    print("{} * {} = {}".format(vec, 3, vec * 3))
    print("{} * {} = {}".format(3, vec, 3 * vec))

    print("+{} = {}".format(vec, +vec))
    print("-{} = {}".format(vec, -vec))

    print("norm({}) = {}".format(vec, vec.norm()))
    print("norm({}) = {}".format(vec2, vec2.norm()))

    print("normalize {} is {}".format(vec, vec.normalize()))
    print("normalize {} is {}".format(vec2, vec2.normalize()))

    print(vec.normalize().norm())
    O = Vector([0., 0., 0.])
    try:
        O.normalize()
    except ZeroDivisionError:
        print("Cannot normalize zero vector.")
    except:
        print("Unknown Error!")
