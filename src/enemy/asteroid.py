import pygame as pg
from random import randint

from .core import EnemyCore
from src.typing import CORD
from src.bullet import Bullet
from src.utils import MaxSpeed


class Asteroid(EnemyCore):
    image_path = 'images/asteroid.png'
    size = pg.image.load(image_path).get_rect()

    def __init__(self, core, pos: CORD, borders: CORD, bullets: list[Bullet]) -> None:
        super().__init__(core, pos, borders, bullets)
        self.hp = 3
        self.scores = 5
        self.max_speed = MaxSpeed(x=(-6, -3), y=(0, 0))
        self.speed = (randint(*self.max_speed.x), 0)

    def attack(self) -> None:
        pass

    def damage(self) -> None:
        x, y = self.rect.x, self.rect.y
        self.hp -= 1
        self.surface = pg.transform.scale(
            self.surface,
            (self.rect.width - 10, self.rect.height - 10)
        )
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = x + 5, y + 5

