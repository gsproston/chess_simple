import pygame

import pieces as p

# global constants
SQUARE_SIZE = 60

# global variables
Board = [[]]

class Square:
  piece = None

  def __init__(self, x, y):
    self.x = x
    self.y = y   
    
    # auto select the piece
    if (y >= 2 and y <= 5):
      # no piece
      return 
    # determine colour first
    colour = 1
    if (y <= 1):
      colour = 0
    # now the piece type
    if (y == 1 or y == 6):
      self.piece = p.Pawn(colour)
    elif (x == 0 or x == 7):
      self.piece = p.Rook(colour)
    elif (x == 1 or x == 6):
      self.piece = p.Knight(colour)
    elif (x == 2 or x == 5):
      self.piece = p.Bishop(colour)
    elif (x == 3):
      self.piece = p.Queen(colour)
    else:
      self.piece = p.King(colour)

# draws a section of the board, with a piece if applicable
def drawSquare(i, j):
  screen = pygame.display.get_surface() 
  # get the offsets
  offsetw = (screen.get_width() - SQUARE_SIZE*8) / 2
  offseth = (screen.get_height() - SQUARE_SIZE*8) / 2
  # get the rectangle
  gridRect = pygame.Rect(i*SQUARE_SIZE+offsetw,
    j*SQUARE_SIZE+offseth,SQUARE_SIZE,SQUARE_SIZE)
  # draw the grid
  if ((i + j) % 2 == 1):
    # draw a darker square every other square
    pygame.draw.rect(screen, (150,150,150), gridRect)
  pygame.draw.rect(screen, (0,0,0), gridRect, 1)
  
  if (Board[i][j].piece != None):
    # draw the piece
    colour = Board[i][j].piece.iColour
    piece = Board[i][j].piece.iPiece
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
  
  # all squares
  for i in range(8):
    for j in range(8):
      Board[i][j] = Square(i,j)  
  drawBoard()
  
def squareClicked(i, j):
  print("x ",i,", y ",j)
  
def initBoard():
  global Board

  # load the images
  p.LoadPieceImages()
  # init the board
  Board = [[None for x in range(8)] for y in range(8)]
  resetBoard()