from config import *
import board


class App:
    TITLE_FONT = pg.font.SysFont("jokerman", 45)
    TEXT_FONT = pg.font.SysFont("papyrus", 20)

    def __init__(self):
        self.clock = pg.time.Clock()
        self.board = board.GameBoard(50, 50)
        self.TITLE = App.TITLE_FONT.render("Tism Gem Smash", True, PALETTE["brown"])

    def mainLoop(self):
        # update
        for event in pg.event.get():
            if event.type == pg.QUIT:
                return False
        (x, y) = pg.mouse.get_pos()
        mouseLablel = App.TEXT_FONT.render(f"mouse: ({x}, {y})", True, PALETTE["red"], PALETTE["beige"])

        # draw
        SCREEN.fill(PALETTE["beige"])

        self.board.draw(SCREEN)

        # targetSurface.blit(sourceSurface, upperleft)
        SCREEN.blit(self.TITLE, (275, -9))
        SCREEN.blit(mouseLablel, (400, 900))
        pg.display.update()

        # timing
        pg.display.set_caption(str(self.clock.get_fps()))
        self.clock.tick(60)
        return True
