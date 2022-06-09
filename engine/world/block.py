from pygame import Rect
from utilities.settings import Settings
from random import randint
from utilities.resource_manager import ResourceManager


class Block:

    def __init__(self, x: int, y: int, block_name: str, is_passable: bool = False, animated: bool = False):
        starting_values = [x for x in range(175, -1, -25)]
        self._is_passable: bool = is_passable
        self._block_name: str = block_name
        self._animated = animated
        if self._animated:
            self._animation_frame = starting_values[randint(0, 7)]

    @property
    def is_passable(self):
        return self._is_passable

    @property
    def is_animated(self):
        return self._animated

    @property
    def block_name(self):
        return self._block_name

    def increase_animation_frame(self):
        self._animation_frame += 1
        if self._animation_frame == 200:
            self._animation_frame = 0

    def get_image_from_current_frame(self, world_map_x: int, world_map_y: int):
        if not self._animated:
            return None

        if self._block_name == "campfire":
            if (world_map_x == 1 and world_map_y == 2) or (world_map_x == 1 and world_map_y == 3):
                if self._animation_frame > 175:
                    return ResourceManager.campfire_dungeon_1
                elif self._animation_frame > 150:
                    return ResourceManager.campfire_dungeon_2
                elif self._animation_frame > 125:
                    return ResourceManager.campfire_dungeon_3
                elif self._animation_frame > 100:
                    return ResourceManager.campfire_dungeon_4
                elif self._animation_frame > 75:
                    return ResourceManager.campfire_dungeon_5
                elif self._animation_frame > 50:
                    return ResourceManager.campfire_dungeon_6
                elif self._animation_frame > 25:
                    return ResourceManager.campfire_dungeon_7
                else:
                    return ResourceManager.campfire_dungeon_8

            elif (world_map_x == 2 and world_map_y == 3) or (world_map_x == 3 and world_map_y == 3):
                if self._animation_frame > 175:
                    return ResourceManager.campfire_outside_1
                elif self._animation_frame > 150:
                    return ResourceManager.campfire_outside_2
                elif self._animation_frame > 125:
                    return ResourceManager.campfire_outside_3
                elif self._animation_frame > 100:
                    return ResourceManager.campfire_outside_4
                elif self._animation_frame > 75:
                    return ResourceManager.campfire_outside_5
                elif self._animation_frame > 50:
                    return ResourceManager.campfire_outside_6
                elif self._animation_frame > 25:
                    return ResourceManager.campfire_outside_7
                else:
                    return ResourceManager.campfire_outside_8
