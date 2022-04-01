from abc import ABC
from state import State

class StateMachine(ABC):
    def __init__(self, owner, state: State, prev_state: State = None, global_state: State = None) -> None:
        self.owner = owner
        self.state = state
        self.prev_state = prev_state
        self.global_state = global_state

    def update(self) -> None:
        if self.global_state:
            self.global_state.execute(self.owner)
        
        if self.state:
            self.state.execute(self.owner)
    
    def change_state(self, new_state: State):
        assert new_state, "new state can't be null"
        self.prev_state = self.state
        self.state.exit(self.owner)
        self.state = self.new_state
        self.state.enter(self.owner)
    
    def revert_to_prev_state(self):
        self.change_state(self.prev_state)
    
    def is_in_state(self, state: State):
        return type(self.state) == type(state)
    
