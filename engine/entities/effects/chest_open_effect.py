from engine.collectibles.collectible import ItemType
from engine.entities.effects.screen_effect import ScreenEffect
from utilities.resource_manager import ResourceManager
from utilities.settings import Settings
import pygame


class ChestOpenEffect(ScreenEffect):
    def __init__(self, x: int, y: int, item_type: ItemType):
        super().__init__(x, y, 150)
        self._item_type: ItemType = item_type
        self._bounding_box = pygame.Rect(x, y, 48, 32)
        self._image: pygame.image

        if item_type == ItemType.COIN:
            self._image = ResourceManager.plus_coin
        elif item_type == ItemType.HEALTH:
            self._image = ResourceManager.plus_heart

    def move(self):
        if self._y - 1 >= 0 and self._animation_frame % 4 == 0:
            self._y -= 1
            self._bounding_box.update(self._x, self._y, 48, 32)

    def update_image(self):
        alpha = ((150 - self._animation_frame) / 150) * 255
        self._image = self._image.copy()
        self._image.set_alpha(alpha)

    @property
    def item_type(self) -> ItemType:
        return self._item_type
