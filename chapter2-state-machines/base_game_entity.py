class BaseGameEntity:
    id = 1
    def __init__(self, id=None):
        if id != None:
            assert id >= BaseGameEntity.id, f"id: {id} less than BaseGameEntity.id: {BaseGameEntity.id}"
            self.id = id
        else:
            self.id = BaseGameEntity.id 
        BaseGameEntity.id = self.id + 1

    def __repr__(self):
        return f"{type(self).__name__}({self.id}) {BaseGameEntity.id = }"

    
    def update():
        pass

    
