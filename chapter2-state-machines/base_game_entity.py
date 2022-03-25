from __future__ import annotations
from abc import ABC, abstractmethod

class BaseGameEntity(ABC):
    id = 1
    def __init__(self, id: int|None=None):
        if isinstance(id, int):
            assert id >= BaseGameEntity.id, f"id: {id} less than BaseGameEntity.id: {BaseGameEntity.id}"
            self.id = id
        else:
            self.id = BaseGameEntity.id 
        BaseGameEntity.id = self.id + 1

    def __repr__(self):
        return f"{type(self).__name__}({self.id}) {BaseGameEntity.id = }"

    @abstractmethod
    def update(self):
        pass

    
