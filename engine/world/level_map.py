
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
                px = image.getpixel((x, y))




