import math


def main(y, x, z):

    func1 = (83 + (y ** 3) / 21 + y) ** 6
    func4 = 86 * (49 * (x ** 2) + x + (z ** 3) / 54) ** 5
    func2 = 17 * (59 * y + 37 * (x ** 2) + 63 * (y ** 3)) ** 7
    func3 = math.floor(y + 61 * (z ** 2) + 1) ** 2
    res_func = (func1 + func4) ** 0.5 - (func2 - func3)
    return res_func


result = main(0.73, 0.25, 0.91)
