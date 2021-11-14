class Being(tuple):

    __slots__ = []

    def __new__(cls, x, y):
        return super().__new__(cls, (x, y))

    @property
    def x(self):
        return self[0]

    @property
    def y(self):
        return self[1]

    def __repr__(self):
        return 'Being({0!r}, {1!r})'.format(self.x, self.y)

    __str__ = __repr__
