import math
from random import randint
import sys
import pygame
from typing import List

from engine.entities.hostile_entity import HostileEntity
from engine.entities.hostile_entity import HostileEntityType
from engine.entities.missiles.ghost_fireball import GhostFireball
from engine.entities.peaceful_entity import PeacefulEntity
from engine.entities.peaceful_entity import PeacefulEntityType
from engine.entities.peaceful_entity import Entity
from engine.entities.container import Container
from engine.entities.container import ContainerType
from engine.collectibles.collectible import Collectible
from engine.collectibles.collectible import ItemType
from engine.entities.missiles.missile import Missile
from engine.entities.effects.screen_effect import ScreenEffect
from engine.entities.effects.screen_prompt import ScreenPrompt
from engine.entities.effects.chest_open_effect import ChestOpenEffect
from engine.world.map import Map
from engine.world.level_map import LevelMap
from utilities.map_direction import MapDirection
from utilities.resource_manager import ResourceManager
from engine.entities.player import Player
from gui.main_screen import MainScreen


class GameEngine:
    _initialized = False

    _keys = [] # tablica przycisków
    _player: Player = Player(480, MainScreen.WINDOW_HEIGHT - 192, 10, 3)
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
                        GameEngine._start_player_attack_animation()
                    if event.key == pygame.K_w:
                        GameEngine._handle_player_movement(MapDirection.NORTH)
                    if event.key == pygame.K_a:
                        GameEngine._handle_player_movement(MapDirection.WEST)
                    if event.key == pygame.K_s:
                        GameEngine._handle_player_movement(MapDirection.SOUTH)
                    if event.key == pygame.K_d:
                        GameEngine._handle_player_movement(MapDirection.EAST)
                    if event.key == pygame.K_e:
                        GameEngine._handle_player_interaction()

            GameEngine._handle_enemies_movement()
            GameEngine._handle_enemies_attack()
            GameEngine._handle_peaceful_entities_actions()
            GameEngine._handle_effects()
            GameEngine._handle_missiles()
            GameEngine._handle_enemies_drop()
            GameEngine._handle_level_change()

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

    @staticmethod
    def _handle_player_movement(direction: MapDirection):
        player: Player = GameEngine._player
        player.decrease_invincible_frame()

        player.facing = direction
        if GameEngine._can_entity_move(player) and player.is_alive():
            player.move()

    @staticmethod
    def _can_entity_move(entity: Entity) -> bool:
        pass

    @staticmethod
    def _handle_player_interaction():
        player: Player = GameEngine._player
        for chest in GameEngine._chests:
            if not chest.is_opened and GameEngine._distance(player.x, player.y, chest.x, chest.y) <= 50:
                chest.is_opened = True
                for i, item in enumerate(chest.inventory):
                    if item.item_type == ItemType.COIN:
                        player.add_coin()
                    if item.item_type == ItemType.HEALTH:
                        player.add_health()
                    """czy na pewno chcemy to robić w zależności od pozycji gracza, a nie skrzyni?"""
                    GameEngine._effects.append(ChestOpenEffect(player.x + i*10, player.y - i*10 - 16, item))
                if chest.container_type == ContainerType.STONE_SWORD and not player.has_sword:
                    player.has_sword = True

        for peaceful_entity in GameEngine._peaceful_entities:
            if GameEngine._distance(player.x, player.y, peaceful_entity.x, peaceful_entity.y) <= 50:
                if peaceful_entity.peaceful_entity_type == PeacefulEntityType.DUNGEON_ENTRANCE:
                    GameEngine._handle_enter_dungeon()
            GameEngine._handle_pick_up_items()

    @staticmethod
    def _handle_enemies_movement():
        # TODO animation
        for enemy in GameEngine._hostile_entities:
            enemy.follow_player()
            if GameEngine._can_entity_move(enemy) and not enemy.is_attacking:
                enemy.move()
            else:
                enemy.facing = MapDirection.opposite(enemy.facing)

    @staticmethod
    def _handle_missiles():
        to_remove = []
        for missile in GameEngine._missiles:
            missile.increase_animation_frame()
            if missile.should_animation_end():
                to_remove.append(missile)
            # TODO kolizje
            missile.move()

        for missile in to_remove:
            GameEngine._missiles.remove(missile)

    @staticmethod
    def _handle_enemies_attack():
        for enemy in GameEngine._hostile_entities:
            enemy.decrease_attack_frame()
            if enemy.hostile_entity_type == HostileEntityType.GHOST:
                GameEngine._handle_attack_ghost(enemy)
            # TODO kolizje

    @staticmethod
    def _handle_attack_ghost(ghost: HostileEntity):
        pass

    @staticmethod
    def _handle_peaceful_entities_actions():
        player: Player = GameEngine._player
        for entity in GameEngine._peaceful_entities:
            if entity.peaceful_entity_type == PeacefulEntityType.TREE_OF_HEALTH:
                entity.increase_passive_effect_frame()
                if GameEngine._distance(player.x, player.y, entity.x, entity.y) <= 128 and entity.passive_effect_frame == 100:
                    player.heal(2)

    @staticmethod
    def _handle_effects():
        to_remove = []
        for effect in GameEngine._effects:
            if isinstance(effect, ChestOpenEffect):
                effect.increase_animation_frame()
                effect.move()
                if effect.animation_frame == effect.effect_duration:
                    to_remove.append(effect)
        for effect in to_remove:
            GameEngine._effects.remove(effect)

    @staticmethod
    def _handle_pick_up_items():
        # TODO jak ogarniemy kolizje
        pass

    @staticmethod
    def _handle_player_attack():
        player: Player = GameEngine._player
        if player.attack_frame == 0:
            return
        player.decrease_attack_frame()
        # TODO kolizje

    @staticmethod
    def _start_player_attack_animation():
        if GameEngine._player.attack_frame == 0 and GameEngine._player.has_sword:
            GameEngine._player.attack_frame = 30

    @staticmethod
    def _handle_enemies_drop():
        to_remove = []
        for enemy in GameEngine._hostile_entities:
            if not enemy.is_alive():
                rand = randint(1, 5)
                if rand == 1:
                    GameEngine._items.append(Collectible(enemy.x, enemy.y, ItemType.COIN))
                if rand == 2:
                    GameEngine._items.append(Collectible(enemy.x, enemy.y, ItemType.HEALTH))
                to_remove.append(enemy)
        for enemy in to_remove:
            GameEngine._hostile_entities.remove(enemy)

    @staticmethod
    def _handle_level_change():
        player: Player = GameEngine._player
        if player.x >= MainScreen.WINDOW_WIDTH - 32:
            # TODO
            # GameEngine._current_level = GameEngine._world_map.get_level(GameEngine._current_level.)
            player.x = 1
            # GameEngine._hostile_entities = GameEngine._current_level.
            # GameEngine._peaceful_entities =
            # GameEngine._chests =
            GameEngine._items.clear()
            GameEngine._effects.clear()
            GameEngine._prompts.clear()
            GameEngine._missiles.clear()
        # if

    @staticmethod
    def _handle_enter_dungeon():
        GameEngine._player.y = 0

    @staticmethod
    def start_attack_ghost(enemy: HostileEntity):
        GameEngine._missiles.append(GhostFireball(enemy.x + 16, enemy.y + 16, GameEngine.get_facing_for_aim(enemy)))

    @staticmethod
    def get_facing_for_aim(self, enemy: HostileEntity):
        player: Player = GameEngine._player
        delta_x: int = player.x - enemy.x
        delta_y: int = player.y - enemy.y
        if abs(delta_x) <= abs(delta_y) and delta_y < 0:
            return MapDirection.NORTH
        elif abs(delta_x) <= abs(delta_y) and delta_y > 0:
            return MapDirection.SOUTH
        elif abs(delta_x) > abs(delta_y) and delta_y > 0:
            return MapDirection.EAST
        else:
            return MapDirection.WEST

    # @staticmethod
    # def _start_missile_animation(enemy: HostileEntity):
    #     pass
    #
    # @staticmethod
    # def _handle_missile(enemy: HostileEntity):
    #     pass

    @staticmethod
    def _distance(x1: int, y1: int, x2: int, y2: int) -> int:
        return int(math.sqrt((x2-x1)**2+(y2-y1)**2))










