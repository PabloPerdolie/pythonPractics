class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = "A"

    def pull(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "F"
            return 3
        if self.state == "D":
            self.state = "E"
            return 5
        if self.state == "E":
            self.state = "F"
            return 7
        if self.state == "F":
            self.state = "D"
            return 9
        if self.state == "G":
            self.state = "H"
            return 10
        if self.state == "H":
            self.state = "D"
            return 11
        raise MealyError("pull")

    def glare(self):
        if self.state == "A":
            self.state = "F"
            return 1
        if self.state == "B":
            self.state = "C"
            return 2
        if self.state == "C":
            self.state = "D"
            return 4
        if self.state == "D":
            self.state = "D"
            return 6
        if self.state == "F":
            self.state = "G"
            return 8
        raise MealyError("glare")


def main():
    return StateMachine()


def raises(func, error):
    output = None
    try:
        output = func()
    except Exception as e:
        assert type(e) == error
    assert output is None


def test():
    o = main()
    assert o.glare() == 1
    assert o.glare() == 8
    raises(lambda: o.glare(), MealyError)
    assert o.pull() == 10
    assert o.pull() == 11
    assert o.glare() == 6
    assert o.pull() == 5
    assert o.pull() == 7
    assert o.pull() == 9

    o = main()
    assert o.pull() == 0
    assert o.glare() == 2
    raises(lambda: o.pull(), MealyError)
    assert o.glare() == 4

    o = main()
    assert o.pull() == 0
    assert o.pull() == 3