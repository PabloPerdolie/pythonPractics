import math


def f(y, x, z):
    res = 0
    for i in range(1, len(y) + 1):
        x1 = 6 * x[i - 1] ** 3 - 67 * y[i - 1] ** 2 - 83 * z[len(y) - i]
        res += (math.exp(x1) ** 5) / 95
    return res * 47


def main(y, x, z):
    return f(y, x, z)


y2 = [-0.69, 0.17, -0.07, -0.59, -0.85, 0.02, 0.81]
x2 = [-0.12, -0.14, -0.8, -0.24, -0.27, -0.83, -0.38]
z2 = [-0.33, 0.21, -0.31, 0.59, 0.21, -0.48, -0.3]
result = main(y2, x2, z2)
