from .tile_type import TileType
from ..entities.wall import Wall
from ..entities.floor import Floor

TILE_SIZE = 32

class Map():
    def __init__(self, window_width, window_height) -> None:
        self.map_width = window_width // TILE_SIZE
        self.map_height = window_height // TILE_SIZE
        self.max_tile_count = self.map_width * self.map_height

        self.tiles = list(map(lambda _tile_idx: TileType.WALL.value, range(self.max_tile_count)))
    
    def map_index(self, x, y) -> int:
        return (y * self.map_width) + x
""" 
    def build(self) -> None:
        for y in range(self.map_height):
            for x in range(self.map_width):
                index = self.map_index(x, y) 
                match self.tiles[index]:
                    case TileType.FLOOR.value:
                        Floor(x, y, TILE_SIZE, self.floor_layer) """