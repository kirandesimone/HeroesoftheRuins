from typing import Literal
from .game_state import GameState

class GameStateManager:
    def __init__(self) -> None:
        self.current_state = GameState.LOADING.value
        self.message_queue = []
    
    def get_current_state(self) -> int:
        return self.current_state
    
    def set_current_state(self, new_state: Literal[GameState.LOADING, GameState.NEXT]) -> None:
        self.current_state = new_state.value
        
