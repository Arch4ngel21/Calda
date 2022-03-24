from engine.entities.hostile_entity import HostileEntity
from engine.world.map import Map
from engine.entities.player import Player

class GameEngine:
    _initialized = False

    _keys = [] # tablica przycisków
    _player = None
    _hostile_entities = []
    _peaceful_entities = []
    _chests = []
    _items = []
    _missiles = []
    _effects = []
    _prompts = []

    _world_map = None
    _current_level = None
    _is_running = True

    @staticmethod
    def start_engine():
        pass

    @staticmethod
    def generate_levels():
        pass

    @staticmethod
    def handle_player_movement():
        pass

    @staticmethod
    def handle_player_interaction():
        pass

    @staticmethod
    def handle_enemies_movement():
        pass

    @staticmethod
    def handle_missiles():
        pass

    @staticmethod
    def handle_enemies_attack():
        pass

    @staticmethod
    def handle_peaceful_entities_actions():
        pass

    @staticmethod
    def handle_effects():
        pass

    @staticmethod
    def handle_pick_up_items():
        pass

    @staticmethod
    def handle_player_attack():
        pass

    @staticmethod
    def start_player_attack_animation():
        pass

    @staticmethod
    def handle_enemies_drop():
        pass

    @staticmethod
    def handle_level_change():
        pass

    @staticmethod
    def handle_enter_dungeon():
        pass

    @staticmethod
    def start_missile_animation(enemy: HostileEntity):
        pass

    @staticmethod
    def handle_missile(enemy: HostileEntity):
        pass











