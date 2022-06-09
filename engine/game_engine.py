import math
from random import randint
import sys
import pygame
import os
from typing import List, Optional

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
from engine.entities.effects.fade_out_effect import FadeOutEffect
from engine.entities.effects.chest_open_effect import ChestOpenEffect
from engine.world.map import Map
from engine.world.level_map import LevelMap
from utilities.map_direction import MapDirection
from utilities.resource_manager import ResourceManager
from utilities.exceptions import WrongMapDirection, KeyCodeError
from utilities.settings import Settings
from engine.entities.player import Player
from gui.main_screen import MainScreen


class GameEngine:
    _initialized = False

    _keys = [False for _ in range(123)]  # tablica przycisków
    _player: Player = None
    _hostile_entities: List[HostileEntity] = []
    _peaceful_entities: List[PeacefulEntity] = []
    _chests: List[Container] = []
    _items: List[Collectible] = []
    _missiles: List[Missile] = []
    _effects: List[ScreenEffect] = []
    _prompts: List[ScreenPrompt] = []

    _world_map: Map = None
    _current_level: LevelMap = None
    _clock = None
    _is_running = False

    _font_game_over: Optional[pygame.font.Font] = None
    _font_prompts: Optional[pygame.font.Font] = None

    @staticmethod
    def run():
        GameEngine.start_engine()
        MainScreen.init_screen()
        _clock = pygame.time.Clock()

        while True:
            _clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

                GameEngine._player.is_walking = False
                if event.type == pygame.KEYDOWN:
                    try:
                        GameEngine.press_key(event.key)
                    except KeyCodeError:
                        print("Not accepted key")
                elif event.type == pygame.KEYUP:
                    try:
                        GameEngine.release_key(event.key)
                    except KeyCodeError:
                        print("Not accepted key")

            if GameEngine._is_running:
                GameEngine._handle_key_inputs()
                GameEngine._handle_player_attack()
                GameEngine._handle_player_damaged()
                GameEngine._handle_level_change()
                GameEngine._handle_enemies_movement()
                GameEngine._handle_enemies_attack()
                GameEngine._handle_peaceful_entities_actions()
                GameEngine._handle_missiles()
                GameEngine._handle_enemies_drop()
            GameEngine._handle_effects()
            GameEngine._render_screen()

    @staticmethod
    def start_engine():
        pygame.init()
        GameEngine._player = Player(480, Settings.WINDOW_HEIGHT - 192, 20, 3)
        GameEngine._world_map = Map(Settings.WORLD_MAP_WIDTH, Settings.WORLD_MAP_HEIGHT)
        GameEngine.generate_levels()
        GameEngine._current_level = GameEngine._world_map.get_level(2, 0)
        GameEngine._peaceful_entities = GameEngine._current_level.friendly_entity_list
        GameEngine._hostile_entities = GameEngine._current_level.enemies_list
        GameEngine._is_running = True

        GameEngine._font_game_over = pygame.font.Font(os.path.join("resources", "fonts", "THE_LAST_KINGDOM.ttf"), 86)
        GameEngine._font_prompts = pygame.font.SysFont("helvetica.ttf", 20)

    @staticmethod
    def _render_screen():
        MainScreen.render_map(GameEngine._current_level)
        MainScreen.render_player(GameEngine._player)
        MainScreen.render_enemies(GameEngine._hostile_entities)
        MainScreen.render_missiles(GameEngine._missiles)
        MainScreen.render_collectibles(GameEngine._items)
        MainScreen.render_containers(GameEngine._chests)
        MainScreen.render_hud(GameEngine._player)
        MainScreen.render_debug(GameEngine._player, GameEngine._hostile_entities)
        MainScreen.render_effects(GameEngine._effects, GameEngine._font_game_over, GameEngine._font_prompts)
        pygame.display.flip()

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

        #HostileEntities
        levels[0].add_hostile_entity(HostileEntity(200, Settings.WINDOW_HEIGHT - 200, 10, 1, HostileEntityType.GHOST))
        levels[0].add_hostile_entity(HostileEntity(200, Settings.WINDOW_HEIGHT - 400, 10, 1, HostileEntityType.SLIME))

        # PeacefulEntities
        levels[0].add_peaceful_entity(PeacefulEntity(720, 144, 1, 0, PeacefulEntityType.TREE_OF_HEALTH))

        # Chests
        chest = Container(736, Settings.GAME_WINDOW_HEIGHT - 128, ContainerType.STONE_SWORD)
        levels[1].add_effect(ScreenPrompt(chest.x-32, chest.y-32, "to take the sword", True, False, "E", chest))
        levels[1].add_chest(chest)

        chest = Container(608, Settings.GAME_WINDOW_HEIGHT - 160, ContainerType.CHEST)
        chest.include_item(ItemType.COIN)
        chest.include_item(ItemType.HEALTH)
        levels[3].add_chest(chest)

        chest = Container(704, Settings.GAME_WINDOW_HEIGHT - 192, ContainerType.CHEST)
        chest.include_item(ItemType.COIN)
        levels[4].add_chest(chest)

        chest = Container(704, Settings.GAME_WINDOW_HEIGHT - 544, ContainerType.CHEST)
        chest.include_item(ItemType.COIN)
        levels[11].add_chest(chest)

        chest = Container(32, 32, ContainerType.CHEST)
        chest.include_item(ItemType.COIN)
        levels[9].add_chest(chest)

        chest = Container(192, 96, ContainerType.CHEST)
        chest.include_item(ItemType.COIN)
        levels[17].add_chest(chest)

        chest = Container(416, 96, ContainerType.CHEST)
        chest.include_item(ItemType.COIN)
        levels[17].add_chest(chest)

        chest = Container(640, 96, ContainerType.CHEST)
        chest.include_item(ItemType.COIN)
        levels[17].add_chest(chest)

        chest = Container(128, 128, ContainerType.CHEST)
        chest.include_item(ItemType.COIN)
        levels[12].add_chest(chest)

        chest = Container(800, Settings.GAME_WINDOW_HEIGHT - 160, ContainerType.CHEST)
        chest.include_item(ItemType.COIN)
        levels[13].add_chest(chest)

        # Prompts
        GameEngine._gen_prompts_for_containers(levels)

        for level in levels:
            GameEngine._world_map.add_level(level)

    @staticmethod
    def _gen_prompts_for_containers(levels: List[LevelMap]):
        for level in levels:
            for chest in level.chests:
                if not chest.container_type == ContainerType.STONE_SWORD:
                    level.add_effect(ScreenPrompt(chest.x-32, chest.y-32, "to open chest", True, False, "E", chest))

    @staticmethod
    def _handle_player_movement(direction: MapDirection):
        player: Player = GameEngine._player

        player.facing = direction
        for _ in range(Settings.PLAYER_MOVE_SPEED):
            if GameEngine._can_entity_move(player) and player.is_alive():
                player.move()

    @staticmethod
    def _handle_player_damaged():
        if not GameEngine._player.is_alive() and GameEngine._is_running:
            GameEngine._is_running = False
            GameEngine._effects.append(FadeOutEffect())
            GameEngine._effects.append(ScreenPrompt(400, Settings.GAME_WINDOW_HEIGHT // 2 - 64, "Game over", False, True))

        GameEngine._player.increase_invincible_frame()

    # TODO - jak v2 będzie działać, to tą usuniemy (chyba, że nie będzie xd)
    @staticmethod
    def _can_entity_move(entity: Entity) -> bool:

        # Dla wyszstkich kierunkow tak samo - w odp. ifie potem sie koryguje, jesli bedzie trzeba
        if entity.x % Settings.BLOCK_SIZE == 0:
            block_x = entity.x // Settings.BLOCK_SIZE
        else:
            block_x = (entity.x - (entity.x % Settings.BLOCK_SIZE)) // Settings.BLOCK_SIZE

        if entity.y % Settings.BLOCK_SIZE == 0:
            block_y = entity.y // Settings.BLOCK_SIZE
        else:
            block_y = (entity.y - (entity.y % Settings.BLOCK_SIZE)) // Settings.BLOCK_SIZE

        if entity.facing == MapDirection.NORTH:
            # normalizacja do lewego gornego rogu
            if entity.y == block_y * Settings.BLOCK_SIZE:
                if not GameEngine._current_level.get_block(block_x, block_y - 1).is_passable:
                    return False
                if entity.x % Settings.BLOCK_SIZE != 0 and not GameEngine._current_level.get_block(block_x + 1,
                                                                                                   block_y - 1).is_passable:
                    return False

        elif entity.facing == MapDirection.SOUTH:
            # normalizacja do lewego dolnego rogu
            if entity.y % Settings.BLOCK_SIZE != 0:
                block_y += 1

            if entity.y == block_y * Settings.BLOCK_SIZE:
                if not GameEngine._current_level.get_block(block_x, block_y + 1).is_passable:
                    return False
                if entity.x % Settings.BLOCK_SIZE != 0 and not GameEngine._current_level.get_block(block_x + 1,
                                                                                                   block_y + 1).is_passable:
                    return False

        elif entity.facing == MapDirection.EAST:
            # normalizacja do prawego gornego rogu
            if entity.x % Settings.BLOCK_SIZE != 0:
                block_x += 1

            if entity.x == block_x * Settings.BLOCK_SIZE:
                if not GameEngine._current_level.get_block(block_x + 1, block_y).is_passable:
                    return False
                if entity.y % Settings.BLOCK_SIZE != 0 and not GameEngine._current_level.get_block(block_x + 1,
                                                                                                   block_y + 1).is_passable:
                    return False

        elif entity.facing == MapDirection.WEST:
            # normalizacja do lewego gornego rogu
            if entity.x == block_x * Settings.BLOCK_SIZE:
                if not GameEngine._current_level.get_block(block_x - 1, block_y).is_passable:
                    return False
                if entity.y % Settings.BLOCK_SIZE != 0 and not GameEngine._current_level.get_block(block_x - 1,
                                                                                                   block_y + 1).is_passable:
                    return False

        return True

    # TODO - funkcja do przetestowania czy dziala poprawnie
    #  Robi to samo, co 1 wersja, tylko prosciej.
    @staticmethod
    def _can_entity_move_v2(entity: Entity) -> bool:
        # NORTH - lewy gorny
        # SOUTH - lewy dolny
        # EAST - prawy gorny
        # WEST - lewy gorny

        block_x = entity.x // Settings.BLOCK_SIZE
        block_y = entity.y // Settings.BLOCK_SIZE

        if entity.facing == MapDirection.SOUTH:
            block_y += 1

        if entity.facing == MapDirection.EAST:
            block_x += 1

        if entity.facing == MapDirection.NORTH and entity.y % Settings.BLOCK_SIZE == 0:
            if not GameEngine._current_level.get_block(block_x, block_y - 1).is_passable:
                return False
            if entity.x % Settings.BLOCK_SIZE != 0 and not GameEngine._current_level.get_block(block_x + 1,
                                                                                               block_y - 1).is_passable:
                return False

        elif entity.facing == MapDirection.SOUTH and entity.y % Settings.BLOCK_SIZE == 0:
            if not GameEngine._current_level.get_block(block_x, block_y + 1).is_passable:
                return False
            if entity.x % Settings.BLOCK_SIZE != 0 and not GameEngine._current_level.get_block(block_x + 1,
                                                                                               block_y + 1).is_passable:
                return False

        elif entity.facing == MapDirection.EAST and entity.x % Settings.BLOCK_SIZE == 0:
            if not GameEngine._current_level.get_block(block_x + 1, block_y).is_passable:
                return False
            if entity.y % Settings.BLOCK_SIZE != 0 and not GameEngine._current_level.get_block(block_x + 1,
                                                                                               block_y + 1).is_passable:
                return False

        elif entity.facing == MapDirection.WEST and entity.x % Settings.BLOCK_SIZE == 0:
            if not GameEngine._current_level.get_block(block_x - 1, block_y).is_passable:
                return False
            if entity.y % Settings.BLOCK_SIZE != 0 and not GameEngine._current_level.get_block(block_x - 1,
                                                                                               block_y + 1).is_passable:
                return False

        elif not isinstance(entity.facing, MapDirection):
            print(f"_can_entity_move - given Entity has illegal MapDirection value: {entity.facing}")
            raise WrongMapDirection

        return True

    @staticmethod
    def _handle_key_inputs():

        if GameEngine.is_pressed(pygame.K_q):
            GameEngine._start_player_attack_animation()
        if GameEngine.is_pressed(pygame.K_w):
            GameEngine._handle_player_movement(MapDirection.NORTH)
        if GameEngine.is_pressed(pygame.K_a):
            GameEngine._handle_player_movement(MapDirection.WEST)
        if GameEngine.is_pressed(pygame.K_s):
            GameEngine._handle_player_movement(MapDirection.SOUTH)
        if GameEngine.is_pressed(pygame.K_d):
            GameEngine._handle_player_movement(MapDirection.EAST)
        if GameEngine.is_pressed(pygame.K_e):
            GameEngine._handle_player_interaction()

    @staticmethod
    def _handle_player_interaction():
        player: Player = GameEngine._player
        for chest in GameEngine._chests:
            if not chest.is_opened and GameEngine.distance(player.x, player.y, chest.x, chest.y) <= 50:
                chest.is_opened = True
                chest.update_image()
                for i, item in enumerate(chest.inventory):
                    if item == ItemType.COIN:
                        player.add_coin()
                    if item == ItemType.HEALTH:
                        player.add_health()
                    GameEngine._effects.append(ChestOpenEffect(player.x + i * 10, player.y - i * 10 - 16, item))
                if chest.container_type == ContainerType.STONE_SWORD and not player.has_sword:
                    player.has_sword = True

        for peaceful_entity in GameEngine._peaceful_entities:
            if GameEngine.distance(player.x, player.y, peaceful_entity.x, peaceful_entity.y) <= 50:
                if peaceful_entity.peaceful_entity_type == PeacefulEntityType.DUNGEON_ENTRANCE:
                    GameEngine._handle_enter_dungeon()

        GameEngine._handle_pick_up_items()

    @staticmethod
    def _handle_enemies_movement():
        for enemy in GameEngine._hostile_entities:
            enemy.follow_player(GameEngine._player)
            enemy.increase_animation_frame()
            if GameEngine._can_entity_move(enemy) and not enemy.is_attacking:
                enemy.move()
            else:
                enemy.facing = MapDirection.opposite(enemy.facing)

    @staticmethod
    def _handle_missiles():
        for missile in GameEngine._missiles:
            missile.increase_animation_frame()

            if missile.should_animation_end():
                GameEngine._missiles.remove(missile)

            if not GameEngine._player.is_damaged and missile.bounding_box.colliderect(GameEngine._player.hit_box):
                GameEngine._player.damage(missile.damage)
                GameEngine._player.is_damaged = True
                GameEngine._missiles.remove(missile)

            missile.move()

    @staticmethod
    def _handle_enemies_attack():
        for enemy in GameEngine._hostile_entities:
            if enemy.is_attacking:
                enemy.decrease_attack_frame()

            if enemy.hostile_entity_type == HostileEntityType.GHOST:
                GameEngine._handle_attack_ghost(enemy)

            if not enemy.is_attacking and enemy.bounding_box.colliderect(
                    GameEngine._player.hit_box) and not GameEngine._player.is_damaged and GameEngine._player.is_alive():
                enemy.set_attack_frame(45)
                GameEngine._player.damage(enemy.attack_damage)
                GameEngine._player.is_damaged = True

    @staticmethod
    def _handle_attack_ghost(ghost: HostileEntity):
        if not ghost.is_attacking and ghost.is_following and abs(GameEngine._player.y - ghost.y) <= 3 or abs(GameEngine._player.x - ghost.x) <= 3:
            ghost.set_attack_frame(50)
            ghost.is_attacking = True

        if ghost.attack_frame == 20:
            GameEngine.start_attack_ghost(ghost)

    @staticmethod
    def _handle_peaceful_entities_actions():
        player: Player = GameEngine._player
        for entity in GameEngine._peaceful_entities:
            if entity.peaceful_entity_type == PeacefulEntityType.TREE_OF_HEALTH:
                entity.increase_passive_effect_frame()
                if GameEngine.distance(player.x, player.y, entity.x,
                                       entity.y) <= 128 and entity.passive_effect_frame == 100:
                    player.heal(2)

    @staticmethod
    def _handle_effects():
        to_remove = []
        for effect in GameEngine._effects:
            if isinstance(effect, ChestOpenEffect):
                effect.increase_animation_frame()
                effect.update_image()
                effect.move()
                if effect.animation_frame == effect.effect_duration:
                    to_remove.append(effect)

            elif isinstance(effect, ScreenPrompt):
                if effect.triggerable:
                    if GameEngine.distance(GameEngine._player.x, GameEngine._player.y, effect.triggerable_entity.x, effect.triggerable_entity.y) <= 50:
                        if isinstance(effect.triggerable_entity, Container):
                            if not effect.triggerable_entity.is_opened:
                                effect.should_show = True
                            else:
                                effect.should_show = False
                        else:
                            effect.should_show = False
                    else:
                        effect.should_show = False

            elif isinstance(effect, FadeOutEffect):
                effect.increase_animation_frame()

        for effect in to_remove:
            GameEngine._effects.remove(effect)

    @staticmethod
    def _handle_pick_up_items():
        to_remove = []
        for item in GameEngine._items:
            if item.bounding_box.colliderect(GameEngine._player.hit_box):
                if item.item_type == ItemType.COIN:
                    GameEngine._player.add_coin()
                if item.item_type == ItemType.HEALTH:
                    GameEngine._player.add_max_health()
                to_remove.append(item)
        for item in to_remove:
            GameEngine._items.remove(item)

    @staticmethod
    def _handle_player_attack():
        player: Player = GameEngine._player
        if player.attack_frame == 0:
            return
        should_damage = player.increase_attack_frame()
        if not should_damage:
            return
        for enemy in GameEngine._hostile_entities:
            if player.bounding_box.colliderect(enemy.hit_box):
                enemy.damage(player.attack_damage)

    @staticmethod
    def _start_player_attack_animation():
        if GameEngine._player.attack_frame == 0 and GameEngine._player.has_sword:
            GameEngine._player.attack_frame = 1

    @staticmethod
    def _handle_enemies_drop():
        to_remove = []
        for enemy in GameEngine._hostile_entities:
            if not enemy.is_alive():
                rand = randint(1, 3)
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

        if player.x >= Settings.GAME_WINDOW_WIDTH - player._hit_box.width:
            GameEngine._current_level = GameEngine._world_map.get_level(GameEngine._current_level.world_map_x + 1,
                                                                        GameEngine._current_level.world_map_y)
            player.x = 1
            GameEngine._hostile_entities = GameEngine._current_level.enemies_list
            GameEngine._peaceful_entities = GameEngine._current_level.friendly_entity_list
            GameEngine._chests = GameEngine._current_level.chests
            GameEngine._effects = GameEngine._current_level.effects
            GameEngine._items.clear()
            GameEngine._prompts.clear()
            GameEngine._missiles.clear()

        elif player.x <= 0:
            GameEngine._current_level = GameEngine._world_map.get_level(GameEngine._current_level.world_map_x - 1,
                                                                        GameEngine._current_level.world_map_y)
            player.x = Settings.GAME_WINDOW_WIDTH - player._hit_box.width
            GameEngine._hostile_entities = GameEngine._current_level.enemies_list
            GameEngine._peaceful_entities = GameEngine._current_level.friendly_entity_list
            GameEngine._chests = GameEngine._current_level.chests
            GameEngine._items.clear()
            GameEngine._effects.clear()
            GameEngine._prompts.clear()
            GameEngine._missiles.clear()

        elif player.y >= Settings.GAME_WINDOW_HEIGHT - player._hit_box.height:
            GameEngine._current_level = GameEngine._world_map.get_level(GameEngine._current_level.world_map_x,
                                                                        GameEngine._current_level.world_map_y - 1)
            player.y = 1
            GameEngine._hostile_entities = GameEngine._current_level.enemies_list
            GameEngine._peaceful_entities = GameEngine._current_level.friendly_entity_list
            GameEngine._chests = GameEngine._current_level.chests
            GameEngine._items.clear()
            GameEngine._effects.clear()
            GameEngine._prompts.clear()
            GameEngine._missiles.clear()

        elif player.y <= 0:
            GameEngine._current_level = GameEngine._world_map.get_level(GameEngine._current_level.world_map_x,
                                                                        GameEngine._current_level.world_map_y + 1)
            player.y = Settings.GAME_WINDOW_HEIGHT - player._hit_box.height
            GameEngine._hostile_entities = GameEngine._current_level.enemies_list
            GameEngine._peaceful_entities = GameEngine._current_level.friendly_entity_list
            GameEngine._chests = GameEngine._current_level.chests
            GameEngine._items.clear()
            GameEngine._effects.clear()
            GameEngine._prompts.clear()
            GameEngine._missiles.clear()

    @staticmethod
    def _handle_enter_dungeon():
        # TODO - brzydkie rozwiazanie tego problemu
        #  (gracz pojawia sie na granicy mapy, przez co teleportuje go na kolejny poziom)
        #  dziala, ale mozna to poprawic
        GameEngine._player.y = 0

    @staticmethod
    def start_attack_ghost(enemy: HostileEntity):
        GameEngine._missiles.append(GhostFireball(enemy.x + 16, enemy.y + 16, GameEngine.get_facing_for_aim(enemy)))

    @staticmethod
    def get_facing_for_aim(enemy: HostileEntity):
        player: Player = GameEngine._player
        delta_x: int = player.x - enemy.x
        delta_y: int = player.y - enemy.y
        if abs(delta_x) <= abs(delta_y) and delta_y < 0:
            return MapDirection.NORTH
        elif abs(delta_x) <= abs(delta_y) and delta_y > 0:
            return MapDirection.SOUTH
        elif abs(delta_x) > abs(delta_y) and delta_x > 0:
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
    def distance(x1: int, y1: int, x2: int, y2: int) -> int:
        return int(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2))

    @staticmethod
    def press_key(key_code: int):
        if key_code > 122:
            raise KeyCodeError
        GameEngine._keys[key_code] = True

    @staticmethod
    def release_key(key_code: int):
        if key_code > 122:
            raise KeyCodeError
        GameEngine._keys[key_code] = False

    @staticmethod
    def is_pressed(key_code: int):
        if key_code > 122:
            raise KeyCodeError
        return GameEngine._keys[key_code]
