from abc import abstractmethod

from vector import Vector


class Direction:
    @classmethod
    def from_label(cls, label):
        match label:
            case "N": return North()
            case "E": return East()
            case _: raise Exception(f"{label} non reconnu")

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass

    @abstractmethod
    def label(self) -> str:
        pass

    @abstractmethod
    def delta(self) -> Vector:
        pass


class East(Direction):
    def delta(self) -> Vector:
        return Vector(1, 0)

    def right(self):
        return South()

    def left(self):
        return North()

    def label(self) -> str:
        return "E"


class South(Direction):
    def delta(self) -> Vector:
        raise NotImplementedError()

    def right(self):
        return West()

    def left(self):
        return East()

    def label(self) -> str:
        return "S"


class West(Direction):
    def delta(self) -> Vector:
        raise NotImplementedError()

    def right(self):
        return North()

    def label(self) -> str:
        return "W"

    def left(self):
        return South()


class North(Direction):
    def delta(self) -> Vector:
        return Vector(0, 1)

    def right(self):
        return East()

    def label(self) -> str:
        return "N"

    def left(self):
        return West()
