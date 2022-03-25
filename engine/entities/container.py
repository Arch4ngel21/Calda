from enum import Enum
from typing import List

import pygame

from engine.entities.entity import Entity
from engine.collectibles.collectible import Collectible


class ContainerType(Enum):
    CHEST = 1
    STONE_SWORD = 2


class Container(Entity):
    def __init__(self, x: int, y: int, container_type: ContainerType):
        super().__init__(x, y, 0, 0)
        self._inventory: List[Collectible] = []
        self._container_type: ContainerType = container_type
        self._capacity: int = 5
        self._is_opened: bool = False
        self._bounding_box = pygame.Rect(x, y, 32, 32)

    def include_item(self, item: Collectible):
        if len(self._inventory) >= self._capacity:
            return
        self._inventory.append(item)

    def increase_animation_frame(self):
        self._animation_frame += 1
        if self._animation_frame >= 40:
            self._animation_frame = 0
