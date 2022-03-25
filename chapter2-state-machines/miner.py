from base_game_entity import BaseGameEntity

class State:
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

    def update():
        self.thirst += 1
        if self.state:
            self.state.exectute(self)

    def change_state(state):
        self.state = state
