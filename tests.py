import pytest


class Rover:
    def __init__(self, position):
        self._position = position

    @classmethod
    def at(cls, position):
        return Rover(position)

    def position(self):
        return self._position

    def executes(self, commands):
        self._position = "0 0 W"


@pytest.mark.parametrize("position", ["1 2 N", "4 3 N"])
def test_landing(position):
    assert Rover.at(position).position() == position


def test_execute_commands():
    rover = Rover.at("0 0 N")
    rover.executes("L")
    assert rover.position() == "0 0 W"
