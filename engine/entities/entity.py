import pygame

from utilities.map_direction import MapDirection
from typing import Optional


class Entity:
    def __init__(self, x: int, y: int, health: int, damage: int):
        self._x: int = x
        self._y: int = y
        self._health: int = health
        self._max_health: int = health
        self._damage: int = damage
        self._animation_frame = 0
        self._invincible_frame = 0
        self._facing: MapDirection = MapDirection.NORTH
        self._is_damaged = False
        self._hit_box: Optional[pygame.Rect] = None
        self._bounding_box: Optional[pygame.Rect] = None
            
    def heal(self, health_amount: int):
        self._health += health_amount
        if self._health > self._max_health:
            self._health = self._max_health

    def increase_max_health(self, health_amount: int):
        self._max_health += health_amount

    def is_alive(self):
        return self._health > 0

    def damage(self, damage_amount: int):
        self._health -= damage_amount

    def increase_invincible_frame(self):
        pass

    @property
    def facing(self):
        return self._facing

    @facing.setter
    def facing(self, direction: MapDirection):
        if not isinstance(direction, MapDirection):
            raise ValueError("it must be MapDirection")
        self._facing = direction

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
    def bounding_box(self):
        return self._bounding_box


