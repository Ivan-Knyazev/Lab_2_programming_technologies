from abc import ABC, abstractmethod
from game_app.base_abs_object import GameObject


class Unit(GameObject, ABC):
    @abstractmethod
    def __init__(self, name: str, X: float, Y: float,
                 is_alive: bool = True, hp: float = 100) -> None:
        super().__init__(name, X, Y)
        self.is_alive: bool = is_alive
        self.hp: float = hp

    def isAlive(self) -> bool:
        return self.is_alive

    def getHp(self) -> float:
        return self.hp

    def receiveDamage(self, damage: float) -> None:
        if damage <= self.hp:
            self.hp -= damage
            self.is_alive = True if self.hp > 0 else False
        else:
            raise ValueError("Damage of more hp!")


class Building(GameObject, ABC):
    @abstractmethod
    def __init__(self, name: str, X: float, Y: float,
                 is_build: bool = False) -> None:
        super().__init__(name, X, Y)
        self.is_build: bool = is_build

    def isBuilt(self) -> bool:
        return self.is_build
