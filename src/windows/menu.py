import json
import pygame as pg

from src import position
from src.texts import Text, TextCenter, TextGroupMaxSize, TextMaxSize
from src.buttons import Button, ButtonCenter
from src.animation import Animation
from .core import Window


class WindowMenu(Window):
    def __init__(self, core) -> None:
        super().__init__(core)
        self.name_game = TextCenter(
            'Space War', font_size=65,
            pos=position.part(.5, .09), font_color=(0, 0, 0)
        )
        width, height = position.part(.95, .15)
        self.button_start_game = ButtonCenter(
            pos=position.part(.5, .65), width=width, height=height, 
            color_active=(128, 128, 128), color_disabled=(255, 255, 255), 
            text=TextCenter(
                'Старт', font_size=65,
                pos=(width // 2, height // 2), font_color=(0, 0, 0)
            ), 
            func=self.core.set_window_game
        )

        self.name_scores = TextCenter(
            'Очки', font_size=65,
            pos=position.part(.8, .25), font_color=(0, 0, 0)
        )
        self.scores_1 = TextCenter(
            '', font_size=65,
            pos=position.part(.8, .4), font_color=(0, 0, 0)
        )
        self.scores_2 = TextCenter(
            '', font_size=65,
            pos=position.part(.8, .6), font_color=(0, 0, 0)
        )
        self.info_1 = TextCenter(
            '<w> <a> <s> <d> - перемещение', font_size=50,
            pos=position.part(.25, .93), font_color=(0, 0, 0)
        )
        self.info_2 = TextCenter(
            '<space> - огонь', font_size=50,
            pos=position.part(.8, .93), font_color=(0, 0, 0)
        )
        self.animation = Animation(
            pos=position.part(0.03, 0.2), size=position.part(.6, .5),
            core=self.core
        )

        self.update_scores()

    def draw(self) -> None:
        self.surface.fill((100, 100, 100))
        self.name_game.draw(self.surface)
        self.info_1.draw(self.surface)
        self.info_2.draw(self.surface)
        self.name_scores.draw(self.surface)
        self.scores_1.draw(self.surface)
        self.scores_2.draw(self.surface)
        self.button_start_game.draw(self.surface)
        self.animation.draw(self.surface)

    def update_scores(self) -> None:
        with open('scores.json') as file:
            data = json.load(file)
            self.scores_1.set_text(f"Лучшее: {data['max']}")
            self.scores_2.set_text(f"Последнее: {data['last']}")

    def event(self, event: pg.event.Event) -> None:
        self.button_start_game.event(event)
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.core.set_window_pause()

    def update(self) -> None:
        self.animation.update()

