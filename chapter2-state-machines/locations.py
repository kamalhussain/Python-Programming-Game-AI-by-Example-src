from enum import Enum, auto, unique

@unique
class LocationType(Enum):
    shack = auto()
    goldmine = auto()
    bank = auto()
    saloon = auto()
