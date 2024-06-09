import numpy as np
from .map import Map
from typing import Any
from ..entities.wall import Wall
from ..entities.floor import Floor
from ..entities.player import Player
from .tile_type import TileType
from .prefab_maps import *

TILESIZE = 32
NUM_OF_ROOMS = 3
ROOM_SIZE = 4

class MapBuilder():
    def __init__(self, win_h: int, win_w: int, starting_point: tuple[int, int], *groups: Any) -> None:
        self.map = Map(win_w, win_h)
        self.starting_point = starting_point
        self.floor_layer = groups[0]
        self.wall_layer = groups[1]
        self.player_layer = groups[2]
    
    def build(self, rng: np.random.Generator):
        self.fill()
        self.build_random_rooms(rng)

    def fill(self):
        for row in range(self.map.map_height):
            for column in range(self.map.map_width):
                Wall(row, column, TILESIZE, self.wall_layer)
    
    def build_random_rooms(self, rng: np.random.Generator):
        room_count = 0
        while room_count < NUM_OF_ROOMS:
            start_row = rng.integers(1, self.map.map_height - 1)
            start_column = rng.integers(1, self.map.map_width - 1)
            starting_point = self.map.map_index(start_row, start_column)
            self.room_build_rule(starting_point, ROOM_SIZE)
            break

    def room_build_rule(self, starting_point: int ,room_size: int) -> None:
        row_above = (starting_point - (self.map.map_width + 1)) 
        row_below = (starting_point + (self.map.map_width + 1))
        right = starting_point + 1
        left = starting_point - 1

        floors = 0
        self.map.tiles[starting_point] = TileType.FLOOR.value
        while floors < room_size:
            if starting_point < self.map.map_width and starting_point < self.map.map_height: 
                if self.map.tiles[row_above] is not TileType.FLOOR.value:
                    self.map.tiles[row_above] = TileType.FLOOR.value
                    floors += 1

                if self.map.tiles[row_below] is not TileType.FLOOR.value:
                    self.map.tiles[row_below] = TileType.FLOOR.value
                    floors += 1

                if self.map.tiles[right] is not TileType.FLOOR.value:
                    self.map.tiles[right] = TileType.FLOOR.value
                    floors += 1
            
                if self.map.tiles[left] is not TileType.FLOOR.value:
                    self.map.tiles[left] = TileType.FLOOR.value
                    floors += 1
            
            break

    def build_prefab(self):
        for i, row in enumerate(level_1_tilemap):
            for j, column in enumerate(row):
                if column == TileType.FLOOR.value:
                    Floor(j, i, TILESIZE, self.floor_layer)

                if column == TileType.WALL.value:
                    Wall(j, i, TILESIZE, self.wall_layer)
                
                if column == TileType.PLAYER.value:
                     Player(j, i, self.player_layer)