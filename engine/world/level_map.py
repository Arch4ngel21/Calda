
from engine.entities.hostile_entity import HostileEntity
from engine.entities.peaceful_entity import PeacefulEntity
from engine.entities.container import Container
from engine.world.block import Block
from typing import List, Optional
from PIL import Image
import random


class LevelMap:
    level: List[List[Optional[Block]]]
    world_map_x: int
    world_map_y: int
    level_map_width: int
    level_map_height: int

    enemies_list: List[HostileEntity]
    friendly_entity_list: List[PeacefulEntity]
    chests: List[Container]

    def __init__(self, world_map_x: int, world_map_y: int, image: Image.Image):
        self.world_map_x = world_map_x
        self.world_map_y = world_map_y
        self.level_map_width = image.size[0]
        self.leve_map_height = image.size[1]
        level = [[None for _ in range(self.level_map_width)] for _ in range(self.level_map_height)]

        for y in range(self.level_map_height):
            for x in range(self.level_map_width):
                r, g, b = image.getpixel((x, y))

                if (26, 213, 0) == (r, g, b):

                    rand = random.randint(0, 7)
                    if rand == 0:
                        level[y][x] = Block(x, y, "grass4", True)
                    elif rand == 1:
                        level[y][x] = Block(x, y, "grass1", True)
                    elif rand in [2, 3, 4, 5, 6]:
                        level[y][x] = Block(x, y, "grass2", True)
                    else:
                        level[y][x] = Block(x, y, "grass3", True)

                elif (18, 146, 0) == (r, g, b):
                    level[y][x] = Block(x, y, "bush", False)

                elif (146, 146, 146) == (r, g, b):
                    rand = random.randint(0, 4)
                    if rand == 0:
                        level[y][x] = Block(x, y, "bricks1", True)
                    elif rand == 1:
                        level[y][x] = Block(x, y, "bricks2", True)
                    elif rand == 2:
                        level[y][x] = Block(x, y, "bricks3", True)
                    elif rand == 3:
                        level[y][x] = Block(x, y, "bricks4", True)

                elif (85, 85, 85) == (r, g, b):

                    if (self.world_map_x == 4 and self.world_map_y == 1) or (self.world_map_x == 4 and self.world_map_y == 3) \
                            or (self.world_map_x == 2 and self.world_map_y == 3):
                        level[y][x] = Block(x, y, "cobblestone", False)
                    else:
                        level[y][x] = Block(x, y, "cobblestone", True)

                elif (0, 83, 197) == (r, g, b):
                    level[y][x] = Block(x, y, "water", False)

                elif (103, 43, 138) == (r, g, b):
                    rand = random.randint(0, 4)
                    if rand == 0:
                        level[y][x] = Block(x, y, "dungeon_bricks1", False)
                    elif rand == 1:
                        level[y][x] = Block(x, y, "dungeon_bricks2", False)
                    elif rand == 2:
                        level[y][x] = Block(x, y, "dungeon_bricks3", False)
                    elif rand == 3:
                        level[y][x] = Block(x, y, "dungeon_bricks4", False)

                elif (150, 106, 0) == (r, g, b):
                    # TODO -> obracanie ścieżki
                    pass

                elif (195, 193, 0) == (r, g, b):
                    # TODO -> obracanie brzegu
                    pass

                elif (224, 42, 0) == (r, g, b):
                    level[y][x] = Block(x, y, "campfire", False)

                elif (116, 87, 0) == (r, g, b):
                    level[y][x] = Block(x, y, "tree_bottom", False)

                elif (8, 64, 0) == (r, g, b):
                    level[y][x] = Block(x, y, "tree_up", False)

                elif (0, 252, 255) == (r, g, b):
                    if image.getpixel((x+1, y)) == (0, 252, 255):
                        level[y][x] = Block(x, y, "dungeon_entrance_left", False)
                    else:
                        level[y][x] = Block(x, y, "dungeon_entrance_right", False)



                else:
                    level[y][x] = Block(x, y, "error_block", False)


