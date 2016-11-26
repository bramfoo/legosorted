from legoPlatform.direction import Direction
from sort import Sort


class Box:

    garbage_direction = Direction.up

    def __init__(self):
        self.color = None
        self.shape = None
        self.sort = None
        self.dimension = None
        self.slots = []
        self.reset()

    def reset(self):
        self.set_preferences(None, None, None, Sort.color)
        self.slots = [
            Slot(Direction.left),
            Slot(Direction.down),
            Slot(Direction.right),
            Slot(Box.garbage_direction)
        ]

    def offer(self, lego_block):

        for slot in self.slots:
            if slot.try_place_block(lego_block, self.color, self.shape, self.dimension, self.sort):
                return slot.direction

        # We couldn't find a slot for the block, put it in the last slot
        return self.slots[-1].direction

    def set_preferences(self, color, shape, dimension, sort):
        self.color = color
        self.shape = shape
        self.dimension = dimension
        self.sort = sort


class Slot:

    def __init__(self, direction):
        self.direction = direction
        self.blocks = []

    def try_place_block(self, new_lego_block, color, shape, dimension, sort):

        can_place_block = True
        is_empty = len(self.blocks) == 0
        current_lego_block = None if is_empty else self.blocks[0]

        # Sort on 1 specific dimension
        if dimension is not None:
            can_place_block = can_place_block and new_lego_block.has_dimension(dimension)

        # Sort on 1 specific color
        if color is not None:
            can_place_block = can_place_block and new_lego_block.color == color

        # Sort on 1 specific shape
        if shape is not None:
            can_place_block = can_place_block and new_lego_block.shape == shape

        # Sort on (any) color or (any) shape
        if sort is not None:
            # Sort on color or shape
            if sort == Sort.color:
                can_place_block = can_place_block and (is_empty or new_lego_block.color == current_lego_block.color)
            else:
                can_place_block = can_place_block and (is_empty or new_lego_block.shape == current_lego_block.shape)

        if can_place_block:
            self.blocks.append(new_lego_block)

        return can_place_block
