from enum import Enum
import pygame


class ItemType(Enum):
    COIN = 1
    HEALTH = 2


class Collectible:
    def __init__(self, x: int, y: int, item_type: ItemType):
        self._x = x
        self._y = y
        self._item_type = item_type
        self._bounding_box = pygame.Rect(x, y, 32, 32)

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        if not isinstance(value, int):
            raise ValueError("x must be an int")
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        if not isinstance(value, int):
            raise ValueError("y must be an int")
        self._y = value

    @property
    def item_type(self) -> ItemType:
        return self._item_type

    @item_type.setter
    def item_type(self, value: ItemType):
        if not isinstance(value, ItemType):
            raise ValueError("item_type must be an ItemType")
        self._item_type = value

    @property
    def bounding_box(self) -> pygame.Rect:
        return self._bounding_box
