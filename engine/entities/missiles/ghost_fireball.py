from engine.entities.missiles.missile import Missile
from utilities.map_direction import MapDirection


class GhostFireball(Missile):
    def __init__(self, x: int, y: int, facing: MapDirection):
        super().__init__(x, y, 2, facing, 10, 8, 8, 3)

    def increase_animation_frame(self):
        self._animation_frame += 1
        if not self._animation_frame % 18:
            self._animation_frame = 0
