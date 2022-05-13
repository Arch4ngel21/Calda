import pygame

from engine.entities.player import Player
from engine.world.level_map import LevelMap
from utilities.resource_manager import ResourceManager
from utilities.settings import Settings
from utilities.map_direction import MapDirection


class MainScreen:
    screen: pygame.Surface = None

    @staticmethod
    def init_screen():
        pygame.init()
        MainScreen.screen = pygame.display.set_mode((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT))

    @staticmethod
    def render_map(curr_level: LevelMap):

        for y in range(curr_level.level_map_height):
            for x in range(curr_level.level_map_width):
                back_image = None
                block_image = None

                if curr_level.get_block(x, y).block_name == "bricks1":
                    block_image = ResourceManager.bricks_1
                elif curr_level.get_block(x, y).block_name == "bricks2":
                    block_image = ResourceManager.bricks_2
                elif curr_level.get_block(x, y).block_name == "bricks3":
                    block_image = ResourceManager.bricks_3
                elif curr_level.get_block(x, y).block_name == "bricks4":
                    block_image = ResourceManager.bricks_4

                elif curr_level.get_block(x, y).block_name == "cobblestone":
                    block_image = ResourceManager.cobblestone

                elif curr_level.get_block(x, y).block_name == "dungeon_bricks1":
                    block_image = ResourceManager.dungeon_bricks_1
                elif curr_level.get_block(x, y).block_name == "dungeon_bricks2":
                    block_image = ResourceManager.dungeon_bricks_2
                elif curr_level.get_block(x, y).block_name == "dungeon_bricks3":
                    block_image = ResourceManager.dungeon_bricks_3
                elif curr_level.get_block(x, y).block_name == "dungeon_bricks4":
                    block_image = ResourceManager.dungeon_bricks_4

                elif curr_level.get_block(x, y).block_name == "dungeon_floor1":
                    block_image = ResourceManager.dungeon_floor_1
                elif curr_level.get_block(x, y).block_name == "dungeon_floor2":
                    block_image = ResourceManager.dungeon_floor_2
                elif curr_level.get_block(x, y).block_name == "dungeon_floor3":
                    block_image = ResourceManager.dungeon_floor_3
                elif curr_level.get_block(x, y).block_name == "dungeon_floor4":
                    block_image = ResourceManager.dungeon_floor_4
                elif curr_level.get_block(x, y).block_name == "dungeon_floor5":
                    block_image = ResourceManager.dungeon_floor_5

                elif curr_level.get_block(x, y).block_name == "grass1":
                    block_image = ResourceManager.grass_1
                elif curr_level.get_block(x, y).block_name == "grass2":
                    block_image = ResourceManager.grass_2
                elif curr_level.get_block(x, y).block_name == "grass3":
                    block_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "grass4":
                    block_image = ResourceManager.grass_4
                elif curr_level.get_block(x, y).block_name == "bush":
                    block_image = ResourceManager.bush
                    back_image = ResourceManager.grass_2

                elif curr_level.get_block(x, y).block_name == "water":
                    block_image = ResourceManager.water_4

                elif curr_level.get_block(x, y).block_name == "tree_bottom":
                    block_image = ResourceManager.tree_down
                    back_image = ResourceManager.grass_1
                elif curr_level.get_block(x, y).block_name == "tree_up":
                    block_image = ResourceManager.tree_up
                    back_image = ResourceManager.grass_1

                elif curr_level.get_block(x, y).block_name == "path_center":
                    block_image = ResourceManager.path_1
                elif curr_level.get_block(x, y).block_name == "path_straight_up":
                    block_image = ResourceManager.path_3
                    block_image = pygame.transform.rotate(block_image, 90)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "path_straight_down":
                    block_image = ResourceManager.path_3
                    block_image = pygame.transform.rotate(block_image, 270)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "path_straight_left":
                    block_image = ResourceManager.path_3
                    block_image = pygame.transform.rotate(block_image, 180)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "path_straight_right":
                    block_image = ResourceManager.path_3
                    back_image = ResourceManager.grass_3

                elif curr_level.get_block(x, y).block_name == "path_corner_left_down":
                    block_image = ResourceManager.path_4
                    block_image = pygame.transform.rotate(block_image, 270)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "path_corner_left_up":
                    block_image = ResourceManager.path_4
                    block_image = pygame.transform.rotate(block_image, 180)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "path_corner_right_up":
                    block_image = ResourceManager.path_4
                    block_image = pygame.transform.rotate(block_image, 90)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "path_corner_right_down":
                    block_image = ResourceManager.path_4
                    back_image = ResourceManager.grass_3

                elif curr_level.get_block(x, y).block_name == "path_turn_left_down":
                    block_image = ResourceManager.path_2
                    block_image = pygame.transform.rotate(block_image, 270)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "path_turn_left_up":
                    block_image = ResourceManager.path_2
                    block_image = pygame.transform.rotate(block_image, 180)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "path_turn_right_up":
                    block_image = ResourceManager.path_2
                    block_image = pygame.transform.rotate(block_image, 90)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "path_turn_right_down":
                    block_image = ResourceManager.path_2
                    back_image = ResourceManager.grass_3

                elif curr_level.get_block(x, y).block_name == "shore_center":
                    block_image = ResourceManager.water_4
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_straight_up":
                    block_image = ResourceManager.water_2
                    block_image = pygame.transform.rotate(block_image, 90)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_straight_down":
                    block_image = ResourceManager.water_2
                    block_image = pygame.transform.rotate(block_image, 270)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_straight_left":
                    block_image = ResourceManager.water_2
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_straight_right":
                    block_image = ResourceManager.water_2
                    block_image = pygame.transform.rotate(block_image, 180)
                    back_image = ResourceManager.grass_3

                elif curr_level.get_block(x, y).block_name == "shore_corner_left_down":
                    block_image = ResourceManager.water_1
                    block_image = pygame.transform.rotate(block_image, 90)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_corner_left_up":
                    block_image = ResourceManager.water_1
                    block_image = pygame.transform.rotate(block_image, 180)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_corner_right_up":
                    block_image = ResourceManager.water_1
                    block_image = pygame.transform.rotate(block_image, 270)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_corner_right_down":
                    block_image = ResourceManager.water_1
                    back_image = ResourceManager.grass_3

                elif curr_level.get_block(x, y).block_name == "shore_turn_left_down":
                    block_image = ResourceManager.water_3
                    block_image = pygame.transform.rotate(block_image, 90)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_turn_left_up":
                    block_image = ResourceManager.water_3
                    block_image = pygame.transform.rotate(block_image, 180)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_turn_right_up":
                    block_image = ResourceManager.water_3
                    block_image = pygame.transform.rotate(block_image, 270)
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "shore_turn_right_down":
                    block_image = ResourceManager.water_3
                    back_image = ResourceManager.grass_3
                elif curr_level.get_block(x, y).block_name == "campfire":
                    block_image = ResourceManager.blank
                elif curr_level.get_block(x, y).block_name == "sign":
                    block_image = ResourceManager.sign
                    back_image = ResourceManager.path_1
                elif curr_level.get_block(x, y).block_name == "sword_stone":
                    # TODO - to do usunięcia, jak się zrobi resztę Entity; miecz jest przyjaznym NPC
                    block_image = ResourceManager.stone_with_sword
                    back_image = ResourceManager.grass_1
                elif curr_level.get_block(x, y).block_name == "dungeon_entrance_left":
                    block_image = ResourceManager.dungeon_entrance_left
                    back_image = ResourceManager.cobblestone
                elif curr_level.get_block(x, y).block_name == "dungeon_entrance_right":
                    block_image = ResourceManager.dungeon_entrance_right
                    back_image = ResourceManager.cobblestone
                elif curr_level.get_block(x, y).block_name == "error_block":
                    block_image = ResourceManager.blank
                else:
                    print(f"Error in block: x: {x}, y: {y}")
                    block_image = ResourceManager.blank

                if back_image:
                    MainScreen.screen.blit(back_image, (x * Settings.BLOCK_SIZE, y * Settings.BLOCK_SIZE))
                MainScreen.screen.blit(block_image, (x * Settings.BLOCK_SIZE, y * Settings.BLOCK_SIZE))

    @staticmethod
    def render_player(player: Player):
        player.draw(MainScreen.screen)

    @staticmethod
    def render_debug(player: Player):
        MainScreen.screen.blit(ResourceManager.piksel, player._hit_box)
        pygame.draw.rect(MainScreen.screen, (0, 0, 255), (player._hit_box.x, player._hit_box.y, player._hit_box.width, player._hit_box.height), 1)
        pygame.draw.rect(MainScreen.screen, (255, 0, 0), (player._bounding_box.x, player._bounding_box.y, player._bounding_box.width, player._bounding_box.height), 1)


