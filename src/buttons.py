import pygame as pg

from .typing import TEXT, COLOR


class Button:
    def __init__(
        self, pos: tuple[int, int], width: int, height: int,
        color_disabled: COLOR, color_active: COLOR, text: TEXT,
            func, func_args: tuple | None = None
    ) -> None:
        self.rect = pg.Rect(*pos, width, height)
        self.surface = pg.Surface((self.rect.width, self.rect.height))
        self.click = pg.Rect(*pos, width, height)

        self.func = func
        self.func_args = func_args if func_args is not None else tuple()

        self.text = text
        self.color_disabled = color_disabled
        self.color_active = color_active
        self.color = self.color_disabled
        self.flag_click = False
        self.render()

    def event(self, event: pg.event.Event) -> None:
        try:
            pos = event.pos[0], event.pos[1]
            if self.click.collidepoint(pos):
                self.color = self.color_active
                if event.type == pg.MOUSEBUTTONUP and event.button == 1 and self.flag_click:
                    self.flag_click = False
                    self.func(*self.func_args)
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and not self.flag_click:
                    self.flag_click = True
            else:
                self.color = self.color_disabled
            self.render()
        except AttributeError:
            pass

    def render(self) -> None:
        self.surface.fill(pg.Color(self.color))
        self.text.draw(self.surface)

    def draw(self, surface: pg.Surface) -> None:
        surface.blit(self.surface, self.rect)


class ButtonCenter(Button):
    def __init__(
        self, pos: tuple[int, int], width: int, height: int,
        color_disabled: COLOR, color_active: COLOR, text: TEXT,
        func, func_args: tuple | None = None
    ) -> None:
        pos = (pos[0] - width // 2, pos[1] + height // 2)
        super().__init__(
            pos, width, height, color_disabled, color_active, text,
            func, func_args
        )
