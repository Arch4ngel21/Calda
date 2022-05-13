import pygame

from utilities.map_direction import MapDirection
from utilities.settings import Settings


class Missile:
    BOX_SIZE = 8
    def __init__(self, x: int, y: int, velocity: int, facing: MapDirection):
        self._x: int = x
        self._y: int = y
        self._start_x: int = x
        self._start_y: int = y
        self._animation_frame: int = 0
        self._velocity: int = velocity
        self._facing: MapDirection = facing
        self._lifespan: int
        self._damage: int
        self._bound_box: pygame.Rect
    def increase_animation_frame(self):
        pass

    def should_animation_end(self) -> bool:
        return abs(self._x - self._start_x) >= self._lifespan*32 or abs(self._y-self._start_y) >= self._lifespan*32 or\
               self._x + self._velocity >= Settings.GAME_WINDOW_WIDTH or self._x-self._velocity < 0 or\
               self._y + self._velocity >= Settings.GAME_WINDOW_HEIGHT or self._y - self._velocity < 0

    def move(self):
        if self._facing == MapDirection.NORTH and self._y - self._velocity >= 0:
            self._y -= self._velocity
        if self._facing == MapDirection.EAST and self._x + self._velocity <= Settings.GAME_WINDOW_WIDTH:
            self._x += self._velocity
        if self._facing == MapDirection.SOUTH and self._y + self._velocity <= Settings.GAME_WINDOW_HEIGHT:
            self._y += self._velocity
        if self._facing == MapDirection.WEST and self._x - self._velocity >= 0:
            self._x -= self._velocity
        self._bound_box.update(self.x, self.y, self.BOX_SIZE, self.BOX_SIZE)

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
    def bound_box(self) -> pygame.Rect:
        return self._bound_box

    @property
    def damage(self) -> int:
        return self.damage
