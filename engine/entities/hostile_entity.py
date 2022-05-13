from enum import Enum
import pygame
from random import randint
import math

from engine.entities.entity import Entity
from engine.entities.player import Player
from utilities.map_direction import MapDirection
from utilities.resource_manager import ResourceManager


class HostileEntityType(Enum):
    GHOST = 0
    SLIME = 1


class HostileEntity(Entity):
    BOX_SIZE: int = 32

    def __init__(self, x: int, y: int, health: int, damage: int, entity_type: HostileEntityType):
        super().__init__(x, y, health, damage)
        self._steps = 0
        self._attack_frame: int = 0
        self._is_attacking: bool = False
        self._is_following_player: bool = False
        self._entity_type: HostileEntityType = entity_type
        self._hit_box: pygame.Rect = pygame.Rect(x, y, self.BOX_SIZE, self.BOX_SIZE)
        self._bounding_box: pygame.Rect = pygame.Rect(x, y, self.BOX_SIZE, self.BOX_SIZE)
        self._facing: MapDirection = MapDirection.WEST

        if self._entity_type == HostileEntityType.GHOST:
            self._image = ResourceManager.ghost_moving_1
        else:
            self._image = ResourceManager.slime_standing_1

    def move(self):
        if self._steps % 3 == 0:
            if self._facing == MapDirection.NORTH:
                self._y -= 1
            elif self._facing == MapDirection.WEST:
                self._x -= 1
            elif self._facing == MapDirection.EAST:
                self._x += 1
            elif self._facing == MapDirection.SOUTH:
                self._y += 1
            self._bounding_box.update(self._x, self._x, self.BOX_SIZE, self.BOX_SIZE)
            self._hit_box.update(self._x, self._x, self.BOX_SIZE, self.BOX_SIZE)

        self.increase_steps()
        if self._steps == 0:
            self._facing = self.new_direction()

        self.increase_steps()
        self.update_image()

    def update_image(self):
        if self.hostile_entity_type == HostileEntityType.GHOST:
            if self._attack_frame == 0:
                if self._animation_frame > 438:
                    self._image = ResourceManager.ghost_moving_1
                elif self._animation_frame > 375:
                    self._image = ResourceManager.ghost_moving_2
                elif self._animation_frame > 313:
                    self._image = ResourceManager.ghost_moving_3
                elif self._animation_frame > 250:
                    self._image = ResourceManager.ghost_moving_4
                elif self._animation_frame > 188:
                    self._image = ResourceManager.ghost_moving_5
                elif self._animation_frame > 125:
                    self._image = ResourceManager.ghost_moving_6
                elif self._animation_frame > 62:
                    self._image = ResourceManager.ghost_moving_7
                else:
                    self._image = ResourceManager.ghost_moving_8

            else:
                if self._attack_frame > 40:
                    self._image = ResourceManager.ghost_attack_1
                elif self._attack_frame > 30:
                    self._image = ResourceManager.ghost_attack_2
                elif self._attack_frame > 20:
                    self._image = ResourceManager.ghost_attack_3
                elif self._attack_frame > 10:
                    self._image = ResourceManager.ghost_attack_4
                else:
                    self._image = ResourceManager.ghost_attack_5

        elif self.hostile_entity_type == HostileEntityType.SLIME:
            if self._attack_frame == 0:
                if self._animation_frame > 429:
                    self._image = ResourceManager.slime_standing_1
                elif self._animation_frame > 358:
                    self._image = ResourceManager.slime_standing_2
                elif self._animation_frame > 287:
                    self._image = ResourceManager.slime_standing_3
                elif self._animation_frame > 216:
                    self._image = ResourceManager.slime_standing_4
                elif self._animation_frame > 145:
                    self._image = ResourceManager.slime_standing_5
                elif self._animation_frame > 73:
                    self._image = ResourceManager.slime_standing_6
                else:
                    self._image = ResourceManager.slime_standing_7

            # TODO - Offset!
            else:
                if self._attack_frame > 35:
                    self._image = ResourceManager.slime_jumping_1
                elif self._attack_frame > 30:
                    self._image = ResourceManager.slime_jumping_2
                elif self._attack_frame > 25:
                    self._image = ResourceManager.slime_jumping_3
                elif self._attack_frame > 20:
                    self._image = ResourceManager.slime_jumping_4
                elif self._attack_frame > 15:
                    self._image = ResourceManager.slime_jumping_5
                elif self._attack_frame > 10:
                    self._image = ResourceManager.slime_jumping_6
                else:
                    self._image = ResourceManager.slime_jumping_7

    def increase_animation_frame(self):
        self._animation_frame += 1
        if self._animation_frame >= 500:
            self._animation_frame = 0

    def increase_steps(self):
        self._steps += 1
        if self._steps >= 500:
            self._steps = 0

    def decrease_attack_frame(self):
        if self._attack_frame == 0:
            self._is_attacking = False
        else:
            self._attack_frame -= 1

    def set_attack_frame(self, value: int):
        self._is_attacking = True
        self._attack_frame = value

    def follow_player(self, player: Player):
        distance_to_follow: int
        if self._entity_type == HostileEntityType.SLIME:
            distance_to_follow = 256
        elif self._entity_type == HostileEntityType.GHOST:
            distance_to_follow = 320
        else:
            distance_to_follow = 256
        if math.dist((player.x, player.y), (self._x, self._y)) > distance_to_follow:
            self._stop_following()
            return

        self._start_following()

        delta_x = player.x - self._x
        delta_y = player.y - self._y

        if abs(delta_x) <= abs(delta_y) and delta_y <= 0:
            self._facing = MapDirection.NORTH
        if abs(delta_x) <= abs(delta_y) and delta_y > 0:
            self._facing = MapDirection.SOUTH
        if abs(delta_x) > abs(delta_y) and delta_y <= 0:
            self._facing = MapDirection.WEST
        if abs(delta_x) > abs(delta_y) and delta_y > 0:
            self._facing = MapDirection.EAST

    def _stop_following(self):
        self._is_following_player = False

    def _start_following(self):
        self._is_following_player = True

    @staticmethod
    def new_direction() -> MapDirection:
        rand = randint(1, 4)
        if rand == 1:
            return MapDirection.NORTH
        if rand == 2:
            return MapDirection.EAST
        if rand == 3:
            return MapDirection.SOUTH
        return MapDirection.WEST

    @property
    def is_attacking(self) -> bool:
        return self._is_attacking

    @property
    def hostile_entity_type(self) -> HostileEntityType:
        return self._entity_type

    @property
    def is_following(self) -> bool:
        return self._is_following_player

    @property
    def attack_frame(self) -> int:
        return self._attack_frame
