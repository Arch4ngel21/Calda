from pygame import Rect
from utilities.settings import Settings


class Block:

    def __init__(self, x: int, y: int, block_name: str, is_passable: bool = False):
        self._is_passable: bool = is_passable
        self._block_name: str = block_name
        # self._block_bounding_box = Rect(x, y, Settings.BLOCK_SIZE, Settings.BLOCK_SIZE)

    @property
    def is_passable(self):
        return self._is_passable

    @property
    def block_name(self):
        return self._block_name

    # TODO - Dlaczego blok ma bounding box?
    # @property
    # def block_bounding_box(self):
    #     return self._block_bounding_box
