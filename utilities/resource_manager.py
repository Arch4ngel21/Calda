
from PIL import Image
import pygame


class ResourceManager:
    level_2_0 = Image.open(r"./resources/maps/2_0.png")
    level_3_0 = Image.open(r"./resources/maps/3_0.png")
    level_2_1 = Image.open(r"./resources/maps/2_1.png")
    level_3_1 = Image.open(r"./resources/maps/3_1.png")
    level_4_1 = Image.open(r"./resources/maps/4_1.png")
    level_0_2 = Image.open(r"./resources/maps/0_2.png")
    level_1_2 = Image.open(r"./resources/maps/1_2.png")
    level_4_2 = Image.open(r"./resources/maps/4_2.png")
    level_0_3 = Image.open(r"./resources/maps/0_3.png")
    level_1_3 = Image.open(r"./resources/maps/1_3.png")
    level_2_3 = Image.open(r"./resources/maps/2_3.png")
    level_3_3 = Image.open(r"./resources/maps/3_3.png")
    level_4_3 = Image.open(r"./resources/maps/4_3.png")
    level_0_4 = Image.open(r"./resources/maps/0_4.png")
    level_1_4 = Image.open(r"./resources/maps/1_4.png")
    level_2_4 = Image.open(r"./resources/maps/2_4.png")
    level_3_4 = Image.open(r"./resources/maps/3_4.png")
    level_4_4 = Image.open(r"./resources/maps/4_4.png")

    # pierwsze 3 rzędy dla stania, kolejne 3 dla chodzenia
    # [kierunek dla stania | kierunek dla chodzenia + 3] [has_sword] [1/2 klatka]
    player_movement = [[[None for _ in range(2)] for _ in range(2)] for _ in range(6)]

    # [kierunek] [1/2/3 klatka]
    player_attack = [[None for _ in range(3)] for _ in range(3)]

    bricks_1 = pygame.image.load(r"./resources/tiles/bricks1.png")
    bricks_2 = pygame.image.load(r"./resources/tiles/bricks2.png")
    bricks_3 = pygame.image.load(r"./resources/tiles/bricks3.png")
    bricks_4 = pygame.image.load(r"./resources/tiles/bricks4.png")

    cobblestone = pygame.image.load(r"./resources/tiles/cobblestone.png")

    tree_down = pygame.image.load(r"./resources/tiles/tree_down.png")
    tree_up = pygame.image.load(r"./resources/tiles/tree_up.png")

    dungeon_bricks_1 = pygame.image.load(r"./resources/tiles/dungeon_bricks1.png")
    dungeon_bricks_2 = pygame.image.load(r"./resources/tiles/dungeon_bricks2.png")
    dungeon_bricks_3 = pygame.image.load(r"./resources/tiles/dungeon_bricks3.png")
    dungeon_bricks_4 = pygame.image.load(r"./resources/tiles/dungeon_bricks4.png")

    dungeon_floor_1 = pygame.image.load(r"./resources/tiles/dungeon_floor1.png")
    dungeon_floor_2 = pygame.image.load(r"./resources/tiles/dungeon_floor2.png")
    dungeon_floor_3 = pygame.image.load(r"./resources/tiles/dungeon_floor3.png")
    dungeon_floor_4 = pygame.image.load(r"./resources/tiles/dungeon_floor4.png")
    dungeon_floor_5 = pygame.image.load(r"./resources/tiles/dungeon_floor5.png")

    dungeon_entrance = pygame.image.load(r"./resources/tiles/dungeon_entrance.png")

    dungeon_entrance_left = pygame.image.load(r"./resources/tiles/dungeon_entrance_left.png")
    dungeon_entrance_right = pygame.image.load(r"./resources/tiles/dungeon_entrance_right.png")

    grass_1 = pygame.image.load(r"./resources/tiles/grass1.png")
    grass_2 = pygame.image.load(r"./resources/tiles/grass2.png")
    grass_3 = pygame.image.load(r"./resources/tiles/grass3.png")
    grass_4 = pygame.image.load(r"./resources/tiles/grass4.png")

    bush = pygame.image.load(r"./resources/tiles/bush.png")

    path_1 = pygame.image.load(r"./resources/tiles/path1.png")
    path_2 = pygame.image.load(r"./resources/tiles/path2.png")
    path_3 = pygame.image.load(r"./resources/tiles/path3.png")
    path_4 = pygame.image.load(r"./resources/tiles/path4.png")

    water_1 = pygame.image.load(r"./resources/tiles/water1.png")
    water_2 = pygame.image.load(r"./resources/tiles/water2.png")
    water_3 = pygame.image.load(r"./resources/tiles/water3.png")
    water_4 = pygame.image.load(r"./resources/tiles/water4.png")

    chest_closed = pygame.image.load(r"./resources/tiles/chest_closed.png")
    chest_opened = pygame.image.load(r"./resources/tiles/chest_opened.png")

    sign = pygame.image.load(r"./resources/tiles/sign.png")
    stone_with_sword = pygame.image.load(r"./resources/tiles/stone_with_sword.png")
    stone_without_sword = pygame.image.load(r"./resources/tiles/stone_without_sword.png")

    campfire_dungeon_1 = pygame.image.load(r"./resources/tiles/campfire_dungeon_1.png")
    campfire_dungeon_2 = pygame.image.load(r"./resources/tiles/campfire_dungeon_2.png")
    campfire_dungeon_3 = pygame.image.load(r"./resources/tiles/campfire_dungeon_3.png")
    campfire_dungeon_4 = pygame.image.load(r"./resources/tiles/campfire_dungeon_4.png")
    campfire_dungeon_5 = pygame.image.load(r"./resources/tiles/campfire_dungeon_5.png")
    campfire_dungeon_6 = pygame.image.load(r"./resources/tiles/campfire_dungeon_6.png")
    campfire_dungeon_7 = pygame.image.load(r"./resources/tiles/campfire_dungeon_7.png")
    campfire_dungeon_8 = pygame.image.load(r"./resources/tiles/campfire_dungeon_8.png")

    campfire_outside_1 = pygame.image.load(r"./resources/tiles/campfire_outside_1.png")
    campfire_outside_2 = pygame.image.load(r"./resources/tiles/campfire_outside_2.png")
    campfire_outside_3 = pygame.image.load(r"./resources/tiles/campfire_outside_3.png")
    campfire_outside_4 = pygame.image.load(r"./resources/tiles/campfire_outside_4.png")
    campfire_outside_5 = pygame.image.load(r"./resources/tiles/campfire_outside_5.png")
    campfire_outside_6 = pygame.image.load(r"./resources/tiles/campfire_outside_6.png")
    campfire_outside_7 = pygame.image.load(r"./resources/tiles/campfire_outside_7.png")
    campfire_outside_8 = pygame.image.load(r"./resources/tiles/campfire_outside_8.png")

    healing_effect_1 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_1.png")
    healing_effect_2 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_2.png")
    healing_effect_3 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_3.png")
    healing_effect_4 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_4.png")
    healing_effect_5 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_5.png")
    healing_effect_6 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_6.png")
    healing_effect_7 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_7.png")
    healing_effect_8 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_8.png")
    healing_effect_9 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_9.png")
    healing_effect_10 = pygame.image.load(r"./resources/tiles/healing_effect/healing_effect_10.png")

    portal_1 = pygame.image.load(r"./resources/tiles/portal_1.png")
    portal_2 = pygame.image.load(r"./resources/tiles/portal_2.png")
    portal_3 = pygame.image.load(r"./resources/tiles/portal_3.png")
    portal_4 = pygame.image.load(r"./resources/tiles/portal_4.png")
    portal_5 = pygame.image.load(r"./resources/tiles/portal_5.png")
    portal_6 = pygame.image.load(r"./resources/tiles/portal_6.png")
    portal_7 = pygame.image.load(r"./resources/tiles/portal_7.png")
    portal_8 = pygame.image.load(r"./resources/tiles/portal_8.png")

    player_movement[1][0][0] = player_standing_left_1 = pygame.image.load(r"./resources/entities/player_standing_left_1.png")
    player_movement[1][0][1] = player_standing_left_2 = pygame.image.load(r"./resources/entities/player_standing_left_2.png")
    player_movement[1][1][0] = player_standing_left_sword_1 = pygame.image.load(r"./resources/entities/player_standing_left_sword_1.png")
    player_movement[1][1][1] = player_standing_left_sword_2 = pygame.image.load(r"./resources/entities/player_standing_left_sword_2.png")

    player_movement[2][0][0] = player_standing_front_1 = pygame.image.load(r"./resources/entities/player_standing_front_1.png")
    player_movement[2][0][1] = player_standing_front_2 = pygame.image.load(r"./resources/entities/player_standing_front_2.png")
    player_movement[2][1][0] = player_standing_front_sword_1 = pygame.image.load(r"./resources/entities/player_standing_front_sword_1.png")
    player_movement[2][1][1] = player_standing_front_sword_2 = pygame.image.load(r"./resources/entities/player_standing_front_sword_2.png")

    player_movement[0][0][0] = player_standing_back_1 = pygame.image.load(r"./resources/entities/player_standing_back_1.png")
    player_movement[0][0][1] = player_standing_back_2 = pygame.image.load(r"./resources/entities/player_standing_back_2.png")
    player_movement[0][1][0] = player_standing_back_sword_1 = pygame.image.load(r"./resources/entities/player_standing_back_sword_1.png")
    player_movement[0][1][1] = player_standing_back_sword_2 = pygame.image.load(r"./resources/entities/player_standing_back_sword_2.png")

    player_movement[4][0][0] = player_walking_left_1 = pygame.image.load(r"./resources/entities/player_walking_left_1.png")
    player_movement[4][0][1] = player_walking_left_2 = pygame.image.load(r"./resources/entities/player_walking_left_2.png")
    player_movement[4][1][0] = player_walking_left_sword_1 = pygame.image.load(r"./resources/entities/player_walking_left_sword_1.png")
    player_movement[4][1][1] = player_walking_left_sword_2 = pygame.image.load(r"./resources/entities/player_walking_left_sword_2.png")

    player_movement[5][0][0] = player_walking_front_1 = pygame.image.load(r"./resources/entities/player_walking_front_1.png")
    player_movement[5][0][1] = player_walking_front_2 = pygame.image.load(r"./resources/entities/player_walking_front_2.png")
    player_movement[5][1][0] = player_walking_front_sword_1 = pygame.image.load(r"./resources/entities/player_walking_front_sword_1.png")
    player_movement[5][1][1] = player_walking_front_sword_2 = pygame.image.load(r"./resources/entities/player_walking_front_sword_2.png")

    player_movement[3][0][0] = player_walking_back_1 = pygame.image.load(r"./resources/entities/player_walking_back_1.png")
    player_movement[3][0][1] = player_walking_back_2 = pygame.image.load(r"./resources/entities/player_walking_back_2.png")
    player_movement[3][1][0] = player_walking_back_sword_1 = pygame.image.load(r"./resources/entities/player_walking_back_sword_1.png")
    player_movement[3][1][1] = player_walking_back_sword_2 = pygame.image.load(r"./resources/entities/player_walking_back_sword_2.png")

    player_attack[1][0] = player_attack_left_1 = pygame.image.load(r"./resources/entities/player_attack_left_1.png")
    player_attack[1][1] = player_attack_left_2 = pygame.image.load(r"./resources/entities/player_attack_left_2.png")
    player_attack[1][2] = player_attack_left_3 = pygame.image.load(r"./resources/entities/player_attack_left_3.png")

    player_attack[2][0] = player_attack_front_1 = pygame.image.load(r"./resources/entities/player_attack_front_1.png")
    player_attack[2][1] = player_attack_front_2 = pygame.image.load(r"./resources/entities/player_attack_front_2.png")
    player_attack[2][2] = player_attack_front_3 = pygame.image.load(r"./resources/entities/player_attack_front_3.png")

    player_attack[0][0] = player_attack_back_1 = pygame.image.load(r"./resources/entities/player_attack_back_1.png")
    player_attack[0][1] = player_attack_back_2 = pygame.image.load(r"./resources/entities/player_attack_back_2.png")
    player_attack[0][2] = player_attack_back_3 = pygame.image.load(r"./resources/entities/player_attack_back_3.png")

    ghost_moving_1 = pygame.image.load(r"./resources/entities/ghost_moving_1.png")
    ghost_moving_2 = pygame.image.load(r"./resources/entities/ghost_moving_2.png")
    ghost_moving_3 = pygame.image.load(r"./resources/entities/ghost_moving_3.png")
    ghost_moving_4 = pygame.image.load(r"./resources/entities/ghost_moving_4.png")
    ghost_moving_5 = pygame.image.load(r"./resources/entities/ghost_moving_5.png")
    ghost_moving_6 = pygame.image.load(r"./resources/entities/ghost_moving_6.png")
    ghost_moving_7 = pygame.image.load(r"./resources/entities/ghost_moving_7.png")
    ghost_moving_8 = pygame.image.load(r"./resources/entities/ghost_moving_8.png")

    ghost_attack_1 = pygame.image.load(r"./resources/entities/ghost_attack_1.png")
    ghost_attack_2 = pygame.image.load(r"./resources/entities/ghost_attack_2.png")
    ghost_attack_3 = pygame.image.load(r"./resources/entities/ghost_attack_3.png")
    ghost_attack_4 = pygame.image.load(r"./resources/entities/ghost_attack_4.png")
    ghost_attack_5 = pygame.image.load(r"./resources/entities/ghost_attack_5.png")

    ghost_fireball_1 = pygame.image.load(r"./resources/entities/ghost_fireball_1.png")
    ghost_fireball_2 = pygame.image.load(r"./resources/entities/ghost_fireball_2.png")
    ghost_fireball_3 = pygame.image.load(r"./resources/entities/ghost_fireball_3.png")

    slime_standing_1 = pygame.image.load(r"./resources/entities/slime_standing_1.png")
    slime_standing_2 = pygame.image.load(r"./resources/entities/slime_standing_2.png")
    slime_standing_3 = pygame.image.load(r"./resources/entities/slime_standing_3.png")
    slime_standing_4 = pygame.image.load(r"./resources/entities/slime_standing_4.png")
    slime_standing_5 = pygame.image.load(r"./resources/entities/slime_standing_5.png")
    slime_standing_6 = pygame.image.load(r"./resources/entities/slime_standing_6.png")
    slime_standing_7 = pygame.image.load(r"./resources/entities/slime_standing_7.png")

    slime_jumping_1 = pygame.image.load(r"./resources/entities/slime_jump_1.png")
    slime_jumping_2 = pygame.image.load(r"./resources/entities/slime_jump_2.png")
    slime_jumping_3 = pygame.image.load(r"./resources/entities/slime_jump_3.png")
    slime_jumping_4 = pygame.image.load(r"./resources/entities/slime_jump_4.png")
    slime_jumping_5 = pygame.image.load(r"./resources/entities/slime_jump_5.png")
    slime_jumping_6 = pygame.image.load(r"./resources/entities/slime_jump_6.png")
    slime_jumping_7 = pygame.image.load(r"./resources/entities/slime_jump_7.png")

    coin = pygame.image.load(r"./resources/icons/coin.png")
    plus_coin = pygame.image.load(r"./resources/icons/plus_coin.png")

    heart_0 = pygame.image.load(r"./resources/icons/heart_0.png")
    heart_1 = pygame.image.load(r"./resources/icons/heart_1.png")
    heart_2 = pygame.image.load(r"./resources/icons/heart_2.png")
    heart_3 = pygame.image.load(r"./resources/icons/heart_3.png")
    heart_4 = pygame.image.load(r"./resources/icons/heart_4.png")
    heart_5 = pygame.image.load(r"./resources/icons/heart_5.png")
    plus_heart = pygame.image.load(r"./resources/icons/plus_heart.png")
    gold_heart = pygame.image.load(r"./resources/icons/heart_gold_1.png")

    blank = pygame.image.load(r"./resources/tiles/blank.png")
    piksel = pygame.image.load(r"./resources/tiles/piksel.png")

    key_e = pygame.image.load(r"./resources/icons/key_E.png")

    def __init__(self):
        pass

    # TODO - funkcja dajaca lustrzne odbicie obrazu

