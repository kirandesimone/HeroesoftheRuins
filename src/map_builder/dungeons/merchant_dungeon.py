from .dungeon_type import DungeonType

class MerchantDungeon:
    def __init__(self, id: int) -> None:
        self.id: int = id
        self.type: str = DungeonType.MERCHANT.value
        self.adjacents: list[int] = []
    
    def add_adjacent(self, dungeon_id: int) -> None:
        self.adjacents.append(dungeon_id)

    def build(self) -> None:
        pass
    
    def __repr__(self) -> str:
        return f'{self.id} --> {self.adjacents}'