from pygame import Rect
from engine.game_engine import GameEngine


class Block:

    def __init__(self, x: int, y: int, block_name: str, is_passable: bool = False):
        self._is_passable: bool = is_passable
        self._block_name: str = block_name
        self._rectangle = Rect(x, y, GameEngine.BLOCK_SIZE, GameEngine.BLOCK_SIZE)

    @property
    def is_passable(self):
        return self._is_passable

    @property
    def block_name(self):
        return self._block_name
