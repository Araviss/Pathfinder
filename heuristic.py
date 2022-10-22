from math import dist


class Heuristics:

    def calc_euclidean(self, x, y):
        d = dist(x, y)
        return d

    def calc_manhattan(self, x, y):
        d = sum(abs(val1 - val2) for val1, val2 in zip(x, y))
        return d
