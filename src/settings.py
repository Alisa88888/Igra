import pygame as pg
#            (640, 480), (960, 540), (1280, 720), (1280, 768), (1280, 1024), (1440, 1080), (1536, 960),
#            (1536, 1024), (1600, 1024), (1920, 1080), (2048, 1080), (2048, 1152), (2048, 1536),
#            (2560, 1080), (2560, 1440), (2560, 1600), (2560, 2048), (3200, 1800), (3200, 2048),
#            (3200, 2400), (3440, 1440), (3840, 2160), (3840, 2400), (4096, 2160)


class Settings:
    def __init__(self) -> None:
        self.fullscreen: bool = False
        self.screen_resolution: tuple[int, int] = (1280, 720)
        self.board_size = (self.width, round(self.height * 0.95))
        self.size_cell = (100, 100)
        self.scores_level = (80, 200)

    @property
    def width(self):
        return self.screen_resolution[0]

    @property
    def height(self):
        return self.screen_resolution[1]

    def get_level(self, scores) -> int:
        for i in range(len(self.scores_level)):
            if scores < self.scores_level[i]:
                return i
        return len(self.scores_level)


settings = Settings()

