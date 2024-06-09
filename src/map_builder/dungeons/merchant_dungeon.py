from .dungeon_type import DungeonType


class MerchantDungeon:
    def __init__(self) -> None:
        self.type = DungeonType.MERCHANT.value
    
    def build(self) -> None:
        pass
    
    def get_type(self) -> str:
        return self.type