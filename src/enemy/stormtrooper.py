import pygame as pg

from src.typing import CORD
from src.bullet import Bullet
from src.enemy.core import EnemyCore


class Stormtrooper(EnemyCore):
    image_path = 'images/stormtrooper.png'
    size = pg.image.load(image_path).get_rect()

    def __init__(self, core, pos: CORD, borders: CORD, bullets: list[Bullet]) -> None:
        super().__init__(core, pos, borders, bullets)
        self.time_attack *= 1.5
        self.scores = 20
        self.hp = 2

    def attack(self) -> None:
        tick = pg.time.get_ticks()
        if tick - self.tick_attack >= self.time_attack:
            for padding in (
                self.rect.height // 4 - Bullet.size.height // 2,
                self.rect.height // 4 * 3 - Bullet.size.height // 2
            ):
                self.bullets.append(Bullet(
                    pos=(self.rect.x, self.rect.y + padding),
                    speed=(self.speed[0], 0)
                ))
            self.tick_attack = tick
            self.sound_attack.set_volume(self.core.sound_volume.value)
            self.sound_attack.play()

