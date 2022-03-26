from engine.collectibles.collectible import ItemType
from engine.entities.effects.screen_effect import ScreenEffect


class ChestOpenEffect(ScreenEffect):
    def __init__(self, x: int, y: int, item_type: ItemType):
        super().__init__(x, y, 200)
        self._item_type: ItemType = item_type

    def move(self):
        if self._y - 1 >= 0 and self._animation_frame % 4 == 0:
            self._y -= 1

    @property
    def item_type(self) -> ItemType:
        return self._item_type
