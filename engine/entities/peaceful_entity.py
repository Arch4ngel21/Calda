from enum import Enum
import pygame

from engine.entities.entity import Entity
from utilities.resource_manager import ResourceManager


class PeacefulEntityType(Enum):
    SIGN = 1
    DUNGEON_ENTRANCE = 2
    TREE_OF_HEALTH = 3
    PORTAL = 4


class PeacefulEntity(Entity):
    def __init__(self, x: int, y: int, health: int, damage: int, peaceful_entity_type: PeacefulEntityType):
        super().__init__(x, y, health, damage)
        self._passive_effect_frame: int = 0
        self._peaceful_entity_type = peaceful_entity_type
        self._bounding_box = pygame.Rect(x, y, 64, 64)

        if self._peaceful_entity_type == PeacefulEntityType.PORTAL:
            self._image = ResourceManager.portal_1

    def draw(self, screen: pygame.Surface):
        self.update_image()
        screen.blit(self._image, self._bounding_box)

    def update_image(self):

        if self._peaceful_entity_type == PeacefulEntityType.PORTAL:
            if self._animation_frame > 175:
                self._image = ResourceManager.portal_8
            elif self._animation_frame > 150:
                self._image = ResourceManager.portal_7
            elif self._animation_frame > 125:
                self._image = ResourceManager.portal_6
            elif self._animation_frame > 100:
                self._image = ResourceManager.portal_5
            elif self._animation_frame > 75:
                self._image = ResourceManager.portal_4
            elif self._animation_frame > 50:
                self._image = ResourceManager.portal_3
            elif self._animation_frame > 25:
                self._image = ResourceManager.portal_2
            else:
                self._image = ResourceManager.portal_1

            self._image = pygame.transform.flip(self._image, True, False)
            self._image = pygame.transform.scale(self._image, (128, 128))
            self.increase_animation_frame()

    def increase_animation_frame(self):
        self._animation_frame += 1
        if self._peaceful_entity_type == PeacefulEntityType.PORTAL and self._animation_frame > 200:
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
