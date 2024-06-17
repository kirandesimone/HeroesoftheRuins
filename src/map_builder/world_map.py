from .dungeons.dungeon_protocol import Dungeon
from .dungeons.battle_dungeon import BattleDungeon
from .dungeons.boss_dungeon import BossDungeon
from .dungeons.entrance_dungeon import EntranceDungeon
from .dungeons.treasure_dungeon import TreasureDungeon
from .dungeons.merchant_dungeon import MerchantDungeon
from .dungeons.dungeon_type import DungeonType

MAX_DUNGEON_COUNT = 7

class WorldMap:
    # We'll be storing our world map in an adjacency list
    def __init__(self) -> None:
        self.dungeon_digraph: dict[int, Dungeon] = {}
        self.isLoading: bool = True

        self.__construct_base()

    def __construct_base(self) -> None:
        entrance_dungeon: Dungeon = EntranceDungeon(0)
        merchant_dungeon: Dungeon = MerchantDungeon(8)
        boss_dungeon: Dungeon = BossDungeon(9)

        self.__add_vertex(entrance_dungeon)
        self.__add_vertex(merchant_dungeon)
        self.__add_vertex(boss_dungeon)
        self.__add_directed_edge(merchant_dungeon, boss_dungeon)
        self.__add_directed_edge(entrance_dungeon, merchant_dungeon)
    
    def __rewrite(self) -> None:
        # we add the max amount of dungeons by adding all battle dungeons 
        # then we walk the graph and run the
        # rules that are needed to craft a world
        pass
    
    def __merchant_before_boss_rule(self) -> None:
        # There must be a merchant dungeon room before every boss dungeon
        pass
        
    def __add_directed_edge(self, from_dungeon: Dungeon, to_dungeon: Dungeon) -> None:
        # The vertices must be added to the graph before making edges
        from_dungeon_value = self.dungeon_digraph.get(from_dungeon.id)
        to_dungeon_value = self.dungeon_digraph.get(to_dungeon.id)

        if from_dungeon_value and to_dungeon_value:
            from_dungeon_value.add_adjacent(to_dungeon.id)
        
    def __add_vertex(self, dungeon: Dungeon) -> None:
        self.dungeon_digraph[dungeon.id] = dungeon
