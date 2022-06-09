
from __future__ import annotations
from PIL import Image
import random
from typing import List, Optional
from enum import Enum

from engine.entities.effects.screen_effect import ScreenEffect
from engine.entities.hostile_entity import HostileEntity
from engine.entities.peaceful_entity import PeacefulEntity
from engine.entities.container import Container
from engine.world.block import Block
from utilities.exceptions import EmptyBlockException, WrongBlockOrientation


class LevelMap:
    # _level: List[List[Optional[Block]]]
    # _world_map_x: int
    # _world_map_y: int
    # _level_map_width: int
    # _level_map_height: int
    # _enemies_list: List[HostileEntity]
    # _friendly_entity_list: List[PeacefulEntity]
    # _chests: List[Container]

    def __init__(self, world_map_x: int, world_map_y: int, image: Image.Image):
        self._world_map_x = world_map_x
        self._world_map_y = world_map_y
        self._level_map_width = image.size[0]
        self._level_map_height = image.size[1]
        self._level = [[None for _ in range(self._level_map_width)] for _ in range(self._level_map_height)]
        self._enemies_list = []
        self._friendly_entity_list = []
        self._chests = []
        self._effects = []

        for y in range(self._level_map_height):
            for x in range(self._level_map_width):
                r, g, b, alpha = image.getpixel((x, y))

                if (26, 213, 0) == (r, g, b):

                    rand = random.randint(0, 7)
                    if rand == 0:
                        self._level[y][x] = Block(x, y, "grass4", True)
                    elif rand == 1:
                        self._level[y][x] = Block(x, y, "grass1", True)
                    elif rand in [2, 3, 4, 5, 6]:
                        self._level[y][x] = Block(x, y, "grass2", True)
                    else:
                        self._level[y][x] = Block(x, y, "grass3", True)

                elif (18, 146, 0) == (r, g, b):
                    self._level[y][x] = Block(x, y, "bush", False)

                elif (146, 146, 146) == (r, g, b):
                    rand = random.randint(0, 4)
                    if rand == 0:
                        self._level[y][x] = Block(x, y, "bricks1", True)
                    elif rand == 1:
                        self._level[y][x] = Block(x, y, "bricks2", True)
                    elif rand == 2:
                        self._level[y][x] = Block(x, y, "bricks3", True)
                    else:
                        self._level[y][x] = Block(x, y, "bricks4", True)

                elif (85, 85, 85) == (r, g, b):

                    if (self._world_map_x == 4 and self._world_map_y == 1) or (self._world_map_x == 4 and self._world_map_y == 3) \
                            or (self._world_map_x == 2 and self._world_map_y == 3):
                        self._level[y][x] = Block(x, y, "cobblestone", False)
                    else:
                        self._level[y][x] = Block(x, y, "cobblestone", True)

                elif (0, 83, 197) == (r, g, b):
                    self._level[y][x] = Block(x, y, "water", False)

                elif (103, 43, 138) == (r, g, b):
                    rand = random.randint(0, 4)
                    if rand == 0:
                        self._level[y][x] = Block(x, y, "dungeon_bricks1", False)
                    elif rand == 1:
                        self._level[y][x] = Block(x, y, "dungeon_bricks2", False)
                    elif rand == 2:
                        self._level[y][x] = Block(x, y, "dungeon_bricks3", False)
                    else:
                        self._level[y][x] = Block(x, y, "dungeon_bricks4", False)

                elif (181, 85, 255) == (r, g, b):
                    rand = random.randint(0, 16)
                    if rand == 0:
                        self._level[y][x] = Block(x, y, "dungeon_floor4", True)
                    elif rand in [1, 2, 3]:
                        self._level[y][x] = Block(x, y, "dungeon_floor2", True)
                    elif rand in [4, 5, 6]:
                        self._level[y][x] = Block(x, y, "dungeon_floor3", True)
                    elif rand in [7, 8, 9, 10]:
                        self._level[y][x] = Block(x, y, "dungeon_floor5", True)
                    else:
                        self._level[y][x] = Block(x, y, "dungeon_floor1", True)

                elif (150, 106, 0) == (r, g, b):

                    orientation = self.find_orientation(image, self, r, g, b, x, y)

                    if orientation == LevelMap.BlockOrientation.CENTER:
                        self._level[y][x] = Block(x, y, "path_center", True)
                    elif orientation == LevelMap.BlockOrientation.STRAIGHT_UP:
                        self._level[y][x] = Block(x, y, "path_straight_up", True)
                    elif orientation == LevelMap.BlockOrientation.STRAIGHT_DOWN:
                        self._level[y][x] = Block(x, y, "path_straight_down", True)
                    elif orientation == LevelMap.BlockOrientation.STRAIGHT_LEFT:
                        self._level[y][x] = Block(x, y, "path_straight_left", True)
                    elif orientation == LevelMap.BlockOrientation.STRAIGHT_RIGHT:
                        self._level[y][x] = Block(x, y, "path_straight_right", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_LEFT_DOWN:
                        self._level[y][x] = Block(x, y, "path_corner_left_down", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_LEFT_UP:
                        self._level[y][x] = Block(x, y, "path_corner_left_up", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_RIGHT_UP:
                        self._level[y][x] = Block(x, y, "path_corner_right_up", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_RIGHT_DOWN:
                        self._level[y][x] = Block(x, y, "path_corner_right_down", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_LEFT_DOWN:
                        self._level[y][x] = Block(x, y, "path_corner_left_down", True)
                    elif orientation == LevelMap.BlockOrientation.TURN_LEFT_UP:
                        self._level[y][x] = Block(x, y, "path_turn_left_up", True)
                    elif orientation == LevelMap.BlockOrientation.TURN_LEFT_DOWN:
                        self._level[y][x] = Block(x, y, "path_turn_left_down", True)
                    elif orientation == LevelMap.BlockOrientation.TURN_RIGHT_DOWN:
                        self._level[y][x] = Block(x, y, "path_turn_right_down", True)
                    elif orientation == LevelMap.BlockOrientation.TURN_RIGHT_UP:
                        self._level[y][x] = Block(x, y, "path_turn_right_up", True)
                    else:
                        print(f"Zle obliczona orientacja dla bloku ({x, y})")
                        raise WrongBlockOrientation

                elif (195, 193, 0) == (r, g, b):

                    orientation = self.find_orientation(image, self, r, g, b, x, y)

                    if orientation == LevelMap.BlockOrientation.CENTER:
                        self._level[y][x] = Block(x, y, "shore_center", True)
                    elif orientation == LevelMap.BlockOrientation.STRAIGHT_UP:
                        self._level[y][x] = Block(x, y, "shore_straight_up", True)
                    elif orientation == LevelMap.BlockOrientation.STRAIGHT_DOWN:
                        self._level[y][x] = Block(x, y, "shore_straight_down", True)
                    elif orientation == LevelMap.BlockOrientation.STRAIGHT_LEFT:
                        self._level[y][x] = Block(x, y, "shore_straight_left", True)
                    elif orientation == LevelMap.BlockOrientation.STRAIGHT_RIGHT:
                        self._level[y][x] = Block(x, y, "shore_straight_right", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_LEFT_DOWN:
                        self._level[y][x] = Block(x, y, "shore_corner_left_down", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_LEFT_UP:
                        self._level[y][x] = Block(x, y, "shore_corner_left_up", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_RIGHT_UP:
                        self._level[y][x] = Block(x, y, "shore_corner_right_up", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_RIGHT_DOWN:
                        self._level[y][x] = Block(x, y, "shore_corner_right_down", True)
                    elif orientation == LevelMap.BlockOrientation.CORNER_LEFT_DOWN:
                        self._level[y][x] = Block(x, y, "shore_corner_left_down", True)
                    elif orientation == LevelMap.BlockOrientation.TURN_LEFT_UP:
                        self._level[y][x] = Block(x, y, "shore_turn_left_up", True)
                    elif orientation == LevelMap.BlockOrientation.TURN_LEFT_DOWN:
                        self._level[y][x] = Block(x, y, "shore_turn_left_down", True)
                    elif orientation == LevelMap.BlockOrientation.TURN_RIGHT_DOWN:
                        self._level[y][x] = Block(x, y, "shore_turn_right_down", True)
                    elif orientation == LevelMap.BlockOrientation.TURN_RIGHT_UP:
                        self._level[y][x] = Block(x, y, "shore_turn_right_up", True)
                    else:
                        print(f"Zle obliczona orientacja dla bloku ({x, y})")
                        raise WrongBlockOrientation

                elif (224, 42, 0) == (r, g, b):
                    self._level[y][x] = Block(x, y, "campfire", False, True)

                elif (116, 87, 0) == (r, g, b):
                    self._level[y][x] = Block(x, y, "tree_bottom", False)

                elif (8, 64, 0) == (r, g, b):
                    self._level[y][x] = Block(x, y, "tree_up", False)

                elif (255, 198, 0) == (r, g, b):
                    self._level[y][x] = Block(x, y, "sign", False)

                elif (0, 0, 0) == (r, g, b):
                    self._level[y][x] = Block(x, y, "grass1", True)

                elif (0, 252, 255) == (r, g, b):
                    if image.getpixel((x+1, y))[:-1] == (0, 252, 255):
                        self._level[y][x] = Block(x, y, "dungeon_entrance_left", False)
                    else:
                        self._level[y][x] = Block(x, y, "dungeon_entrance_right", False)
                else:
                    self._level[y][x] = Block(x, y, "error_block", False)

    @property
    def world_map_x(self) -> int:
        return self._world_map_x

    @property
    def world_map_y(self) -> int:
        return self._world_map_y

    def get_block(self, x: int, y: int) -> Optional[Block]:
        if not self._level[y][x]:
            print(f"Empty block on level: {self._world_map_x, self._world_map_y}, at {x, y}")
            raise EmptyBlockException

        return self._level[y][x]

    @property
    def level_map_width(self) -> int:
        return self._level_map_width

    @property
    def level_map_height(self) -> int:
        return self._level_map_height

    @property
    def enemies_list(self):
        return self._enemies_list

    @property
    def friendly_entity_list(self):
        return self._friendly_entity_list

    @property
    def chests(self):
        return self._chests

    @property
    def effects(self):
        return self._effects

    def add_hostile_entity(self, entity: HostileEntity):
        self._enemies_list.append(entity)

    def add_peaceful_entity(self, entity: PeacefulEntity):
        self._friendly_entity_list.append(entity)

    def add_chest(self, container: Container):
        self._chests.append(container)

    def add_effect(self, effect: ScreenEffect):
        self._effects.append(effect)

    class BlockOrientation(Enum):
        CENTER = 0
        STRAIGHT_UP = 1
        STRAIGHT_DOWN = 2
        STRAIGHT_RIGHT = 3
        STRAIGHT_LEFT = 4
        CORNER_LEFT_DOWN = 5
        CORNER_LEFT_UP = 6
        CORNER_RIGHT_DOWN = 7
        CORNER_RIGHT_UP = 8
        TURN_LEFT_DOWN = 9
        TURN_LEFT_UP = 10
        TURN_RIGHT_DOWN = 11
        TURN_RIGHT_UP = 12

    @staticmethod
    def find_orientation(image: Image.Image, level_map: LevelMap, r: int, g: int, b: int, x: int, y: int) -> BlockOrientation:
        check_square = [[False for _ in range(3)] for _ in range(3)]

        if (150, 106, 0) == (r, g, b):
            # grass_rgb_value = (26, 213, 0)
            # bush_rgb_value = (18, 146, 0)
            # shore_rgb_value = (195, 193, 0)
            accepted_values = [(26, 213, 0), (18, 146, 0), (195, 193, 0)]

            # Zbudowanie tablicy z boolami, gdzie True wskazuje na miejsce, gdzie nie ma bloku ścieżki
            if x-1 >= 0 and image.getpixel((x-1, y))[:-1] in accepted_values:
                check_square[0][1] = True
            if x-1 >= 0 and y-1 >= 0 and image.getpixel((x-1, y-1))[:-1] in accepted_values:
                check_square[0][2] = True
            if y-1 >= 0 and image.getpixel((x, y-1))[:-1] in accepted_values:
                check_square[1][2] = True
            if x+1 < level_map.level_map_width and y-1 >= 0 and image.getpixel((x+1, y-1))[:-1] in accepted_values:
                check_square[2][2] = True
            if x+1 < level_map.level_map_width and image.getpixel((x+1, y))[:-1] in accepted_values:
                check_square[2][1] = True
            if x+1 < level_map.level_map_width and y+1 < level_map.level_map_height and image.getpixel((x+1, y+1))[:-1] in accepted_values:
                check_square[2][0] = True
            if y+1 < level_map.level_map_height and image.getpixel((x, y+1))[:-1] in accepted_values:
                check_square[1][0] = True
            if x-1 >= 0 and y+1 < level_map.level_map_height and image.getpixel((x-1, y+1))[:-1] in accepted_values:
                check_square[0][0] = True

            # if level_map._world_map_x == 2 and level_map._world_map_y == 0:
            #     print(f"Block: {x, y}")
            #     for lane in check_square:
            #         print(lane)

            if check_square[0][1] and check_square[0][2] and check_square[1][2]:
                return LevelMap.BlockOrientation.CORNER_RIGHT_DOWN

            if check_square[1][2] and check_square[2][2] and check_square[2][1]:
                return LevelMap.BlockOrientation.CORNER_LEFT_DOWN

            if check_square[2][1] and check_square[2][0] and check_square[1][0]:
                return LevelMap.BlockOrientation.CORNER_LEFT_UP

            if check_square[1][0] and check_square[0][0] and check_square[0][1]:
                return LevelMap.BlockOrientation.CORNER_RIGHT_UP

            if (check_square[0][0] and check_square[0][1]) or (check_square[0][1] and check_square[0][2]):
                return LevelMap.BlockOrientation.STRAIGHT_RIGHT

            if (check_square[0][2] and check_square[1][2]) or (check_square[1][2] and check_square[2][2]):
                return LevelMap.BlockOrientation.STRAIGHT_DOWN

            if (check_square[2][0] and check_square[2][1]) or (check_square[2][1] and check_square[2][2]):
                return LevelMap.BlockOrientation.STRAIGHT_LEFT

            if (check_square[0][0] and check_square[1][0]) or (check_square[1][0] and check_square[2][0]):
                return LevelMap.BlockOrientation.STRAIGHT_UP

            if check_square[0][0]:
                return LevelMap.BlockOrientation.TURN_RIGHT_UP

            if check_square[2][0]:
                return LevelMap.BlockOrientation.TURN_LEFT_UP

            if check_square[2][2]:
                return LevelMap.BlockOrientation.TURN_LEFT_DOWN

            if check_square[0][2]:
                return LevelMap.BlockOrientation.TURN_RIGHT_DOWN

            else:
                return LevelMap.BlockOrientation.CENTER

        elif (195, 193, 0) == (r, g, b):
            water_rgb_value = (0, 83, 197)

            if x-1 >= 0 and image.getpixel((x-1, y))[:-1] == water_rgb_value:
                check_square[0][1] = True
            if x-1 >= 0 and y-1 >= 0 and image.getpixel((x-1, y-1))[:-1] == water_rgb_value:
                check_square[0][2] = True
            if y-1 >= 0 and image.getpixel((x, y-1))[:-1] == water_rgb_value:
                check_square[1][2] = True
            if x+1 < level_map.level_map_width and y-1 >= 0 and image.getpixel((x+1, y-1))[:-1] == water_rgb_value:
                check_square[2][2] = True
            if x+1 < level_map.level_map_width and image.getpixel((x+1, y))[:-1] == water_rgb_value:
                check_square[2][1] = True
            if x+1 < level_map.level_map_width and y+1 < level_map.level_map_height and image.getpixel((x+1, y+1))[:-1] == water_rgb_value:
                check_square[2][0] = True
            if y+1 < level_map.level_map_height and image.getpixel((x, y+1))[:-1] == water_rgb_value:
                check_square[1][0] = True
            if x-1 >= 0 and y+1 < level_map.level_map_height and image.getpixel((x-1, y+1))[:-1] == water_rgb_value:
                check_square[0][0] = True

            if check_square[1][2] and check_square[2][2] and check_square[2][1]:
                return LevelMap.BlockOrientation.TURN_LEFT_DOWN

            if check_square[2][1] and check_square[2][0] and check_square[1][0]:
                return LevelMap.BlockOrientation.TURN_RIGHT_DOWN

            if check_square[1][0] and check_square[0][0] and check_square[0][1]:
                return LevelMap.BlockOrientation.TURN_RIGHT_UP

            if check_square[0][1] and check_square[0][2] and check_square[1][2]:
                return LevelMap.BlockOrientation.TURN_LEFT_UP

            if not check_square[2][1] and not check_square[1][2] and check_square[2][2]:
                return LevelMap.BlockOrientation.CORNER_LEFT_DOWN

            if not check_square[2][1] and not check_square[1][0] and check_square[2][0]:
                return LevelMap.BlockOrientation.CORNER_RIGHT_DOWN

            if not check_square[0][1] and not check_square[1][0] and check_square[0][0]:
                return LevelMap.BlockOrientation.CORNER_RIGHT_UP

            if not check_square[0][1] and not check_square[1][2] and check_square[0][2]:
                return LevelMap.BlockOrientation.CORNER_LEFT_UP

            if check_square[2][1]:
                return LevelMap.BlockOrientation.STRAIGHT_LEFT

            if check_square[1][0]:
                return LevelMap.BlockOrientation.STRAIGHT_DOWN

            if check_square[0][1]:
                return LevelMap.BlockOrientation.STRAIGHT_RIGHT

            if check_square[1][2]:
                return LevelMap.BlockOrientation.STRAIGHT_UP

            else:
                return LevelMap.BlockOrientation.CENTER

        return LevelMap.BlockOrientation.CENTER


