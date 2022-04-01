from miner import Miner 
from state import State
from locations import LocationType

class EnterMineAndDigForNugget(State):
    def enter(self, miner: Miner) -> None:
        miner.location_type = LocationType.goldmine
        miner.say("Walkin' to the gold mine")

    
    def execute(self, miner: Miner) -> None:
        miner.gold_carried += 1
        miner.fatigue += 1
        miner.say("Pickin' up a nugget")
        if miner.gold_carried >= 2:
            miner.change_state(VisitBankAndDepositGold())
        elif miner.thirst >= 4:
            miner.change_state(QuenchThirst())

    def exit(self, miner: Miner) -> None:
        miner.say("Ah'm leavin' the gold mine with mah pockets full o' sweet gold")

class VisitBankAndDepositGold(State):
    def enter(self, miner: Miner) -> None:
        miner.location_type = LocationType.bank
        miner.say("Goin' to the bank. Yes siree")
    
    def execute(self, miner: Miner) -> None:
        miner.money_in_bank += miner.gold_carried
        miner.gold_carried = 0
        miner.say(f"Depositin' gold. Total savings now: {miner.money_in_bank}")
        if miner.money_in_bank >= 5:
            miner.say("Woohoo! Rich enough for now. Back home to mah li'l lady")
            miner.change_state(GoHomeAndSleepTilRested())
        else:
            miner.change_state(EnterMineAndDigForNugget())
        
    
    def exit(self, miner: Miner) -> None:
        miner.say("Leavin' the bank")

class GoHomeAndSleepTilRested(State):
    def enter(self, miner: Miner) -> None:
        miner.location_type = LocationType.shack
        miner.say("Walkin' home")
    
    def execute(self, miner: Miner) -> None:
        miner.say("ZZZZ...")
        miner.fatigue -= 1
        if miner.fatigue <= 0:
            miner.change_state(EnterMineAndDigForNugget())
    
    def exit(self, miner: Miner) -> None:
        miner.say("What a God-darn fantastic nap! Time to find more gold")

class QuenchThirst(State):
    def enter(self, miner: Miner) -> None:
        miner.location_type = LocationType.saloon
        miner.say("Boy, ah sure is thusty! Walkin' to the saloon")
    
    def execute(self, miner: Miner) -> None:
        miner.thirst = 0
        miner.gold_carried -= 1
        miner.say("That's mighty fine sippin' liquor")
        miner.change_state(EnterMineAndDigForNugget())
    
    def exit(self, miner: Miner) -> None:
        miner.say("Leavin' the saloon, feelin' good")
