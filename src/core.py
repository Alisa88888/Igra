import sys
import json
import pygame as pg

from .settings import settings
from .windows import Window
from .windows.menu import WindowMenu
from .windows.game import WindowGame
from .windows.gameover import WindowGameOver
from .windows.pause import WindowPause

from src.slider import Value


class Core:
    def __init__(self) -> None:
        pg.display.set_caption('Space War')
        self.is_run = False
        self.clock = pg.time.Clock()
        self.display = pg.display.set_mode(settings.screen_resolution)
        self.music_volume = Value(0, 1, 0.01, round(1 / 16, 3))
        self.sound_volume = Value(0, 1, 0.01, round(1 / 16, 3))
        self.music = pg.mixer.music.load('sounds/back.mp3')
        pg.mixer.music.set_volume(self.music_volume.value)
        pg.mixer.music.play()

        self.window_menu = WindowMenu(self)
        self.window_game = WindowGame(self)
        self.window_game_over = WindowGameOver(self)
        self.window_pause = WindowPause(self)

        self.action_window = self.window_menu

    def set_window_menu(self) -> None:
        self.window_menu.update_scores()
        self.action_window = self.window_menu
    
    def set_window_game(self) -> None:
        self.action_window = self.window_game

    def set_window_game_over(self, scores: int) -> None:
        self.window_game_over.set_scores(scores)
        with open('scores.json') as file:
            data = json.load(file)
            data['max'] = max(data['max'], scores)
            data['last'] = scores
        with open('scores.json', "w") as file:
            json.dump(data, file)
        self.action_window = self.window_game_over
        self.window_game.init()

    def set_window_pause(self) -> None:
        self.action_window = self.window_pause

    def set_resolution(self) -> None:
        if settings.fullscreen:
            self.display = pg.display.set_mode(
                settings.screen_resolution, pg.FULLSCREEN
            )
        else:
            self.display = pg.display.set_mode(settings.screen_resolution)

    def event(self) -> None:
        for en in pg.event.get():
            if en.type == pg.QUIT:
                pg.quit()
                sys.exit()
            #
            if self.action_window is not None:
                self.action_window.event(en)

    def update(self) -> None:
        if self.action_window is not None:
            self.action_window.update()

    def draw(self) -> None:
        if self.action_window is not None:
            self.action_window.draw()

    def start(self) -> None:
        pg.event.clear()
        self.is_run = True

        while self.is_run:
            self.clock.tick(60)
            # pg.display.set_caption(str(self.clock.get_fps()))  # нужно для отладки. FPS в заголовок окна!

            self.event()
            self.update()
            self.draw()
            #
            if self.action_window is not None:
                self.display.blit(self.action_window.surface, (0, 0))
            pg.display.update()

