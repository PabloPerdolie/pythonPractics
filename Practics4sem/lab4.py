def f(n):
    if n == 0:
        return -0.93
    elif n == 1:
        return 0.72
    elif n >= 2:
        return f(n - 1) + 60 - (f(n - 2) ** 2) / 58 + 68


def main(n):
    return f(n)


result = main(5)
