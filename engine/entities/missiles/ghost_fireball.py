import pygame

from engine.entities.missiles.missile import Missile
from utilities.map_direction import MapDirection


class GhostFireball(Missile):
    def __init__(self, x: int, y: int, facing: MapDirection):
        super().__init__(x, y, 2, facing)
        self._lifespan: int = 10
        self._damage: int = 3
        self._bound_box: pygame.Rect = pygame.Rect(x, y, self.BOX_SIZE, self.BOX_SIZE)

    def increase_animation_frame(self):
        self._animation_frame += 1
        if not self._animation_frame % 18:
            self._animation_frame = 0
