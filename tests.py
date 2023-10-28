from abc import abstractmethod

import pytest


class Direction:
    @classmethod
    def from_label(cls, label):
        return North()

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def label(self) -> str:
        pass


class West(Direction):
    def label(self) -> str:
        return "W"

    def left(self):
        raise NotImplementedError()


class North(Direction):
    def label(self) -> str:
        return "N"

    def left(self):
        return West()


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
        self._direction = self._direction.left()


@pytest.mark.parametrize("position", ["1 2 N", "4 3 N"])
def test_landing(position):
    assert Rover.at(position).position() == position


@pytest.mark.parametrize("initial,commands,final", [
    ("0 0 N", "L", "0 0 W"),
    # ("0 0 N", "LL", "0 0 S"),
])
def test_execute_commands(initial, commands, final):
    rover = Rover.at(initial)
    rover.executes(commands)
    assert rover.position() == final
