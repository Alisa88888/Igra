import pygame as pg

from src import position
from src.texts import Text, TextCenter
from src.buttons import Button, ButtonCenter
from src.slider import Slider
from .core import Window


class WindowPause(Window):
    def __init__(self, core) -> None:
        super().__init__(core)
        self.text_pause = TextCenter(
            'Пауза', font_size=65,
            pos=position.part(.5, .1), font_color=(0, 0, 0)
        )
        width, height = position.part(.4, .15)
        self.text_sound = TextCenter(
            'Громкость звуков', font_size=50,
            pos=position.part(.5, .2), font_color=(0, 0, 0)
        )
        self.sound_value = Slider(
            pos=position.part(.3, .25), width=width, height=height // 2,
            color_no_act=(128, 128, 128), color_act=(255, 255, 255),
            color_point=(255, 0, 0), value=self.core.sound_volume, 
            func=self.change_volume_music
        )
        self.text_music = TextCenter(
            'Громкость музыки', font_size=50,
            pos=position.part(.5, .4), font_color=(0, 0, 0)
        )
        self.music_value = Slider(
            pos=position.part(.3, .45), width=width, height=height // 2,
            color_no_act=(128, 128, 128), color_act=(255, 255, 255),
            color_point=(255, 0, 0), value=self.core.music_volume, 
            func=self.change_volume_music
        )
        self.button_start_game = ButtonCenter(
            pos=position.part(.5, .5), width=width, height=height, 
            color_active=(128, 128, 128), color_disabled=(255, 255, 255), 
            text=TextCenter(
                'Продолжить', font_size=65,
                pos=(width // 2, height // 2), font_color=(0, 0, 0)
            ), 
            func=self.core.set_window_game
        )
        self.button_menu = ButtonCenter(
            pos=position.part(.5, .7), width=width, height=height, 
            color_active=(128, 128, 128), color_disabled=(255, 255, 255), 
            text=TextCenter(
                'Меню', font_size=65,
                pos=(width // 2, height // 2), font_color=(0, 0, 0)
            ), 
            func=self.core.set_window_menu
        )

    def change_volume_music(self) -> None:
        pg.mixer.music.set_volume(self.core.music_volume.value)

    def draw(self) -> None:
        self.surface.fill((100, 100, 100))
        self.text_pause.draw(self.surface)
        self.text_music.draw(self.surface)
        self.text_sound.draw(self.surface)
        self.button_start_game.draw(self.surface)
        self.button_menu.draw(self.surface)
        self.music_value.draw(self.surface)
        self.sound_value.draw(self.surface)

    def event(self, event: pg.event.Event) -> None:
        self.button_start_game.event(event)
        self.button_menu.event(event)
        self.music_value.event(event)
        self.sound_value.event(event)
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.core.set_window_game()

    def update(self) -> None:
        self.music_value.render()
        self.sound_value.render()

