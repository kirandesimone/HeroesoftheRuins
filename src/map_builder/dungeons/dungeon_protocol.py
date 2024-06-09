from typing import Protocol

# Describes a dungeon
class Dungeon(Protocol):
    type: str

    def build(self) -> None: ...

    def get_type(self) -> str:
        return self.type 
