from enum import Enum


class Shape(Enum):
    square = 1
    rectangle = 2

    @staticmethod
    def from_string(value):
        if value is None or value == "":
            return None
        return Shape.square if value == 'square' else Shape.rectangle
