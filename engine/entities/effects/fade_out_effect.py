import pygame
from engine.entities.effects.screen_effect import ScreenEffect
from utilities.settings import Settings


class FadeOutEffect(ScreenEffect):
    def __init__(self):
        super().__init__(0, 0, 200)
        self._rect = pygame.Surface((Settings.WINDOW_WIDTH, Settings.WINDOW_HEIGHT), pygame.SRCALPHA)

    def draw(self, screen: pygame.Surface):
        alpha = int((self._animation_frame / 200.0) * 255)
        self._rect.fill((0, 0, 0, alpha))
        screen.blit(self._rect, (0, 0))
