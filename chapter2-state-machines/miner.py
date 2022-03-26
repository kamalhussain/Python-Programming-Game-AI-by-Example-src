from __future__ import annotations
from abc import ABC, abstractmethod
from base_game_entity import BaseGameEntity
from locations import LocationType
from entity_names import EntityName, get_name_of_entity

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

class Miner(BaseGameEntity):
    def __init__(self, id: int) -> None:
        import miner_owned_states

        super().__init__(id)
        self.state: State = miner_owned_states.EnterMineAndDigForNugget()
        self.location_type = LocationType.shack
        self.gold_carried = 0
        self.money_in_bank = 0
        self.thirst = 0
        self.fatigue = 0

    def update(self) -> None:
        self.thirst += 1
        self.state.execute(self)

    def change_state(self, state: State) -> None:
        self.state.exit(self)
        self.state = state
        self.state.enter(self)

    def say(self, speech: str) -> None:
        print(f"{get_name_of_entity(EntityName(self.id))}: {speech}")

def main() -> None:
    m = Miner(1)
    for _ in range(25):
        m.update()

if __name__ == "__main__":
    main()
