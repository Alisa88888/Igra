import pygame as pg
from random import randint

from src.settings import settings
from src.bullet import Bullet
from src.player import Player
from src.texts import Text, TextMaxSize

from src.enemy.core import EnemyCore
from src.enemy.asteroid import Asteroid
from src.enemy.stormtrooper import Stormtrooper
from src.enemy.leviathan import Leviathan

from .core import Window


class WindowGame(Window):
    def __init__(self, core) -> None:
        super().__init__(core)
        self.max_count_enemy = 10
        self.enemys: list[EnemyCore]
        self.bullets_enemy: list[Bullet]
        self.player: Player
        self.scores = 0

        self.scores_text = TextMaxSize(
            '',
            height=settings.height - settings.board_size[1],
            pos=(0, settings.board_size[1])
        )
        self.init()

    def init(self) -> None:
        self.enemys = []
        self.bullets_enemy = []
        self.player = Player(self.core, (100, settings.height // 2))
        self.scores = 0

    def draw(self) -> None:
        self.surface.fill((100, 100, 100))
        pg.draw.rect(
            self.surface, (180, 180, 180),
            (0, settings.board_size[1], *settings.screen_resolution)
        )
        self.player.draw(self.surface)
        for enemy in self.enemys:
            enemy.draw(self.surface)
        for bullet in self.bullets_enemy:
            bullet.draw(self.surface)
        self.scores_text.draw(self.surface)

    def event(self, event: pg.event.Event) -> None:
        self.player.event(event)
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            self.core.set_window_pause()

    def update(self) -> None:
        if not self.scores % 50:
            self.max_count_enemy += 5

        self.player.update(self.scores)
        self.spawn_enemy()
        for enemy in self.enemys:
            enemy_remove = False
            enemy.update()
            if enemy.rect.colliderect(self.player.rect):
                self.core.set_window_game_over(self.scores)
            # Убийство противника
            for bullet in self.player.bullets:
                if enemy.rect.colliderect(bullet.rect):
                    enemy.damage()
                    if not enemy.is_live():
                        enemy_remove = True
                        self.scores += enemy.scores
                    self.player.bullets.remove(bullet)
            # Убийство игрока
            for bullet in enemy.bullets:
                if bullet.rect.colliderect(self.player.rect):
                    self.core.set_window_game_over(self.scores)
            # Проверка на вылет противника за экран
            if enemy.no_field():
                enemy_remove = True
            if enemy_remove and enemy in self.enemys:
                self.enemys.remove(enemy)
        # Проверка на вылет пули за экран
        for bullet in self.bullets_enemy:
            bullet.update()
            if bullet.no_field():
                self.bullets_enemy.remove(bullet)
        # Обновление очков
        self.scores_text.set_text(
            f'Очки: {self.scores}   Уровень: {settings.get_level(self.scores)}'
        )

    def spawn_enemy(self) -> None:
        num_spawn = randint(0, max(10, 80 - self.scores % 50))

        if len(self.enemys) < self.max_count_enemy:
            if num_spawn == 0:
                y_pos = randint(0, settings.board_size[1] - Asteroid.size.height)
                self.enemys.append(Asteroid(
                    core=self.core,
                    pos=(settings.width, y_pos),
                    borders=(settings.width, settings.height),
                    bullets=self.bullets_enemy
                ))
            elif num_spawn == 1:
                y_pos = randint(0, settings.board_size[1] - EnemyCore.size.height)
                self.enemys.append(EnemyCore(
                    core=self.core,
                    pos=(settings.width, y_pos),
                    borders=(settings.width, settings.height),
                    bullets=self.bullets_enemy
                ))
            elif num_spawn == 2 and self.scores > settings.scores_level[0]:
                y_pos = randint(0, settings.board_size[1] - Stormtrooper.size.height)
                self.enemys.append(Stormtrooper(
                    core=self.core,
                    pos=(settings.width, y_pos),
                    borders=(settings.width, settings.height),
                    bullets=self.bullets_enemy
                ))
            elif num_spawn == 3 and self.scores > settings.scores_level[1]:
                y_pos = randint(0, settings.board_size[1] - Leviathan.size.height)
                self.enemys.append(Leviathan(
                    core=self.core,
                    pos=(settings.width, y_pos),
                    borders=(settings.width, settings.height),
                    bullets=self.bullets_enemy
                ))

