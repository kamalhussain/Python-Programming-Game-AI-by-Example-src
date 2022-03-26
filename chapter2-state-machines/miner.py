from __future__ import annotations
from abc import ABC, abstractmethod
from base_game_entity import BaseGameEntity
from locations import LocationType
from miner_owned_states import EnterMineAndDigForNugget, VisitBankAndDepositGold, GoHomeAndSleepTilRested, QuenchThirst

class State(ABC):
    @abstractmethod
    def execute(self, miner: Miner) -> None:
        pass

class Miner(BaseGameEntity):
    def __init__(self, id: int) -> None:
        super().__init__(id)
        self.state: State = EnterMineAndDigForNugget()
        self.location_type = LocationType.shack
        self.gold_carried = 0
        self.money_in_bank = 0
        self.thirst = 0
        self.fatigue = 0

    def update(self) -> None:
        self.thirst += 1
        if self.state:
            self.state.execute(self)

    def change_state(self, state: State) -> None:
        self.state = state


    
