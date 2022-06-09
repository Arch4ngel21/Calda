import pygame

from engine.entities.missiles.missile import Missile
from utilities.map_direction import MapDirection
from utilities.resource_manager import ResourceManager


class GhostFireball(Missile):
    def __init__(self, x: int, y: int, facing: MapDirection):
        super().__init__(x, y-4, 2, facing)
        self._lifespan: int = 10
        self._damage: int = 3
        self._bounding_box: pygame.Rect = pygame.Rect(x, y-4, self.BOX_SIZE, self.BOX_SIZE)
        self._image = ResourceManager.ghost_fireball_1

    def increase_animation_frame(self):
        self._animation_frame += 1
        if not self._animation_frame % 18:
            self._animation_frame = 0

    def update_image(self):
        if self._animation_frame > 12:
            self._image = ResourceManager.ghost_fireball_1
        elif self._animation_frame > 6:
            self._image = ResourceManager.ghost_fireball_2
        else:
            self._image = ResourceManager.ghost_fireball_3
        self._image = pygame.transform.scale(self._image, (8, 8))

