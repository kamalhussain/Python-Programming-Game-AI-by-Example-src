from __future__ import annotations
from abc import ABC, abstractmethod
from base_game_entity import BaseGameEntity
from locations import LocationType
from entity_names import EntityName, get_name_of_entity
from state import State
from state_machine import StateMachine

class MinerWife(BaseGameEntity):
    def __init__(self, id: int) -> None:
        import miner_owned_states
        super().__init__(id)
        self.state  = miner_owned_states.EnterMineAndDigForNugget()
        self.state_machine = StateMachine(self)
        self.state_machine.state = miner_owned_states.GoHomeAndSleepTilRested()
        self.location_type = LocationType.shack

    def update(self) -> None:
        self.state_machine.update()