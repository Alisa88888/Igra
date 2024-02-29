import pygame as pg

from src.core import Core



if __name__ == '__main__':
    pg.mixer.pre_init(44100, -16, 1, 512)
    pg.init()
    core = Core()
    core.start()

