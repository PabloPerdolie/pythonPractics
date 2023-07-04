class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = "A"

    def sway(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "D"
            return 2
        if self.state == "E":
            self.state = "C"
            return 6
        if self.state == "H":
            self.state = "F"
            return 11
        raise MealyError("sway")

    def load(self):
        if self.state == "D":
            self.state = "E"
            return 3
        if self.state == "E":
            self.state = "F"
            return 4
        if self.state == "F":
            self.state = "G"
            return 7
        if self.state == "G":
            self.state = "H"
            return 8
        if self.state == "H":
            self.state = "D"
            return 10
        raise MealyError("load")

    def dash(self):
        if self.state == "E":
            self.state = "E"
            return 5
        if self.state == "H":
            self.state = "E"
            return 9
        raise MealyError("dash")


def main():
    return StateMachine()


def test():
    o = main()
    o.sway()
    o.sway()
    o.sway()
    o.load()
    o.sway()
    o.sway()
    o.load()
    o.dash()
    o.load()
    o.load()
    o.load()
    o.sway()
    o.load()
    o.load()
    o.dash()
    o.load()
    o.load()
    o.load()
    o.load()
    try:
        o.sway()
    except MealyError:
        pass
    try:
        o.dash()
    except MealyError:
        pass

    o = main()
    try:
        o.load()
    except MealyError:
        pass
