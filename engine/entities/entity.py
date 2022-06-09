import pygame

from utilities.map_direction import MapDirection
from typing import Optional


class Entity(pygame.sprite.Sprite):
    def __init__(self, x: int, y: int, health: int, damage: int):
        super().__init__()
        self._x: int = x
        self._y: int = y
        self._health: int = health
        self._max_health: int = health
        self._damage: int = damage
        self._animation_frame = 0
        self._invincible_frame = 0
        self._health_bar_frame = 0
        self._facing: MapDirection = MapDirection.WEST
        self._is_damaged = False
        self._hit_box: Optional[pygame.Rect] = None
        self._bounding_box: Optional[pygame.Rect] = None
        self.__health_bar_colors = [(150, 0, 0), (245, 21, 10), (245, 142, 67), (241, 245, 62), (74, 224, 32)]

    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, self._hit_box)
        self.draw_hud(screen)

    def draw_hud(self, screen: pygame.Surface):
        if self._health_bar_frame:

            bar_width = 50
            bar_height = 10
            health_percentage = (self._health / self._max_health)
            color = self.__health_bar_colors[round(health_percentage * 4.0)]

            bar_end = round(health_percentage * bar_width)

            pygame.draw.rect(screen, color, pygame.Rect(self._x - 13, self._y - 14, bar_end - 2, bar_height - 2))
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(self._x - 14, self._y - 15, bar_width, bar_height), 2, 3)

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
        self._health_bar_frame = 100
        # TODO umieranie

    def increase_invincible_frame(self):
        if self._is_damaged:
            self._invincible_frame += 1
            if self._invincible_frame == 50:
                self._is_damaged = False
                self._invincible_frame = 0

    def decrease_health_bar_frame(self):
        if self._health_bar_frame == 0:
            return

        self._health_bar_frame -= 1

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

    @property
    def hit_box(self) -> pygame.Rect:
        return self._hit_box

    @property
    def attack_damage(self) -> int:
        return self._damage

    @property
    def health(self) -> int:
        return self._health

    @health.setter
    def health(self, value: int):
        self._health = value

    @property
    def max_health(self):
        return self._max_health

