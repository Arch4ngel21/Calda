from enum import Enum
import pygame
from random import randint

from engine.entities.entity import Entity
from utilities.map_direction import MapDirection


class HostileEntityType(Enum):
    GHOST = 0
    SLIME = 0


class HostileEntity(Entity):
    def __init__(self, x: int, y: int, health: int, damage: int, entity_type: HostileEntityType):
        super().__init__(x, y, health, damage)
        self._steps = 0
        self._attack_frame: int = 0
        self._is_attacking: bool = False
        self._entity_type: HostileEntityType = entity_type
        self._hit_box: pygame.Rect = pygame.Rect(x, y, 32, 32)
        self._bounding_box: pygame.Rect = pygame.Rect(x, y, 32, 32)
        self._facing: MapDirection = MapDirection.WEST

    def move(self):
        pass

    def increase_animation_frame(self):
        self._animation_frame += 1
        if self._animation_frame >= 500:
            self._animation_frame = 0

    def increase_steps(self):
        self._steps += 1
        if self._steps >= 500:
            self._steps = 0

    def decrease_attack_frame(self):
        pass #po co to

    def follow_player(self):
        pass

    @staticmethod
    def new_direction() -> MapDirection:
        rand = randint(1, 4)
        if rand == 1:
            return MapDirection.NORTH
        if rand == 2:
            return MapDirection.EAST
        if rand == 3:
            return MapDirection.SOUTH
        return MapDirection.WEST


