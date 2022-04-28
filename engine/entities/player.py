import pygame
from utilities.map_direction import MapDirection
from utilities.resource_manager import ResourceManager
from engine.entities.entity import Entity


class Player(Entity):
    BOUNDING_BOX_SIZE: int = 48
    HIT_BOX_SIZE: int = 32

    def __init__(self, x: int, y: int, health: int, damage: int):
        super().__init__(x, y, health, damage)
        self._coins: int = 0
        self._has_sword: bool = False
        self._facing: MapDirection = MapDirection.WEST
        self._hit_box: pygame.Rect = pygame.Rect(x, y, self.HIT_BOX_SIZE, self.HIT_BOX_SIZE)
        # self._bounding_box: pygame.Rect = pygame.Rect(x, y, self.BOUNDING_BOX_SIZE, self.HIT_BOX_SIZE)
        self.rect: pygame.Rect = pygame.Rect(x, y, self.BOUNDING_BOX_SIZE, self.HIT_BOX_SIZE)
        self._attack_frame = 0
        self._is_damaged = 0
        self._is_walking = False
        self.image = ResourceManager.player_walking_left_1

    def move(self):
        self._is_walking = True

        if self._facing == MapDirection.NORTH:
            self._y -= 1
            self._hit_box.y -= 1
            self.rect.y -= 1
            self._hit_box.update(self._x, self._y, self.HIT_BOX_SIZE, self.BOUNDING_BOX_SIZE)
        if self._facing == MapDirection.WEST:
            self._x -= 1
            self._hit_box.x -= 1
            self.rect.x -= 1
            self._hit_box.update(self._x, self._y, self.BOUNDING_BOX_SIZE, self.HIT_BOX_SIZE)
        if self._facing == MapDirection.EAST:
            self._x += 1
            self._hit_box.x += 1
            self.rect.x += 1
            self._hit_box.update(self._x, self._y, self.BOUNDING_BOX_SIZE, self.HIT_BOX_SIZE)
        if self._facing == MapDirection.SOUTH:
            self._y += 1
            self._hit_box.y += 1
            self.rect.y += 1
            self._hit_box.update(self._x, self._y, self.HIT_BOX_SIZE, self.BOUNDING_BOX_SIZE)

        self.rect.update(self._x, self._y, self.BOUNDING_BOX_SIZE, self.BOUNDING_BOX_SIZE)

        self.increase_animation_frame()
        self.update_image()

    def update_image(self):
        if self._is_damaged:
            if self._facing == MapDirection.NORTH:
                self.image = ResourceManager.player_walking_back_1
            elif self._facing == MapDirection.SOUTH:
                self.image = ResourceManager.player_walking_front_1
            elif self._facing == MapDirection.WEST:
                self.image = ResourceManager.player_walking_left_1
            else:
                self.image = pygame.transform.flip(ResourceManager.player_walking_left_1, True, False)

            # TODO - Y Offset

        elif self._attack_frame:
            if self._attack_frame > 20:
                image_version = 0
            elif self._attack_frame > 10:
                image_version = 1
            else:
                image_version = 2

            if self._facing == MapDirection.EAST:
                self.image = pygame.transform.flip(ResourceManager.player_attack[1][image_version], True, False)
            else:
                self.image = ResourceManager.player_attack[self._facing.value][image_version]

        else:
            if self._animation_frame < 15:
                image_version = 0
            else:
                image_version = 1

            if self._facing == MapDirection.EAST:
                if self._is_walking:
                    self.image = pygame.transform.flip(ResourceManager.player_movement[4][self._has_sword][image_version], True, False)
                else:
                    self.image = pygame.transform.flip(ResourceManager.player_movement[1][self._has_sword][image_version], True, False)

            elif self._is_walking:
                self.image = ResourceManager.player_movement[self._facing.value+3][self._has_sword][image_version]
            else:
                self.image = ResourceManager.player_movement[self._facing.value][self._has_sword][image_version]

    def add_health(self):
        self.heal(2)

    def add_max_health(self):
        self.increase_max_health(2)
        self.add_health()

    def add_coin(self):
        self._coins += 1

    def increase_attack_frame(self):
        self._attack_frame += 1
        if self._attack_frame > 30:
            self._attack_frame = 0

    def increase_animation_frame(self):
        self._animation_frame += 1
        if self._animation_frame == 40:
            self._animation_frame = 0

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

    @property
    def is_damaged(self):
        return self._is_damaged

    @is_damaged.setter
    def is_damaged(self, value: bool):
        self._is_damaged = value

    @property
    def is_walking(self) -> bool:
        return self._is_walking

    @is_walking.setter
    def is_walking(self, value: bool):
        self._is_walking = value
