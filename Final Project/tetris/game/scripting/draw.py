import pygame, random
from pygame.locals import *
from constants import *

from game.casting.allignment import Allignment


class Draw:
    """
    """
    def __init__(self):
        pass 

    def convertToPixelCoords(boxx, boxy):
        # Convert the given xy coordinates of the board to xy
        # coordinates of the location on the screen.
        return (XMARGIN + (boxx * BOXSIZE)), (TOPMARGIN + (boxy * BOXSIZE))


    def drawBox(self,boxx, boxy, color, pixelx=None, pixely=None):
        # draw a single box (each tetris piece has four boxes)
        # at xy coordinates on the board. Or, if pixelx & pixely
        # are specified, draw to the pixel coordinates stored in
        # pixelx & pixely (this is used for the "Next" piece).
        if color == BLANK:
            return
        if pixelx == None and pixely == None:
            pixelx, pixely = Allignment.convertToPixelCoords(boxx, boxy)
        pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 1, BOXSIZE - 1))
        pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelx + 1, pixely + 1, BOXSIZE - 4, BOXSIZE - 4))


    def drawBoard(self,board):
        # draw the border around the board
        pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)
        
        # fill the background of the board
        pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))

        # draw the individual boxes on the board
        for x in range(BOARDWIDTH):
            for y in range(BOARDHEIGHT):
                self.drawBox(x, y, board[x][y])


    def drawStatus(self, score, level = 1):
        # draw the score text
        scoreSurf = BASICFONT.render('Score: %s' % score, True, TEXTCOLOR)
        scoreRect = scoreSurf.get_rect()
        scoreRect.topleft = (WINDOWWIDTH - 150, 20)
        DISPLAYSURF.blit(scoreSurf, scoreRect)
        
        # draw the level text
        levelSurf = BASICFONT.render('Level: %s' % level, True, TEXTCOLOR)
        levelRect = levelSurf.get_rect()
        levelRect.topleft = (WINDOWWIDTH - 150, 50)
        DISPLAYSURF.blit(levelSurf, levelRect)


    def drawPiece(self, piece, pixelx=None, pixely=None):
        shapeToDraw = SHAPES[piece['shape']][piece['rotation']]
        
        if pixelx == None and pixely == None:
            # if pixelx & pixely hasn't been specified, use the location stored in the piece data structure
            pixelx, pixely = Allignment.convertToPixelCoords(piece['x'], piece['y'])
            
        # draw each of the blocks that make up the piece
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if shapeToDraw[y][x] != BLANK:
                    self.drawBox(None, None, piece['color'], pixelx + (x * BOXSIZE), pixely + (y * BOXSIZE))


    def drawNextPiece(self, piece):
        # draw the "next" text
        nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
        nextRect = nextSurf.get_rect()
        nextRect.topleft = (WINDOWWIDTH - 120, 80)
        DISPLAYSURF.blit(nextSurf, nextRect)
        # draw the "next" piece
        self.drawPiece(piece, pixelx=WINDOWWIDTH-120, pixely=100)
    
    def getNewPiece(self):
        # return a random new piece in a random rotation and color
        shape = random.choice(list(SHAPES.keys()))
        newPiece = {'shape': shape, 
                    'rotation': random.randint(0, len(SHAPES[shape]) - 1),
                    'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
                    'y': -2, # start it above the board (i.e. less than 0)
                    'color': random.randint(0, len(COLORS)-1)}
        return newPiece
    
    def addToBoard(self, board, piece):
        # fill in the board based on piece's location, shape, and rotation
        for x in range(TEMPLATEWIDTH):
            for y in range(TEMPLATEHEIGHT):
                if SHAPES[piece['shape']][piece['rotation']][y][x] != BLANK:
                    board[x + piece['x']][y + piece['y']] = piece['color']
    
    def getBlankBoard(self):
        # create and return a new blank board data structure
        board = []
        for i in range(BOARDWIDTH):
            board.append([BLANK] * BOARDHEIGHT)
        return board