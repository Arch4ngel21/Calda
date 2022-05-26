import pygame
from engine.entities.effects.screen_effect import ScreenEffect
from engine.entities.entity import Entity
from utilities.resource_manager import ResourceManager
from typing import Optional


class ScreenPrompt(ScreenEffect):
    def __init__(self, x: int, y: int, text: str, triggerable: bool, should_show: bool, additional_key=None, triggerable_entity=None):
        super().__init__(x, y, 20)
        self._text = text
        self._triggerable = triggerable
        self._triggerable_entity: Optional[Entity] = triggerable_entity
        self._should_show = should_show
        self._additional_key = additional_key

    def show(self, screen: pygame.Surface, font_game_over: pygame.font.Font, font_prompts: pygame.font.Font):
        if self._should_show:
            if self._text == "Game over":
                screen.blit(font_game_over.render(self._text, False, (255, 255, 255)), (self._x, self._y))
            else:
                if self._additional_key == "E":
                    screen.blit(ResourceManager.key_e, (self._x, self._y))
                    screen.blit(font_prompts.render(self._text, False, (0, 0, 0)), (self._x+28, self._y+5))
                else:
                    screen.blit(font_prompts.render(self._text, False, (0, 0, 0)), (self._x, self._y))



    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value: str):
        self._text = value

    @property
    def triggerable(self):
        return self._triggerable

    @property
    def triggerable_entity(self):
        return self._triggerable_entity

    @property
    def should_show(self):
        return self._should_show

    @should_show.setter
    def should_show(self, value: bool):
        self._should_show = value
