import pygame
import sys
 
from typing import List
from ..entities.player import Player
from ..events import *

BLACK=(0,0,0)

class World:
    def __init__(self, window_width: int, window_height: int):
        pygame.init()
        self._is_active = True
        self._screen = pygame.display.set_mode((window_width, window_height))
        self._clock = pygame.time.Clock()
        self.message_queue: List[Message] = []
    
    def _create(self):
        # Create game layers for each entity
        self._playing = True

        self.all_sprites_layer = pygame.sprite.LayeredUpdates()
        self.enemies_layer = pygame.sprite.LayeredUpdates()
        self.player_layer = pygame.sprite.LayeredUpdates()

        self.all_sprites_group = pygame.sprite.Group()
        self.enemy_group = pygame.sprite.Group()
        self.player_single_group = pygame.sprite.GroupSingle()

        Player((self.all_sprites_layer, self.all_sprites_group, self.player_single_group))
    
    def _events(self):
        for sys_event in pygame.event.get():
            if sys_event.type == pygame.QUIT:
                self._playing = False 
                break
            elif sys_event.type == pygame.KEYDOWN:
                player = self.player_single_group.sprite
                if sys_event.key == pygame.K_w or sys_event.key == pygame.K_UP:
                    self.message_queue.append(MoveMessage(player, 0, -1))
                elif sys_event.key == pygame.K_s or sys_event.key == pygame.K_DOWN:
                    self.message_queue.append(MoveMessage(player, 0, 1))
                elif sys_event.key == pygame.K_a or sys_event.key == pygame.K_LEFT:
                    self.message_queue.append(MoveMessage(player, -1, 0))
                elif sys_event.key == pygame.K_d or sys_event.key == pygame.K_RIGHT:
                    self.message_queue.append(MoveMessage(player, 1, 0))
            
                
        
    def _update(self):
        self.all_sprites_layer.update()
        self.all_sprites_group.update(self.message_queue)

        # This might need to change but we need to clear the queue once all messages have been passed
        self.message_queue.clear()

    def _draw(self, fps: float):
        self._screen.fill(BLACK)
        self.all_sprites_layer.draw(self._screen)
        self._clock.tick(fps)
        pygame.display.update()

    def start(self, fps: float):
        self._create()

        while self._playing:
            self._events()
            self._update()
            self._draw(fps)
        
        pygame.quit()
    
    def finish(self):
        pass
