import pygame as pg

from src.settings import settings
from src.bullet import BulletPlayer
from src.typing import CORD


class Player:
    def __init__(self, core, pos: CORD) -> None:
        self.core = core
        self.speed = (5, 7)
        self.time_attack = 0.5 * 600
        self.bullets: list[BulletPlayer] = []

        self.surface = pg.image.load('images/me.png')
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = pos
        self.tick_attack = pg.time.get_ticks() - round(self.time_attack * 0.8)
        self.direction_move = [0, 0]
        self.is_attack = False

        self.sound_attack = pg.mixer.Sound('sounds/attack.mp3')
        bullet = BulletPlayer.size.height // 2
        self.range_attack = (
            (self.rect.height // 4 - bullet, self.rect.height // 4 * 3 - bullet),
            (self.rect.height // 2 - bullet, self.rect.height // 4 - bullet, self.rect.height // 4 * 3 - bullet),
        )

    def draw(self, surface: pg.Surface):
        for bullet in self.bullets:
            bullet.draw(surface)
        surface.blit(self.surface, self.rect)

    def update(self, scores: int) -> None:
        self.move()
        self.attack(scores)
        for bullet in self.bullets:
            bullet.update()
            if bullet.no_field():
                self.bullets.remove(bullet)

    def event(self, event: pg.event.Event)-> None:
        if event.type == pg.KEYDOWN and event.key == pg.K_w:
            self.direction_move[1] = -1
        if event.type == pg.KEYDOWN and event.key == pg.K_s:
            self.direction_move[1] = 1
        if event.type == pg.KEYDOWN and event.key == pg.K_a:
            self.direction_move[0] = -1
        if event.type == pg.KEYDOWN and event.key == pg.K_d:
            self.direction_move[0] = 1
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            self.is_attack = True

        if event.type == pg.KEYUP and event.key == pg.K_w:
            self.direction_move[1] = 0
        if event.type == pg.KEYUP and event.key == pg.K_s:
            self.direction_move[1] = 0
        if event.type == pg.KEYUP and event.key == pg.K_a:
            self.direction_move[0] = 0
        if event.type == pg.KEYUP and event.key == pg.K_d:
            self.direction_move[0] = 0
        if event.type == pg.KEYUP and event.key == pg.K_SPACE:
            self.is_attack = False


    def move(self) -> None:
        x, y = self.speed
        x *= self.direction_move[0]
        y *= self.direction_move[1]

        if 0 <= self.rect.x + x <= settings.board_size[0] - self.rect.width:
            self.rect.x += x
        if 0 < self.rect.y + y < settings.board_size[1] - self.rect.height:
            self.rect.y += y

    def attack(self, scores: int) -> None:
        if self.is_attack:
            tick = pg.time.get_ticks()
            if tick - self.tick_attack >= self.time_attack:
                if scores <= 100:
                    self.bullets.append(BulletPlayer(
                        pos=(self.rect.x, self.rect.y + (self.rect.height - BulletPlayer.size.height) // 2),
                        speed=(self.speed[0], 0)
                    ))
                elif scores > 100:
                    range_attack = 0 if scores < 200 else 1
                    for padding in self.range_attack[range_attack]:
                        self.bullets.append(BulletPlayer(
                            pos=(self.rect.x, self.rect.y + padding),
                            speed=(self.speed[0], 0)
                        ))
                self.tick_attack = tick
                self.sound_attack.set_volume(self.core.sound_volume.value)
                self.sound_attack.play()

    def no_field(self) -> bool:
        return self.rect.x <= -self.rect.width

