from typing import Protocol

# Describes a dungeon (vertex/node in the graph)
class Dungeon(Protocol):
    id: int
    type: str
    adjacents: list[int]

    def add_adjacent(self, dungeon_id: int) -> None: ...
    def build(self) -> None: ...
