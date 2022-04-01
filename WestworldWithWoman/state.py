from __future__ import annotations
from abc import ABC, abstractmethod
from base_game_entity import BaseGameEntity
from locations import LocationType
from entity_names import EntityName, get_name_of_entity
from miner import Miner

class State(ABC):
    def __new__(cls) -> State:
        if not hasattr(cls, 'instance'):
            cls.instance = super(State, cls).__new__(cls)
        return cls.instance

    @abstractmethod
    def enter(self, miner: Miner) -> None:
        """ This will execute when state is entered """
        pass

    @abstractmethod
    def execute(self, miner: Miner) -> None:
        """ This is called by Miner.update each update step """
        pass

    @abstractmethod
    def exit(self, miner: Miner) -> None:
        """ This will execute when state is exited """
        pass