from typing import Iterable

from .dungeons.dungeon_protocol import Dungeon
from .dungeons.battle_dungeon import BattleDungeon
from .dungeons.boss_dungeon import BossDungeon
from .dungeons.entrance_dungeon import EntranceDungeon
from .dungeons.treasure_dungeon import TreasureDungeon
from .dungeons.merchant_dungeon import MerchantDungeon

class WorldMap:
    # We'll be storing our world map in an adjacency list
    def __init__(self) -> None:
        self.dungeon_digraph: dict[str, Iterable[Dungeon]] = {}
        self.isLoading: bool = True

    def __construct_base(self) -> None:
        entrance_dungeon: Dungeon = EntranceDungeon()
        boss_dungeon: Dungeon = BossDungeon()

        self.__add_edge(entrance_dungeon, boss_dungeon)
        

    def __add_edge(self, from_vertex: Dungeon, to_vertex: Dungeon) -> None:
        pass
