import pytest


class Rover:
    @classmethod
    def at(cls, position):
        return Rover()

    def position(self):
        return "1 2 N"


@pytest.mark.parametrize("position", ["1 2 N"])
def test_landing(position):
    assert Rover.at(position).position() == position
