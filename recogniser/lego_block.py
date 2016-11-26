from shape import Shape
from math import sqrt
from box.dimension import Dimension


class LegoBlock:

    _pixels_per_circle = 35

    def __init__(self, approximated_poly, color):
        dimension1 = LegoBlock.distance(approximated_poly[0], approximated_poly[1])
        dimension2 = LegoBlock.distance(approximated_poly[1], approximated_poly[2])
        length = int((max(dimension1, dimension2) + 10) / LegoBlock._pixels_per_circle)
        width = int((min(dimension1, dimension2) + 10) / LegoBlock._pixels_per_circle)
        self.dimension = Dimension(length, width)
        self.shape = Shape.square if length == width else Shape.rectangle
        self.color = color

    def has_dimension(self, dimension):
        return self.dimension.length == dimension.length and self.dimension.width == dimension.width

    @staticmethod
    def distance(p1, p2):
        x1 = p1[0][0]
        y1 = p1[0][1]
        x2 = p2[0][0]
        y2 = p2[0][1]
        return sqrt((x2 - x1)**2 + (y2 - y1)**2)

    def __str__(self):
        return "LegoBlock{shape=%s, dimension=%s, color=%s}" % (self.shape, self.dimension, self.color)
