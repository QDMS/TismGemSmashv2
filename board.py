from config import *
import piece


class GameBoard:
    PIECE_SIZE = 60

    TYPES = ["redtree", "orangetree", "bluetree", "purpletree", "greentree", "redstar", "orangestar", "bluestar",
             "purplestar", "greenstar"]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 800
        self.height = 810
        self.surface = pg.Surface((self.width, self.height))
        self.numRows = self.height // GameBoard.PIECE_SIZE
        self.numCols = self.width // GameBoard.PIECE_SIZE
        self.pieces = []
        self.reset()
        self.populate()

    def reset(self):
        for row in range(self.numRows):
            self.pieces.append([])
            for column in range(self.numCols):
                self.pieces[row].append(None)

    def populate(self):
        for row in range(self.numRows):
            for column in range(self.numCols):
                x = column * GameBoard.PIECE_SIZE
                y = row * GameBoard.PIECE_SIZE
                type = GameBoard.TYPES[random.randint(0, 9)]
                self.pieces[row][column] = piece.CandyPiece(x, y, type)

    def draw(self, surface):
        self.surface.fill(PALETTE["pink"])
        for row in range(self.numRows):
            for column in range(self.numCols):
                if self.pieces[row][column] is not None:
                    self.pieces[row][column].draw(self.surface)
        surface.blit(self.surface, (self.x, self.y))
