FACTOR = 1.1


class Coordinates:
    """Coordinates relatively top-left corner
    >>> c = Coordinates(2, 3)
    >>> print(c)
    Coordinates(2, 3)
    >>> d = Coordinates(-1, 5)
    >>> c + d
    Coordinates(1, 8)
    >>> c - d
    Coordinates(3, -2)
    >>> c / 2
    Coordinates(1, 2)
    >>> c % 2
    Coordinates(0, 1)
    >>> c * 3
    Coordinates(6, 9)
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'Coordinates({self.x}, {self.y})'

    __str__ = __repr__

    def __add__(self, other):
        return Coordinates(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Coordinates(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Coordinates(round(self.x * other), round(self.y * other))

    __rmul__ = __mul__

    def __truediv__(self, other):
        return Coordinates(round(self.x / other), round(self.y / other))

    def __mod__(self, other):
        return Coordinates(self.x % other, self.y % other)


class Grid:
    """Parameters of grid
    >>> g = Grid()
    >>> g.origin
    Coordinates(0, 0)
    >>> g.first
    Coordinates(0, 0)
    >>> g.increase(100, 200)
    >>> g.first
    Coordinates(1, 2)
    >>> g.origin
    Coordinates(-10, -20)
    >>> g.cell
    11
    >>> g.decrease(100, 200)
    >>> g.first
    Coordinates(0, 0)
    >>> g.origin
    Coordinates(0, 0)
    >>> g.cell
    10
    >>> g.move(10, -6)
    >>> g.origin
    Coordinates(10, -6)
    >>> g.first
    Coordinates(0, 4)
    """
    def __init__(self, x0=None, y0=None, origin=Coordinates(0, 0), cell=10):
        self.cell = cell  # size of cell
        if x0 and y0:
            self.origin = Coordinates(x0, y0)  # origin of coordinates
        else:
            self.origin = origin

    @property
    def first(self):
        """Coordinates of crossing of first top and first left line"""
        return self.origin % self.cell

    @property
    def x1(self):
        return self.first.x

    @property
    def y1(self):
        return self.first.y

    @property
    def x0(self):
        return self.origin.x

    @property
    def y0(self):
        return self.origin.y

    def increase(self, x_mouse, y_mouse, mouse=None):
        """Increases size of grid"""
        if x_mouse and y_mouse:
            mouse = Coordinates(x_mouse, y_mouse)
        self.cell = round(self.cell * FACTOR)
        self.origin = mouse - FACTOR * (mouse - self.first)

    def decrease(self, x_mouse=None, y_mouse=None, mouse=None):
        """Decreases size of grid"""
        if x_mouse and y_mouse:
            mouse = Coordinates(x_mouse, y_mouse)
        self.cell = round(self.cell / FACTOR)
        self.origin = mouse - (mouse - self.origin) / FACTOR

    def move(self, dx, dy):
        """Moves grid"""
        delta = Coordinates(dx, dy)
        self.origin = self.origin + delta


if __name__ == '__main__':
    import doctest
    doctest.testmod()
