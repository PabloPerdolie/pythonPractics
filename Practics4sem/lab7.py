def main(x):
    x = bin(x)[2:]
    if len(x) < 38:
        x = "0" * (38 - len(x)) + x
    j5 = x[0:3]
    j4 = x[3:13]
    j3 = x[13:23]
    j12 = x[23:]
    x = j5 + j3 + j4 + j12
    return str(int(x, 2))