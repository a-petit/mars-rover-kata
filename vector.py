from dataclasses import dataclass


@dataclass
class Vector:
    _x: int
    _y: int

    def label(self) -> str:
        return f"{self._x} {self._y}"

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self._x + other._x, self._y + other._y)
