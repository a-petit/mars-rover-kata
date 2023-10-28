from abc import abstractmethod


class Direction:
    @classmethod
    def from_label(cls, label):
        return North()

    @abstractmethod
    def left(self):
        pass

    @abstractmethod
    def right(self):
        pass

    @abstractmethod
    def label(self) -> str:
        pass


class East(Direction):
    def right(self):
        return South()

    def left(self):
        return North()

    def label(self) -> str:
        return "E"


class South(Direction):
    def right(self):
        return West()

    def left(self):
        return East()

    def label(self) -> str:
        return "S"


class West(Direction):
    def right(self):
        return North()

    def label(self) -> str:
        return "W"

    def left(self):
        return South()


class North(Direction):
    def right(self):
        return East()

    def label(self) -> str:
        return "N"

    def left(self):
        return West()
