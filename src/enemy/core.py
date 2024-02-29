import pygame as pg

from random import randint

from src.settings import settings
from src.typing import CORD
from src.bullet import Bullet
from src.utils import MaxSpeed


class EnemyCore:
    image_path = 'images/core.png'
    size = pg.image.load(image_path).get_rect()

    def __init__(self, core, pos: CORD, borders: CORD, bullets: list[Bullet]) -> None:
        self.borders = borders
        self.core = core
        self.hp = 1
        self.scores = 10
        self.max_speed = MaxSpeed(x=(-9, -3), y=(-5, 5))
        is_spin = randint(0, 5) == 0
        spin = randint(*self.max_speed.y) if is_spin else 0
        self.speed = (randint(*self.max_speed.x), spin)
        self.time_attack = (
            self.max_speed.all_max - sum(map(abs, self.speed))
        ) * 100
        self.bullets = bullets

        self.surface = pg.image.load(self.image_path)
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = pos
        self.tick_attack = pg.time.get_ticks() - round(self.time_attack * 0.8)

        self.sound_attack = pg.mixer.Sound('sounds/attack.mp3')

    @property
    def padding_y(self) -> int:
        return self.rect.height

    def draw(self, surface: pg.Surface):
        surface.blit(self.surface, self.rect)

    def move(self) -> None:
        x, y = self.speed
        if not (0 < self.rect.y + y < self.borders[1] - self.rect.height):
            self.speed = (x, -y)
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]

    def attack(self) -> None:
        tick = pg.time.get_ticks()
        if tick - self.tick_attack >= self.time_attack:
            self.bullets.append(Bullet(
                pos=(self.rect.x, self.rect.y + (self.rect.height - Bullet.size.height) // 2),
                speed=(self.speed[0], 0)
            ))
            self.tick_attack = tick
            self.sound_attack.set_volume(self.core.sound_volume.value)
            self.sound_attack.play()

    def damage(self) -> None:
        self.hp -= 1

    def is_live(self) -> bool:
        return self.hp > 0

    def update(self) -> None:
        self.move()
        self.attack()

    def no_field(self) -> bool:
        return self.rect.x <= -self.rect.width

