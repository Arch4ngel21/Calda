import pygame

from utilities.map_direction import MapDirection
from gui.main_screen import MainScreen


class Missile:
    def __init__(self, x: int, y: int, velocity: int, facing: MapDirection, lifespan: int = 10, rec_width: int = 8,\
                 rec_height: int = 8, damage: int = 3):
        self._x: int = x
        self._y: int = y
        self._start_x: int = x
        self._start_y: int = y
        self._animation_frame: int = 0
        self._velocity: int = velocity
        self._facing: MapDirection = facing
        self._lifespan: int = lifespan
        self._damage: int = damage
        self._rect: pygame.Rect = pygame.Rect(x, y, rec_width, rec_height)

    def should_animation_end(self) -> bool:
        return abs(self._x - self._start_x) >= self._lifespan*32 or abs(self._y-self._start_y) >= self._lifespan*32 or\
               self._x + self._velocity >= MainScreen.WINDOW_WIDTH or self._x-self._velocity < 0 or\
               self._y + self._velocity >= MainScreen.WINDOW_HEIGHT or self._y - self._velocity < 0

    def move(self):
        if self._facing == MapDirection.NORTH and self._y - self._velocity >= 0:
            self._y -= self._velocity
        if self._facing == MapDirection.EAST and self._x + self._velocity <= MainScreen.WINDOW_WIDTH:
            self._x += self._velocity
        if self._facing == MapDirection.SOUTH and self._y + self._velocity <= MainScreen.WINDOW_HEIGHT:
            self._y += self._velocity
        if self._facing == MapDirection.WEST and self._x - self._velocity >= 0:
            self._x -= self._velocity

    """add more getters/setters if needed"""
    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
