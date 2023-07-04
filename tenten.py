class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def step(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'B':
            self.state = 'E'
            return 2
        if self.state == 'E':
            self.state = 'F'
            return 7
        if self.state == 'F':
            self.state = 'G'
            return 8
        if self.state == 'G':
            self.state = 'B'
            return 10
        if self.state == 'D':
            self.state = 'A'
            return 5
        raise MealyError('step')

    def zoom(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'C':
            self.state = 'D'
            return 3
        if self.state == 'D':
            self.state = 'E'
            return 4
        if self.state == 'H':
            self.state = 'C'
            return 11
        raise MealyError('zoom')

    def spin(self):
        if self.state == 'D':
            self.state = 'H'
            return 6
        if self.state == 'G':
            self.state = 'H'
            return 9
        raise MealyError('spin')


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
    assert o.step() == 0
    assert o.zoom() == 1
    assert o.zoom() == 3
    assert o.zoom() == 4
    assert o.step() == 7
    assert o.step() == 8
    assert o.step() == 10
    assert o.zoom() == 1
    assert o.zoom() == 3
    assert o.spin() == 6
    assert o.zoom() == 11
    assert o.zoom() == 3
    assert o.step() == 5
    raises(lambda: o.zoom(), MealyError)
    raises(lambda: o.spin(), MealyError)
