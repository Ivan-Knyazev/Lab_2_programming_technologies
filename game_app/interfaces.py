from typing import Union
from abc import ABC, abstractmethod
from game_app.abs_objects import Unit, Building


class Attacker(ABC):
    @abstractmethod
    def attack(self, unit: Unit) -> None:
        """Method to attack a unit and deal damage to their hp"""
        raise NotImplementedError(
                'Implement attack() in %s.' % (self.__class__.__name__))


class Moveable(ABC):
    @abstractmethod
    def move(self, diffX: int, diffY: int) -> None:
        """Method to move a unit or a building"""
        raise NotImplementedError(
                'Implement move() in %s.' % (self.__class__.__name__))
