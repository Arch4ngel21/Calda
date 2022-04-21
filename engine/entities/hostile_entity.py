from enum import Enum
import pygame
from random import randint

from engine.entities.entity import Entity
from utilities.map_direction import MapDirection


class HostileEntityType(Enum):
    GHOST = 0
    SLIME = 0


class HostileEntity(Entity):
    BOX_SIZE: int = 32
    def __init__(self, x: int, y: int, health: int, damage: int, entity_type: HostileEntityType):
        super().__init__(x, y, health, damage)
        self._steps = 0
        self._attack_frame: int = 0
        self._is_attacking: bool = False
        self._entity_type: HostileEntityType = entity_type
        self._hit_box: pygame.Rect = pygame.Rect(x, y, self.BOX_SIZE, self.BOX_SIZE)
        self._bounding_box: pygame.Rect = pygame.Rect(x, y, self.BOX_SIZE, self.BOX_SIZE)
        self._facing: MapDirection = MapDirection.WEST

    def move(self):
        if self._steps % 3 == 0:
            if self._facing == MapDirection.NORTH:
                self._y -= 1
            if self._facing == MapDirection.WEST:
                self._x -= 1
            if self._facing == MapDirection.EAST:
                self._x += 1
            if self._facing == MapDirection.SOUTH:
                self._y += 1
            self._bounding_box.update(self._x, self._x, self.BOX_SIZE, self.BOX_SIZE)
            self._hit_box.update(self._x, self._x, self.BOX_SIZE, self.BOX_SIZE)

        self.increase_steps()
        if self._steps == 0:
            self._facing = self.new_direction()

        self.increase_steps()

    #TODO
    # zastanowić się czy te metody mają być publiczne
    def increase_animation_frame(self):
        self._animation_frame += 1
        if self._animation_frame >= 500:
            self._animation_frame = 0

    def increase_steps(self):
        self._steps += 1
        if self._steps >= 500:
            self._steps = 0

    def increase_attack_frame(self):
        pass

    def follow_player(self):
        # TODO
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

    @property
    def is_attacking(self) -> bool:
        return self._is_attacking

    @property
    def hostile_entity_type(self) -> HostileEntityType:
        return self._entity_type

