import pygame as pg

from src.typing import CORD


class Bullet:
    image_path = 'images/bullet.png'
    size = pg.image.load(image_path).get_rect()

    def __init__(self, pos: CORD, speed: tuple[int, int]) -> None:
        self.surface = pg.image.load(self.image_path)
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = pos
        self.speed = (speed[0] - 3, speed[1])

        self.render()

    def render(self) -> None:
        pass
        # self.surface.fill((200, 0, 0))

    def move(self) -> None:
        self.rect.x += self.speed[0]
        self.rect.y += self.speed[1]
        
    def update(self) -> None:
        self.move()

    def draw(self, surface: pg.Surface) -> None:
        surface.blit(self.surface, self.rect)

    def no_field(self) -> bool:
        return self.rect.x <= -self.rect.width


class BulletPlayer(Bullet):
    def __init__(self, pos: CORD, speed: tuple[int, int]) -> None:
        super().__init__(pos, speed)
        self.speed = (speed[0] + 3, speed[1])
        self.surface = pg.transform.flip(self.surface, True, False)

    def render(self) -> None:
        pass
        # self.surface.fill((0, 200, 0))

