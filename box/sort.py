from enum import Enum


class Sort(Enum):
    color = 1,
    shape = 2

    @staticmethod
    def from_string(value):
        if value is None:
            return None
        return Sort.color if value == 'color' else Sort.shape
