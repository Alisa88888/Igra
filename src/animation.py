import pygame as pg
from random import randint

from src.bullet import Bullet
from src.typing import CORD
from src.enemy.core import EnemyCore
from src.enemy.asteroid import Asteroid
from src.enemy.stormtrooper import Stormtrooper
from src.enemy.leviathan import Leviathan


class Animation:
    def __init__(self, pos: CORD, size: CORD, core) -> None:
        self.core = core
        self.surface = pg.Surface(size)
        self.rect = pg.Rect(*pos, *size)
        self.max_count_enemy = 6
        self.enemys: list[EnemyCore] = []
        self.bullets_enemy: list[Bullet] = []

    def draw(self, surface: pg.Surface) -> None:
        self.surface.fill((100, 100, 100))
        pg.draw.rect(
            self.surface, (180, 180, 180),
            (0, self.rect.height, self.rect.width, self.rect.height)
        )
        for enemy in self.enemys:
            enemy.draw(self.surface)
        for bullet in self.bullets_enemy:
            bullet.draw(self.surface)
        surface.blit(self.surface, self.rect)

    def event(self, event: pg.event.Event) -> None:
        pass

    def update(self) -> None:
        self.spawn_enemy()
        for enemy in self.enemys:
            enemy_remove = False
            enemy.update()
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

    def spawn_enemy(self) -> None:
        num_spawn = randint(0, 100)

        if len(self.enemys) < self.max_count_enemy:
            if num_spawn == 0:
                y_pos = randint(0, self.rect.height - Asteroid.size.height)
                enemy = Asteroid(
                    core=self.core,
                    pos=(self.rect.width, y_pos),
                    borders=(self.rect.width, self.rect.height),
                    bullets=self.bullets_enemy
                )
                enemy.speed = (enemy.speed[0], 0)
                self.enemys.append(enemy)
            elif num_spawn == 1:
                y_pos = randint(0, self.rect.height - EnemyCore.size.height)
                enemy = EnemyCore(
                    core=self.core,
                    pos=(self.rect.width, y_pos),
                    borders=(self.rect.width, self.rect.height),
                    bullets=self.bullets_enemy
                )
                enemy.speed = (enemy.speed[0], 0)
                self.enemys.append(enemy)
            elif num_spawn == 2:
                y_pos = randint(0, self.rect.height - Stormtrooper.size.height)
                enemy = Stormtrooper(
                    core=self.core,
                    pos=(self.rect.width, y_pos),
                    borders=(self.rect.width, self.rect.height),
                    bullets=self.bullets_enemy
                )
                enemy.speed = (enemy.speed[0], 0)
                self.enemys.append(enemy)
            elif num_spawn == 3:
                y_pos = randint(0, self.rect.height - Leviathan.size.height)
                enemy = Leviathan(
                    core=self.core,
                    pos=(self.rect.width, y_pos),
                    borders=(self.rect.width, self.rect.height),
                    bullets=self.bullets_enemy
                )
                enemy.speed = (enemy.speed[0], 0)
                self.enemys.append(enemy)

