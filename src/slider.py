import pygame as pg

from src.typing import CORD, COLOR


class Value:
    def __init__(
        self, min_: int | float, max_: int | float, change: int | float,
        value: int | float | None = None
    ) -> None:
        self.min_ = min_
        self.max_ = max_
        self.change = change
        self.value = value if value is not None else min_

    def edit(self, sign) -> None:
        self.value = min(
            self.max_,
            max(self.min_, self.value + sign * self.change)
        )

    def set_value(self, value) -> None:
        self.value = min(self.max_, max(self.min_, value))

    def set(self, min_: int | float, max_: int | float) -> None:
        self.min_, self.max_ = min_, max_


class Slider:
    def __init__(
        self, pos: CORD, width: int, height: int, color_no_act: COLOR, color_act: COLOR,
        color_point: COLOR, value, func, name: str | None = None
    ) -> None:
        self.rect = pg.Rect(*pos, width, height)
        self.value = value
        self.func = func
        self.name = name
        self.color_no_act = color_no_act
        self.color_act = color_act
        self.color_point = color_point
        self.radius_main = self.rect.height // 2
        self.rect_height = self.rect.height // 2.5
        self.radius_mini = self.rect_height // 2
        self.two_radius = self.radius_main + self.radius_mini
        self.rect_width = int(
            self.rect.width - 2 * self.radius_main - 2 * self.radius_mini
        )
        self.padding = (self.rect.height - self.rect_height) // 2
        self.pixel_size = self.rect_width + 2 * self.radius_mini
        self.pixel_change = self.pixel_size / self.value.max_ * self.value.change
        self.flag_click = False
        self.render()

    def event(self, event: pg.event.Event) -> None:
        try:
            if self.rect.collidepoint(*event.pos):
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    self.flag_click = False
                if self.flag_click:
                    value = round(
                        (event.pos[0] - self.rect.x - self.radius_main) /
                        self.pixel_change * self.value.change, 3
                    )
                    self.value.set_value(value)
                    if self.func:
                        self.func()
                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1 and not self.flag_click:
                    self.flag_click = True
            else:
                self.flag_click = False
            self.render()
        except AttributeError:
            pass

    def render(self) -> None:
        self.surface = pg.Surface(
            (self.rect.width, self.rect.height), pg.SRCALPHA)
        pg.draw.circle(
            self.surface, self.color_act,
            (self.two_radius, self.padding + self.radius_mini),
            self.radius_mini
        )
        pg.draw.circle(
            self.surface, self.color_no_act,
            (self.rect.width - self.two_radius, self.padding + self.radius_mini),
            self.radius_mini
        )
        pg.draw.rect(
            self.surface, self.color_no_act,
            (self.two_radius, self.padding, self.rect_width, self.rect_height)
        )
        w_value = self.pixel_size * (self.value.value / self.value.max_)
        pg.draw.rect(
            self.surface, self.color_act,
            (self.two_radius, self.padding, w_value, self.rect_height)
        )
        pg.draw.circle(
            self.surface, self.color_point,
            (self.radius_main + w_value, self.padding + self.radius_mini),
            self.radius_main
        )

    def draw(self, surface: pg.Surface) -> None:
        surface.blit(self.surface, self.rect)

