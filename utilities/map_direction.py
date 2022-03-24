from __future__ import annotations

from enum import Enum


class MapDirection(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

    @staticmethod
    def opposite(direction: MapDirection) -> MapDirection:
        if direction == MapDirection.NORTH:
            return MapDirection.SOUTH
        if direction == MapDirection.SOUTH:
            return MapDirection.NORTH
        if direction == MapDirection.WEST:
            return MapDirection.EAST
        if direction == MapDirection.EAST:
            return MapDirection.WEST

