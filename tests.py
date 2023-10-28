import pytest

from rover import Rover


@pytest.mark.parametrize("position", ["1 2 N", "4 3 N"])
def test_landing(position):
    assert Rover.at(position).position() == position


@pytest.mark.parametrize("initial,commands,final", [
    ("0 0 N", "L", "0 0 W"),
    ("0 0 N", "LL", "0 0 S"),
])
def test_execute_commands(initial, commands, final):
    rover = Rover.at(initial)
    rover.executes(commands)
    assert rover.position() == final
