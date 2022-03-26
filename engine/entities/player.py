import pygame
from utilities.map_direction import MapDirection
from engine.entities.entity import Entity


class Player(Entity):

    def __init__(self, x: int, y: int, health: int, damage: int):
        super().__init__(x, y, health, damage)
        self._coins: int = 0
        self._has_sword: bool = False
        self._facing: MapDirection = MapDirection.WEST
        self._hit_box: pygame.Rect = pygame.Rect(x, y, 32, 32)
        self._attack_frame = 0

    def move(self):
        # TODO
        pass

    def add_health(self):
        self.heal(2)

    def add_max_health(self):
        self.increase_max_health(2)
        self.add_health()

    def add_coin(self):
        self._coins += 1

    @property
    def has_sword(self) -> bool:
        return self._has_sword

    @has_sword.setter
    def has_sword(self, value: bool):
        if not isinstance(value, bool):
            raise ValueError("has_sword must be a bool")
        self._has_sword = value

    @property
    def attack_frame(self) -> int:
        return self._attack_frame

    @attack_frame.setter
    def attack_frame(self, value: int):
        if value not in range(0, 31):
            raise ValueError("Wrong attack frame")
        self._attack_frame = value
