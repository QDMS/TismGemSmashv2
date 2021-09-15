from config import *
import piece


class GameBoard:
    TYPES = ["redtree", "orangetree", "bluetree", "purpletree", "greentree", "redstar", "orangestar", "bluestar",
             "purplestar", "greenstar"]

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 800
        self.height = 810
        self.surface = pg.Surface((self.width, self.height))
        self.numRows = self.height // PIECE_SIZE
        self.numCols = self.width // PIECE_SIZE
        self.pieces = []
        self.reset()
        self.populate()

    def update(self):
        #reset state of pieces
        for row in range(self.numRows):
            for column in range(self.numCols):
                thisPiece = self.pieces[row][column]
                if thisPiece is not None:
                    thisPiece.setMouseHover(False)
                    thisPiece.setNeighbor(False)

    def hasMouse(self, x, y):
        xCheck = x > self.x and x < self.x + self.width
        yCheck = y > self.y and y < self.y + self.height
        return xCheck and yCheck

    def cartesianToGrid(self, x, y):
        row = max(0, min(self.numRows - 1, (y - self.y) // PIECE_SIZE))
        column = max(0, min(self.numCols, (x - self.x) // PIECE_SIZE))
        return (row, column)

    def handleMouseMovement(self):
        (x, y) = pg.mouse.get_pos()
        if self.hasMouse(x, y):
            (row, column) = self.cartesianToGrid(x, y)
            self.pieces[row][column].setMouseHover(True)

    def reset(self):
        for row in range(self.numRows):
            self.pieces.append([])
            for column in range(self.numCols):
                self.pieces[row].append(None)

    def populate(self):
        for row in range(self.numRows):
            for column in range(self.numCols):
                x = column * PIECE_SIZE
                y = row * PIECE_SIZE
                type = GameBoard.TYPES[random.randint(0, 9)]
                self.pieces[row][column] = piece.CandyPiece(x, y, type)

    def draw(self, surface):
        self.surface.fill(PALETTE["pink"])
        for row in range(self.numRows):
            for column in range(self.numCols):
                if self.pieces[row][column] is not None:
                    self.pieces[row][column].draw(self.surface)
        surface.blit(self.surface, (self.x, self.y))
