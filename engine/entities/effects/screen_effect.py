
class ScreenEffect:
    def __init__(self, x: int, y: int, duration: int):
        self._x: int = x
        self._y: int = y
        self._duration: int = duration
        self._animation_frame = 0

    def increase_animation_frame(self):
        if self._animation_frame >= self._duration:
            return
        self._animation_frame += 1

    @property
    def x(self) -> int:
        return self._x

    @x.setter
    def x(self, value: int):
        if not isinstance(value, int):
            raise ValueError("x must be an int")
        self._x = value

    @property
    def y(self) -> int:
        return self._y

    @y.setter
    def y(self, value: int):
        if not isinstance(value, int):
            raise ValueError("y must be an int")
        self._y = value

    @property
    def animation_frame(self) -> int:
        return self._animation_frame

    @property
    def effect_duration(self) -> int:
        return self.effect_duration
