from abc import ABC, abstractmethod


class GameObject(ABC):
    @abstractmethod
    def __init__(self, id: int, name: str, X: float, Y: float) -> None:
        self.id: int = id
        self.name: str = name
        self.X: float = X
        self.Y: float = Y

    def getId(self) -> int:
        return self.id

    def getName(self) -> str:
        return self.name

    def getX(self) -> float:
        return self.X

    def getY(self) -> float:
        return self.Y

    @abstractmethod
    def __repr__(self) -> str:
        object = "GameObject(id={0}, name={1}, X={2}, Y={3})".format(
            self.id, self.name, self.X, self.Y)
        return object
