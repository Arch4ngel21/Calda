from enum import Enum
import pygame

from engine.entities.entity import Entity


class PeacefulEntityType(Enum):
    SIGN = 1
    DUNGEON_ENTRANCE = 2
    TREE_OF_HEALTH = 3


class PeacefulEntity(Entity):
    def __init__(self, x: int, y: int, health: int, damage: int, peaceful_entity_type: PeacefulEntityType):
        super().__init__(x, y, health, damage)
        self._passive_effect_frame: int = 0
        self._peaceful_entity_type = peaceful_entity_type
        self._bounding_box = pygame.Rect(x, y, 32, 32)

    def increase_animation_frame(self):
        self._animation_frame += 1
        if self._animation_frame >= 40:
            self._animation_frame = 0

    def increase_passive_effect_frame(self):
        self._passive_effect_frame += 1
        if self._passive_effect_frame >= 200:
            self._passive_effect_frame = 0

    @property
    def peaceful_entity_type(self) -> PeacefulEntityType:
        return self._peaceful_entity_type

    @property
    def passive_effect_frame(self) -> int:
        return self._passive_effect_frame
