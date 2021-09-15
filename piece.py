from config import *

class CandyPiece:

    JEWELS = {
        "redtree": pg.image.load("gfx/gem39@0.125x.png").convert_alpha(),
        "orangetree": pg.image.load("gfx/gem37@0.125x.png").convert_alpha(),
        "bluetree": pg.image.load("gfx/gem40@0.125x.png").convert_alpha(),
        "purpletree": pg.image.load("gfx/gem41@0.125x.png").convert_alpha(),
        "greentree": pg.image.load("gfx/gem42@0.125x.png").convert_alpha(),
        "redstar": pg.image.load("gfx/gem21@0.125x.png").convert_alpha(),
        "orangestar": pg.image.load("gfx/gem19@0.125x.png").convert_alpha(),
        "bluestar": pg.image.load("gfx/gem22@0.125x.png").convert_alpha(),
        "purplestar": pg.image.load("gfx/gem23@0.125x.png").convert_alpha(),
        "greenstar": pg.image.load("gfx/gem24@0.125x.png").convert_alpha(),
    }

    def __init__(self, x, y, type):
        self.x = x
        self.y = y
        self.type = type
        self.mouseHover = False
        self.neighbor = False

    def setMouseHover(self, mouseHover):
        self.mouseHover = mouseHover

    def setNeighbor(self, neighbor):
        self.neighbor = neighbor

    def getCartesian(self):
        return self.x, self.y

    def draw(self, surface):
        color = PALETTE["beige"]
        if self.neighbor and self.mouseHover:
            color = PALETTE["red"]
        if self.neighbor or self.mouseHover:
            pg.draw.rect(surface, color, pg.Rect(self.x, self.y, PIECE_SIZE, PIECE_SIZE))

        surface.blit(CandyPiece.JEWELS[self.type], (self.x + 4, self.y + 4))