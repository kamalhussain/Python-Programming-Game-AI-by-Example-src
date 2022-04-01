from __future__ import annotations
from abc import ABC, abstractmethod
from base_game_entity import BaseGameEntity
from locations import LocationType
from entity_names import EntityName, get_name_of_entity
#from state import State
from state_machine import StateMachine

class Miner(BaseGameEntity):
    def __init__(self, id: int) -> None:
        import miner_owned_states

        super().__init__(id)
        self.state  = miner_owned_states.EnterMineAndDigForNugget()
        self.state_machine = StateMachine(self)
        self.state_machine.state = miner_owned_states.GoHomeAndSleepTilRested()
        # TODO set global state
        self.location_type = LocationType.shack
        self.gold_carried = 0
        self.money_in_bank = 0
        self.thirst = 0
        self.fatigue = 0

    def update(self) -> None:
        self.thirst += 1
        self.state_machine.update()

    #def change_state(self, state: State) -> None:
    #    self.state.exit(self)
    #    self.state = state
    #    self.state.enter(self)
    
    def revert_to_prev_state(self) -> None:
        self.state.exit(self)
        self.state = self.prev_state
        self.state.enter(self)

    def say(self, speech: str) -> None:
        print(f"{get_name_of_entity(EntityName(self.id))}: {speech}")

    def get_FSM(self) -> StateMachine:
        return self.state_machine