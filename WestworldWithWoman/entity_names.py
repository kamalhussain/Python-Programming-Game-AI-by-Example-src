from enum import Enum, auto, unique

@unique
class EntityName(Enum):
    Miner_Bob = auto()
    Elsa = auto()

def get_name_of_entity(entity: EntityName) -> str:
    if entity == EntityName.Miner_Bob:
        return "Miner Bob"
    elif entity == EntityName.Elsa:
        return "Elsa"
    else:
        return "UNKNOWN!"

