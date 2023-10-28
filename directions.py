from abc import abstractmethod


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


class South(Direction):
    def left(self):
        raise NotImplementedError()

    def label(self) -> str:
        return "S"


class West(Direction):
    def label(self) -> str:
        return "W"

    def left(self):
        return South()


class North(Direction):
    def label(self) -> str:
        return "N"

    def left(self):
        return West()
