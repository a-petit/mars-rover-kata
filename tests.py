import pytest

from rover import Rover


@pytest.mark.parametrize("position", ["1 2 N", "4 3 N"])
def test_landing(position):
    assert Rover.at(position).position() == position


@pytest.mark.parametrize("initial,commands,final", [
    # Turn left
    ("0 0 N", "L", "0 0 W"),
    ("0 0 N", "LL", "0 0 S"),
    ("0 0 N", "LLL", "0 0 E"),
    ("0 0 N", "LLLL", "0 0 N"),
    # Turn right
    ("0 0 N", "R", "0 0 E"),
    ("0 0 N", "RR", "0 0 S"),
    ("0 0 N", "RRR", "0 0 W"),
    ("0 0 N", "RRRR", "0 0 N"),
    # Move in the 4 directions
    ("2 2 N", "M", "2 3 N"),
    ("2 2 E", "M", "3 2 E"),
    ("2 2 S", "M", "2 1 S"),
    ("2 2 W", "M", "1 2 W"),
    # Scenario
    ("1 2 N", "LMLMLMLMM", "1 3 N"),
    ("3 3 E", "MMRMMRMRRM", "5 1 E"),
])
def test_execute_commands(initial, commands, final):
    rover = Rover.at(initial)
    rover.executes(commands)
    assert rover.position() == final
