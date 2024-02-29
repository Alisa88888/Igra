import pygame as pg

from src.settings import settings


class Window:
    def __init__(self, core) -> None:
        self.core = core
        self.surface = pg.Surface(settings.screen_resolution)

    def event(self, event: pg.event.Event) -> None:
        pass

    def draw(self) -> None:
        pass

    def update(self) -> None:
        pass

