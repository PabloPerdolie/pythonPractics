# def f(b, m):
#     res = 0
#     for j in range(1, m + 1):
#         for c in range(1, b + 1):
#             res += 31 * (j / 65 - 0.06 - j ** 3) ** 6 + 93 * (c ** 4)
#     for j in range(1, m + 1):
#         res += 24 * (72 * j - 0.03) ** 3
#     return res
import math


def f(b, n, m, x):
    res = 0
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            for c in range(1, b + 1):
                res += 42 * (math.floor(j - 4 * (i ** 3) - c ** 2)) ** 4
                res -= (math.log(x, 2) ** 7) / 72
    return res


def main(b, n, m, x):
    return f(b, n, m, x)


result = main(8, 5, 6, 0.51)
