from engine.world.level_map import LevelMap
from utilities.exceptions import EmptyLevelMapException


class Map:

    def __init__(self, map_width: int, map_height: int):
        self._map_width = map_width
        self._map_height = map_height
        self._world_map = [[None for _ in range(self._map_height)] for _ in range(self._map_width)]

    def add_level(self, level_map: LevelMap):
        self._world_map[level_map.get_world_map_x()][level_map.get_world_map_y()] = level_map

    def get_level(self, x: int, y: int) -> LevelMap:
        if self._world_map[x][y] is None:
            raise EmptyLevelMapException

        return self._world_map[x][y]

