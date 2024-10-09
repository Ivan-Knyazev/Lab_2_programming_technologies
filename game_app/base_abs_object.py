from abc import ABC, abstractmethod


class GameObject(ABC):
    
    id_counter: int = 0 # static field for count ID numbrs of objects
    
    @abstractmethod
    def __init__(self, name: str, X: float = 0, Y: float = 0) -> None:
        GameObject.id_counter += 1
        self.id: int = GameObject.id_counter
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
