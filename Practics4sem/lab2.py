import math


def f(z):
    if z < 158:
        return (z ** 5) / 72 + (math.ceil(z) ** 3) + math.log(z) / 58
    elif 158 <= z < 248:
        func1 = (z ** 5) / 22 - 61 * math.tan(45 - 95 * z)
        func2 = math.cos(z ** 2 - (z ** 3) / 47) ** 4
        return func1 - func2
    elif 248 <= z < 305:
        return abs(94 * z) ** 4 - 63 * (z ** 3)
    else:
        return (math.cos(z) ** 5) / 46 + 68 * z


def main(z):
    return f(z)


result = main(312)
