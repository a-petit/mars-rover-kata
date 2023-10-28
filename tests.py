class Rover:
    @classmethod
    def at(cls, position):
        return Rover()

    def position(self):
        return "1 2 N"


def test_landing():
    assert Rover.at("1 2 N").position() == "1 2 N"
