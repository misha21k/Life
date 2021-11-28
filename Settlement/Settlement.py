"""
>>> settlement = Settlement()
>>> settlement.add_being(Being(1, 0))
>>> settlement.add_being(Being(2, 0))
>>> settlement.add_being(Being(3, 0))
>>> settlement.add_being(Being(3, 1))
>>> settlement.add_being(Being(3, 2))
>>> len(settlement)
5
>>> being = Being(3, 2)
>>> being
Being(3, 2)
>>> being in settlement
True
>>> being.find_alive_neighbors(settlement)
{Being(3, 1)}
>>> being.count_alive_neighbors(settlement)
1
>>> being.count_dead_neighbors(settlement)
7
>>> settlement.remove_being(Being(3, 2))
>>> being in settlement
False
>>> settlement.calculate_next_generation()
>>> len(settlement.dead_neighbors)
14
>>> len(settlement)
4
>>> settlement.clear()
>>> len(settlement)
0
"""


class Being(tuple):

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

    @property
    def neighbors(self):
        """All neighbors of being"""
        neighbors = set()
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                neighbors.add(Being(self.x + i, self.y + j))
        return neighbors

    def find_alive_neighbors(self, settlement):
        """Finds alive neighbors of being"""
        neighbors = set()
        for neighbor in self.neighbors:
            if neighbor in settlement:
                neighbors.add(neighbor)
        return neighbors

    def find_dead_neighbors(self, settlement):
        """Finds dead neighbors of being"""
        neighbors = set()
        for neighbor in self.neighbors:
            if neighbor not in settlement:
                neighbors.add(neighbor)
        return neighbors

    def count_alive_neighbors(self, settlement):
        return len(self.find_alive_neighbors(settlement))

    def count_dead_neighbors(self, settlement):
        return len(self.find_dead_neighbors(settlement))


class Settlement:

    def __init__(self):
        self.__beings = set()

    @property
    def being(self):
        return self.__beings

    def __contains__(self, being):
        return being in self.__beings

    def __iter__(self):
        return iter(self.__beings)

    def __len__(self):
        return len(self.__beings)

    def add_being(self, being):
        self.__beings.add(being)

    def remove_being(self, being):
        self.__beings.remove(being)

    def clear(self):
        self.__beings = set()

    @property
    def dead_neighbors(self):
        """Returns dead neighbors of all beings"""
        dead_neighbors = set()
        for being in self:
            dead_neighbors |= being.find_dead_neighbors(self)
        return dead_neighbors

    def calculate_next_generation(self):
        """Calculates next configuration (generation) of settlement

        If being has three neighbors, it is born. If being has
        less two neighbors or more three neighbors, it dies
        """
        next_generation = set()
        for being in self:
            if being.count_alive_neighbors(self) in (2, 3):
                next_generation.add(being)
        for being in self.dead_neighbors:
            if being.count_alive_neighbors(self) == 3:
                next_generation.add(being)
        self.__beings = next_generation


if __name__ == '__main__':
    import doctest
    doctest.testmod()
