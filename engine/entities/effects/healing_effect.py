import pygame
from engine.entities.effects.screen_effect import ScreenEffect
from utilities.resource_manager import ResourceManager
from utilities.map_direction import MapDirection


class HealingEffect(ScreenEffect):
    def __init__(self, affected_entity, triggerable_entity=None):
        super().__init__(affected_entity.x, affected_entity.y, 50)
        self._image = ResourceManager.healing_effect_1
        self._away_frame = 0
        self._triggerable_entity = triggerable_entity
        self._affected_entity = affected_entity
        self._bounding_box = pygame.Rect(affected_entity.x, affected_entity.y, 32, 32)
        self._should_show = False

    def update_image(self):
        if self.animation_frame > 180:
            self._image = ResourceManager.healing_effect_1
        elif self.animation_frame > 160:
            self._image = ResourceManager.healing_effect_2
        elif self.animation_frame > 140:
            self._image = ResourceManager.healing_effect_3
        elif self.animation_frame > 120:
            self._image = ResourceManager.healing_effect_4
        elif self.animation_frame > 100:
            self._image = ResourceManager.healing_effect_5
        elif self.animation_frame > 80:
            self._image = ResourceManager.healing_effect_6
        elif self.animation_frame > 60:
            self._image = ResourceManager.healing_effect_7
        elif self.animation_frame > 40:
            self._image = ResourceManager.healing_effect_8
        elif self.animation_frame > 20:
            self._image = ResourceManager.healing_effect_9
        else:
            self._image = ResourceManager.healing_effect_10

        self.increase_animation_frame()
        self._image = pygame.transform.scale(self._image, (120, 75))
        self._image.set_alpha(128)

        if self._affected_entity.facing == MapDirection.EAST or self._affected_entity.facing == MapDirection.WEST:
            self._x = self._affected_entity.x - 40
            self._y = self._affected_entity.y - 35
        else:
            self._x = self._affected_entity.x - 55
            self._y = self._affected_entity.y - 35

        self._bounding_box.update(self._x, self._y, 32, 32)

    def increase_away_frame(self):
        if self._away_frame == self.effect_duration:
            return

        self._away_frame += 1

    def increase_animation_frame(self):
        if self._animation_frame > 200:
            self._animation_frame = 0

        self._animation_frame += 1

    def reset_away_frame(self):
        self._away_frame = 0

    @property
    def triggerable_entity(self):
        return self._triggerable_entity

    @property
    def away_frame(self):
        return self._away_frame

    @property
    def should_show(self):
        return self._should_show

    @should_show.setter
    def should_show(self, value: bool):
        self._should_show = value
