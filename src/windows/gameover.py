import pygame as pg

from src import position
from src.texts import Text, TextCenter
from src.buttons import Button, ButtonCenter
from .core import Window


class WindowGameOver(Window):
    def __init__(self, core) -> None:
        super().__init__(core)
        self.name_game = TextCenter(
            'Вы проиграли', font_size=65,
            pos=position.part(.5, .35), font_color=(0, 0, 0)
        )
        self.scores = TextCenter(
            f'Счёт: 0', font_size=65,
            pos=position.part(.5, .5), font_color=(0, 0, 0)
        )
        width, height = position.part(.4, .15)
        self.button_start_game = ButtonCenter(
            pos=position.part(.5, .55), width=width, height=height, 
            color_active=(128, 128, 128), color_disabled=(255, 255, 255), 
            text=TextCenter(
                'Новая игра', font_size=65,
                pos=(width // 2, height // 2), font_color=(0, 0, 0)
            ), 
            func=self.core.set_window_game
        )

    def set_scores(self, scores: int):
        self.scores.set_text(f'Счёт: {scores}')

    def draw(self) -> None:
        self.surface.fill((100, 100, 100))
        self.name_game.draw(self.surface)
        self.scores.draw(self.surface)
        self.button_start_game.draw(self.surface)

    def event(self, event: pg.event.Event) -> None:
        self.button_start_game.event(event)

    def update(self) -> None:
        pass

