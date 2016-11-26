from enum import Enum


class Color(Enum):
    beige = 1
    white = 2
    red = 3
    dark_orange = 4
    green = 5
    yellow = 6

    @staticmethod
    def from_string(value):
        if value is None:
            return None
        if value == 'beige':
            return Color.beige
        if value == 'white':
            return Color.white
        if value == 'red':
            return Color.red
        if value == 'dark_orange':
            return Color.dark_orange
        if value == 'green':
            return Color.green
        if value == 'yellow':
            return Color.yellow
        return None
