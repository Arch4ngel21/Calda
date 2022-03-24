import sys

import pygame
from typing import List

from engine.entities.hostile_entity import HostileEntity
from engine.entities.peaceful_entity import PeacefulEntity
from engine.entities.container import Container
from engine.collectibles.collectible import Collectible
from engine.entities.missiles.missile import Missile
from engine.entities.effects.screen_effect import ScreenEffect
from engine.entities.effects.screen_prompt import ScreenPrompt
from engine.world.map import Map
from engine.world.level_map import LevelMap
from utilities.map_direction import MapDirection
from utilities.resource_manager import ResourceManager
from engine.entities.player import Player


class GameEngine:
    _initialized = False

    _keys = [] # tablica przycisków
    _player: Player = None
    _hostile_entities: List[HostileEntity] = []
    _peaceful_entities: List[PeacefulEntity] = []
    _chests: List[Container] = []
    _items: List[Collectible] = []
    _missiles: List[Missile] = []
    _effects: List[ScreenEffect] = []
    _prompts: List[ScreenPrompt] = []

    _world_map: Map = None
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
        # TODO
        GameEngine._player = Player(480, 900, 10, 2)
        GameEngine.generate_levels()

    @staticmethod
    def generate_levels():

        levels = [LevelMap(2, 0, ResourceManager.level_2_0), LevelMap(3, 0, ResourceManager.level_3_0),
                  LevelMap(2, 1, ResourceManager.level_2_1), LevelMap(3, 1, ResourceManager.level_3_1),
                  LevelMap(4, 1, ResourceManager.level_4_1), LevelMap(0, 2, ResourceManager.level_0_2),
                  LevelMap(1, 2, ResourceManager.level_1_2), LevelMap(4, 2, ResourceManager.level_4_2),
                  LevelMap(0, 3, ResourceManager.level_0_3), LevelMap(2, 3, ResourceManager.level_2_3),
                  LevelMap(3, 3, ResourceManager.level_3_3), LevelMap(4, 3, ResourceManager.level_4_3),
                  LevelMap(0, 4, ResourceManager.level_0_4), LevelMap(1, 3, ResourceManager.level_1_3),
                  LevelMap(1, 4, ResourceManager.level_1_4), LevelMap(2, 4, ResourceManager.level_2_4),
                  LevelMap(3, 4, ResourceManager.level_3_4), LevelMap(4, 4, ResourceManager.level_4_4)]

        for level in levels:
            GameEngine._world_map.add_level(level)


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











