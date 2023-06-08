def main(d):
    d = list(str(i) for i in d)
    x = {
        "2007": {
            "NINJA": {"1967": 0, "2007": {"1962": 1, "1974": 2, "2001": 3}},
            "POD": {"1967": 4, "2007": {"NU": 5, "RAGEL": 6, "R": 7}},
        },
        "2006": {
            "RAGEL": 11,
            "R": 12,
            "NU": {"POD": 10, "NINJA": {"1967": 8, "2007": 9}},
        },
    }

    while not type(x) is int:
        x = x[list(set(d) & set(x.keys()))[0]]

    return x