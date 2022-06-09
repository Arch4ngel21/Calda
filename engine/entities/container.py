from enum import Enum
from typing import List

import pygame

from engine.entities.entity import Entity
from engine.collectibles.collectible import Collectible, ItemType
from utilities.resource_manager import ResourceManager


class ContainerType(Enum):
    CHEST = 1
    STONE_SWORD = 2


class Container(Entity):
    def __init__(self, x: int, y: int, container_type: ContainerType):
        super().__init__(x, y, 0, 0)
        self._inventory: List[ItemType] = []
        self._container_type: ContainerType = container_type
        self._capacity: int = 5
        self._is_opened: bool = False
        self._bounding_box = pygame.Rect(x, y, 32, 32)

        if self._container_type == ContainerType.CHEST:
            self._image = ResourceManager.chest_closed
        elif self._container_type == ContainerType.STONE_SWORD:
            self._image = ResourceManager.stone_with_sword

    def include_item(self, item: ItemType):
        if len(self._inventory) >= self._capacity:
            return
        if not isinstance(item, ItemType):
            raise ValueError("item must be an ItemType")
        self._inventory.append(item)

    def increase_animation_frame(self):
        self._animation_frame += 1
        if self._animation_frame >= 40:
            self._animation_frame = 0

    def update_image(self):
        if self._is_opened:
            if self._container_type == ContainerType.CHEST:
                self._image = ResourceManager.chest_opened
            elif self._container_type == ContainerType.STONE_SWORD:
                self._image = ResourceManager.stone_without_sword

    def draw(self, screen: pygame.Surface):
        screen.blit(self._image, self._bounding_box)

    @property
    def is_opened(self):
        return self._is_opened

    @is_opened.setter
    def is_opened(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("is_opened must be boolean")
        self._is_opened = value

    @property
    def inventory(self) -> List[ItemType]:
        return self._inventory

    @property
    def container_type(self) -> ContainerType:
        return self._container_type
