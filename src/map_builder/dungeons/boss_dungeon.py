from .dungeon_type import DungeonType

class BossDungeon:
    def __init__(self) -> None:
        self.type = DungeonType.BOSS.value
    
    def build(self) -> None:
        pass
    
    def get_type(self) -> str:
        return self.type