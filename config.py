import pygame as pg
import random


pg.init()
SCREEN_SIZE = (900, 1050)
SCREEN = pg.display.set_mode(SCREEN_SIZE)

PALETTE = {
    "red": (255, 36, 66),
    "beige": (255, 237, 218),
    "brown": (134, 84, 57),
    "pink": (255, 103, 231)
}

PIECE_SIZE = 60