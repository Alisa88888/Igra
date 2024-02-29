import pygame as pg


class Text:
    def __init__(
        self, text: str, pos: tuple[int, int],
            font_color: tuple[int, int, int] = (255, 255, 255),
            font_type: str | None = None, font_size: int = 20
    ) -> None:
        self.text = text
        self._pos = tuple(pos)
        self.font_color = font_color
        self.font_type = font_type
        self.font_size = font_size
        #
        self.font = pg.font.Font(font_type, font_size)
        self.surface = self.font.render(text, True, font_color)
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = self._pos

    def set_text(self, text: str) -> None:
        if text != self.text:
            self.__init__(
                text=text, pos=self._pos, font_color=self.font_color,
                font_type=self.font_type, font_size=self.font_size
            )

    def draw(self, surface: pg.surface.Surface) -> None:
        surface.blit(self.surface, self.rect)


class TextCenter(Text):
    def __init__(
        self, text: str, pos: tuple[int, int],
        font_color: tuple[int, int, int] = (255, 255, 255),
        font_type: str | None = None, font_size: int = 20
    ) -> None:
        super().__init__(text, pos, font_color, font_type, font_size)
        self.rect.x -= self.rect.width // 2
        self.rect.y -= self.rect.height // 2


class TextCenterRect(Text):
    def __init__(
        self, text: str, width: int, height: int, pos: tuple[int, int],
            font_color: tuple[int, int, int] = (255, 255, 255),
            font_type: str | None = None, font_size: int = 20
    ) -> None:
        self.width = width
        self.height = height
        super().__init__(text, pos, font_color, font_type, font_size)
        if width:
            self.rect.x += (width - self.rect.width) // 2
        if height:
            self.rect.y += (height - self.rect.height) // 2

    def set_text(self, text: str) -> None:
        if text != self.text:
            self.__init__(
                text=text, width=self.width, height=self.height, pos=self._pos,
                font_color=self.font_color, font_type=self.font_type,
                font_size=self.font_size
            )


def get_max_size(
    text: str, font_color, font_type,
    width: int | None = None, height: int | None = None
):
    font_size = 1
    while True:
        surface = pg.font.Font(
            font_type, font_size
        ).render(text, True, font_color)
        rect = surface.get_rect()
        if (width and width <= rect.width) or (height and height <= rect.height):
            return font_size - 1
        font_size += 1


class TextMaxSize:
    def __init__(
        self, text: str, width: int | None = None, height: int | None = None,
        pos: tuple[int, int] = (0, 0),
        font_color: tuple[int, int, int] = (255, 255, 255),
        font_type: str | None = None
    ) -> None:
        self.width = width
        self.height = height
        self.text = text
        self.pos = tuple(pos)
        self.font_color = font_color
        self.font_type = font_type
        self.font_size = get_max_size(
            text, font_color, font_type, width, height
        )
        self.surface = pg.font.Font(
            font_type, self.font_size
        ).render(text, True, font_color)
        self.rect = self.surface.get_rect()
        self.rect.x, self.rect.y = pos

    def set_text(self, text: str) -> None:
        if text != self.text:
            self.text = text
            self.__init__(text, self.width, self.height,
                          self.pos, self.font_color, self.font_type)

    def draw(self, surface: pg.Surface) -> None:
        surface.blit(self.surface, self.rect)


class TextGroupMaxSize:
    def __init__(
        self, texts: list[str], pos: tuple[int, int], padding: tuple[int, int],
        width: int | None = None, height: int | None = None,
        font_color: tuple[int, int, int] = (255, 255, 255),
        font_type: str | None = None
    ) -> None:
        self.size = get_max_size(
            max(texts), font_color, font_type, width, height
        )
        self.texts = [
            Text(
                text, (pos[0] + padding[0] * ind, pos[1] + padding[1] * ind),
                font_color, font_type, self.size
            )
            for ind, text in enumerate(texts)
        ]

    def draw(self, surface: pg.Surface) -> None:
        for text in self.texts:
            text.draw(surface)

