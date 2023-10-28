import pytest


class Rover:
    def __init__(self, position):
        self._position = position

    @classmethod
    def at(cls, position):
        return Rover(position)

    def position(self):
        return self._position


@pytest.mark.parametrize("position", ["1 2 N", "4 3 N"])
def test_landing(position):
    assert Rover.at(position).position() == position
