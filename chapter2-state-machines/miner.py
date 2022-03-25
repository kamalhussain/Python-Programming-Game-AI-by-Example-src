from __future__ import annotations
from abc import ABC, abstractmethod
from base_game_entity import BaseGameEntity

class State(ABC):
    @abstractmethod
    def execute(self, miner: Miner):
        pass

class Miner(BaseGameEntity):
    def __init__(self, id):
        super().__init__(id)
        self.state = None
        self.location_type = None
        self.gold_carried = 0
        self.money_in_bank = 0
        self.thirst = 0
        self.fatigue = 0

    def update(self):
        self.thirst += 1
        if self.state:
            self.state.exectute(self)

    def change_state(state):
        self.state = state

class EnterMineAndDigForNugget(State):
    def execute(self, miner: Miner):
        pass

class VisitBankAndDepositGold(State):
    def execute(self, miner: Miner):
        pass

class GoHomeAndSleepTilRested(State):
    def execute(self, miner: Miner):
        pass

class QuenchThirst(State):
    def execute(self, miner: Miner):
        pass

    
