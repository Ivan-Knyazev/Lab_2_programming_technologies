from game_app.interfaces import Attacker, Moveable
from game_app.abs_objects import Unit, Building

# Set damage variables
archer_damage = 24.0
fort_damage = 19.0


class Archer(Unit, Attacker, Moveable):
    def __init__(self, name: str, X: float, Y: float,
                 is_alive: bool = True, hp: float = 100) -> None:
        super().__init__(name, X, Y, is_alive, hp)

    def attack(self, unit: Unit) -> None:
        unit.receiveDamage(damage=archer_damage)

    def move(self, diffX: int = 5, diffY: int = 5) -> None:
        self.X += diffX
        self.Y += diffY

    def __repr__(self) -> str:
        object = super().__repr__()
        object = "Archer({0}, is_alive={1}, hp={2})".format(
            object[11:-1], self.is_alive, self.hp)
        return object


class Fort(Building, Attacker):
    def __init__(self, name: str, X: float, Y: float,
                 is_build: bool = False) -> None:
        super().__init__(name, X, Y, is_build)

    def attack(self, unit: Unit) -> None:
        unit.receiveDamage(damage=fort_damage)

    def __repr__(self) -> str:
        object = super().__repr__()
        object = "Fort({0}, is_build={1})".format(object[11:-1], self.is_build)
        return object


class MobileHouse(Building, Moveable):
    def __init__(self, name: str, X: float, Y: float,
                 is_build: bool = False) -> None:
        super().__init__(name, X, Y, is_build)

    def move(self, diffX: int = 3, diffY: int = 3) -> None:
        self.X += diffX
        self.Y += diffY

    def __repr__(self) -> str:
        object = super().__repr__()
        object = "MobileHouse({0}, is_build={1})".format(
            object[11:-1], self.is_build)
        return object
