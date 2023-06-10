class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = "A"

    def fill(self):
        if self.state == "A":
            self.state = "B"
            return 0
        if self.state == "B":
            self.state = "B"
            return 2
        if self.state == "C":
            self.state = "G"
            return 6
        if self.state == "E":
            self.state = "F"
            return 8
        if self.state == "F":
            self.state = "G"
            return 9
        raise MealyError("pull")

    def cue(self):
        if self.state == "B":
            self.state = "C"
            return 1
        if self.state == "C":
            self.state = "D"
            return 3
        if self.state == "D":
            self.state = "E"
            return 7
        raise MealyError("cue")

    def daub(self):
        if self.state == "C":
            self.state = "E"
            return 4
        raise MealyError("daub")

    def skip(self):
        if self.state == "C":
            self.state = "F"
            return 5
        raise MealyError("skip")


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
    assert o.fill() == 0
    assert o.fill() == 2
    assert o.cue() == 1
    assert o.cue() == 3
    assert o.cue() == 7
    assert o.fill() == 8
    assert o.fill() == 9

    o = main()
    assert o.fill() == 0
    assert o.fill() == 2
    assert o.cue() == 1
    assert o.cue() == 3
    assert o.cue() == 7
    raises(lambda: o.cue(), MealyError)  # MealyError
    assert o.fill() == 8
    assert o.fill() == 9
