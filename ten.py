class MealyError(Exception):
    pass


class StateMachine:
    def __init__(self):
        self.state = 'A'

    def wreck(self):
        if self.state == 'A':
            self.state = 'B'
            return 0
        if self.state == 'C':
            self.state = 'D'
            return 2
        if self.state == 'D':
            self.state = 'E'
            return 3
        if self.state == 'E':
            self.state = 'G'
            return 6
        if self.state == 'F':
            self.state = 'A'
            return 8
        raise MealyError('wreck')

    def crawl(self):
        if self.state == 'B':
            self.state = 'C'
            return 1
        if self.state == 'D':
            self.state = 'F'
            return 4
        if self.state == 'E':
            self.state = 'F'
            return 5
        if self.state == 'F':
            self.state = 'G'
            return 7
        if self.state == 'G':
            self.state = 'A'
            return 9
        raise MealyError('crawl')


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
    assert o.wreck() == 0
    assert o.crawl() == 1
    assert o.wreck() == 2
    assert o.wreck() == 3
    assert o.crawl() == 5
    assert o.wreck() == 8
    assert o.wreck() == 0
    assert o.crawl() == 1
    assert o.wreck() == 2
    assert o.crawl() == 4
    assert o.crawl() == 7
    assert o.crawl() == 9
    assert o.wreck() == 0
    assert o.crawl() == 1
    assert o.wreck() == 2
    assert o.wreck() == 3
    assert o.wreck() == 6
    raises(lambda: o.wreck(), MealyError)
