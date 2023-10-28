from directions import Direction
from vector import Vector


class Rover:
    def __init__(self, coordinates, direction):
        self._coordinates: Vector = coordinates
        self._direction: Direction = direction

    @classmethod
    def at(cls, position):
        x, y, d = position.split(" ")
        coordinates = Vector(int(x), int(y))
        direction = Direction.from_label(d)
        return Rover(coordinates, direction)

    def position(self):
        return f"{self._coordinates.label()} {self._direction.label()}"

    def executes(self, commands):
        for command in commands:
            match command:
                case "L": self._direction = self._direction.left()
                case "R": self._direction = self._direction.right()
                case "M": self._coordinates = self._coordinates + self._direction.delta()
                case _: raise Exception(f"{command} non reconnue")
