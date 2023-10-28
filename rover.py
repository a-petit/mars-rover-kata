from directions import Direction


class Rover:
    def __init__(self, coordinates, direction):
        self._coordinates = coordinates
        self._direction: Direction = direction

    @classmethod
    def at(cls, position):
        x, y, d = position.split(" ")
        coordinates = f"{x} {y}"
        direction = Direction.from_label(d)
        return Rover(coordinates, direction)

    def position(self):
        return f"{self._coordinates} {self._direction.label()}"

    def executes(self, commands):
        for command in commands:
            match command:
                case "L": self._direction = self._direction.left()
                case "R": self._direction = self._direction.right()
                case _: raise Exception(f"{command} non reconnue")
