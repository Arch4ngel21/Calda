import sys

import pygame

from engine.entities.hostile_entity import HostileEntity
from engine.world.map import Map
from utilities.map_direction import MapDirection
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
    def run():
        clock = pygame.time.Clock()
        while True:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        start_player_attack_animation()
                    if event.key == pygame.K_w:
                        handle_player_movement(MapDirection.NORTH)
                    if event.key == pygame.K_a:
                        handle_player_movement(MapDirection.WEST)
                    if event.key == pygame.K_s:
                        handle_player_movement(MapDirection.SOUTH)
                    if event.key == pygame.K_d:
                        handle_player_movement(MapDirection.EAST)
                    if event.key == pygame.K_e:
                        handle_player_interaction()

            handle_enemies_movement()
            handle_enemies_attack()
            handle_peaceful_entities_actions()
            handle_effects()
            handle_missiles()
            handle_enemies_drop()
            handle_level_change()

    @staticmethod
    def start_engine():
        pass

    @staticmethod
    def generate_levels():
        pass


def handle_player_movement(direction: MapDirection):
    pass


def handle_player_interaction():
    pass


def handle_enemies_movement():
    pass


def handle_missiles():
    pass


def handle_enemies_attack():
    pass


def handle_peaceful_entities_actions():
    pass


def handle_effects():
    pass


def handle_pick_up_items():
    pass


def handle_player_attack():
    pass


def start_player_attack_animation():
    pass


def handle_enemies_drop():
    pass


def handle_level_change():
    pass


def handle_enter_dungeon():
    pass


def start_missile_animation(enemy: HostileEntity):
    pass


def handle_missile(enemy: HostileEntity):
    pass











