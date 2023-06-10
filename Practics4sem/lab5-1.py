import math


def f(x):
    res = 0
    for i in range(1, len(x) + 1):
        x1 = math.cos(59 * (x[i - 1] ** 3) + 0.01 + x[len(x) - i] ** 2)
        res += x1
    return res


print(f([0.12, 0.2, -0.52, -0.13, -0.3, -0.94, 0.92, -0.99]))
