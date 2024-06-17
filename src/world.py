import pygame
import sys
import numpy as np
 
from .events import *
from .entities.player import Player
from .map_builder.map_builder import MapBuilder
from .map_builder.world_map import WorldMap

BLACK=(0,0,0)

class World:
    def __init__(self, window_width: int, window_height: int, tilesize: int):
        pygame.init()
        pygame.display.set_caption("Heroes of the Ruins")
        self._is_active = True
        self._screen = pygame.display.set_mode((window_width, window_height))
        self._tilesize = tilesize
        self._clock = pygame.time.Clock()
        self.message_queue: list[Message] = []
    
    def _create(self):
        # Create game layers for each entity
        self._playing = True

        self.all_sprites_layer = pygame.sprite.LayeredUpdates()
        self.floor_layer = pygame.sprite.LayeredUpdates()
        self.wall_layer = pygame.sprite.LayeredUpdates()
        self.enemy_layer = pygame.sprite.LayeredUpdates()
        self.player_layer = pygame.sprite.LayeredUpdates()

        rng = np.random.default_rng(seed=10)

        world_map = WorldMap()
        print(world_map.dungeon_digraph)

        """MapBuilder(
            self._screen.get_width(), 
            self._screen.get_height(), 
            (15, 20), 
            self.floor_layer, self.wall_layer, self.player_layer
        ).build(rng)
        """
    
    def _system_events(self):
        for sys_event in pygame.event.get():
            if sys_event.type == pygame.QUIT:
                self._playing = False 
                break
            elif sys_event.type == pygame.KEYDOWN:
                player = self.player_layer.sprites()[0]
                if sys_event.key == pygame.K_w or sys_event.key == pygame.K_UP:
                    self.message_queue.append(MoveMessage(player, "up"))
                elif sys_event.key == pygame.K_s or sys_event.key == pygame.K_DOWN:
                    self.message_queue.append(MoveMessage(player, "down"))
                elif sys_event.key == pygame.K_a or sys_event.key == pygame.K_LEFT:
                    self.message_queue.append(MoveMessage(player, "left"))
                elif sys_event.key == pygame.K_d or sys_event.key == pygame.K_RIGHT:
                    self.message_queue.append(MoveMessage(player, "right"))
            
    def _update(self):
        self.player_layer.update(self.message_queue)

        # This might need to change but we need to clear the queue once all messages have been passed
        self.message_queue.clear()

    def _draw(self, fps: float):
        self._screen.fill(BLACK)
        self.wall_layer.draw(self._screen)
        self.floor_layer.draw(self._screen)
        self.player_layer.draw(self._screen)
        self._clock.tick(fps)
        pygame.display.update()

    def start(self, fps: float):
        self._create()

        while self._playing:
            self._system_events()
            self._update()
            self._draw(fps)
        
        pygame.quit()
        sys.exit()
    
    def finish(self):
        pass
