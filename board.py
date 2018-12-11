import pygame

import pieces as p

# global constants
SQUARE_SIZE = 60

# global variables
Board = [[]]

# draws a section of the board, with a piece if applicable
def drawSquare(i, j):
  screen = pygame.display.get_surface() 
  # get the rectangle
  gridRect = pygame.Rect(i*SQUARE_SIZE,j*SQUARE_SIZE,SQUARE_SIZE,SQUARE_SIZE)
  # draw the grid
  if ((i + j) % 2 == 0):
    # draw a darker square every other square
    pygame.draw.rect(screen, (150,150,150), gridRect)
  pygame.draw.rect(screen, (0,0,0), gridRect, 1)
  
  if (Board[i][j] != None):
    # draw the piece
    colour = Board[i][j].iColour
    piece = Board[i][j].iPiece
    pygame.Surface.blit(screen, p.PieceImages[colour][piece], gridRect)
  pygame.display.update(gridRect)

# draws the entire board
def drawBoard(): 
  screen = pygame.display.get_surface()    
  screen.fill((255,255,255))
  pygame.display.flip()
  for i in range(0, len(Board)):
    for j in range(0, len(Board[i])):
      drawSquare(i,j)
      
# resets all the pieces on the board and draws it 
def resetBoard():
  global Board
  # pawns
  for i in range(8):
    Board[i][1] = p.Pawn(0)
    Board[i][6] = p.Pawn(1)
  # rooks
  Board[0][0] = p.Rook(0)
  Board[7][0] = p.Rook(0)
  Board[0][7] = p.Rook(1)
  Board[7][7] = p.Rook(1)
  # knights
  Board[1][0] = p.Knight(0)
  Board[6][0] = p.Knight(0)
  Board[1][7] = p.Knight(1)
  Board[6][7] = p.Knight(1)
  # bishops
  Board[2][0] = p.Bishop(0)
  Board[5][0] = p.Bishop(0)
  Board[2][7] = p.Bishop(1)
  Board[5][7] = p.Bishop(1)
  # queens
  Board[3][0] = p.Queen(0)
  Board[4][7] = p.Queen(1)
  # kings
  Board[4][0] = p.King(0)
  Board[3][7] = p.King(1)
  # None
  for i in range(2, 6):
    for j in range(8):
      Board[j][i] = None
  drawBoard()
  
def initBoard():
  global Board

  # load the images
  p.LoadPieceImages()
  # init the board
  Board = [[None for x in range(8)] for y in range(8)]
  resetBoard()