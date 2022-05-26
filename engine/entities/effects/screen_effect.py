import pygame
from typing import Optional


class ScreenEffect(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, duration: int):
        super().__init__()
        self._x: int = x
        self._y: int = y
        self._duration: int = duration
        self._animation_frame = 0
        self._bounding_box: Optional[pygame.Rect] = None
        self._image: Optional[pygame.image] = None

    def increase_animation_frame(self):
        if self._animation_frame >= self._duration:
            return
        self._animation_frame += 1

    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, self._bounding_box)

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
    def animation_frame(self) -> int:
        return self._animation_frame

    @animation_frame.setter
    def animation_frame(self, value: int):
        self._animation_frame = value

    @property
    def effect_duration(self) -> int:
        return self._duration
