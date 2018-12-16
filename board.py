import pygame

import pieces as p

# enum defines
# square status
NONE_ENUM = 0
SELECTED_ENUM = 1
INRANGE_ENUM = 2
THREATENDED_ENUM = 3

# global constants
SQUARE_SIZE = 60

# global variables
Board = [[]]

class Square:
  piece = None
  status = NONE_ENUM

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
  if (Board[i][j].status == SELECTED_ENUM):
    pygame.draw.rect(screen, (255,255,0), gridRect)
  elif (Board[i][j].status == INRANGE_ENUM):
    pygame.draw.rect(screen, (0,255,255), gridRect)
  elif (Board[i][j].status == THREATENDED_ENUM):
    pygame.draw.rect(screen, (255,0,0), gridRect)
  elif ((i + j) % 2 == 1):
    pygame.draw.rect(screen, (150,150,150), gridRect)
  else:
    pygame.draw.rect(screen, (255,255,255), gridRect)
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
  
# clears all highlighting
def clearHighlighting():
  global Board
  # cycle over all sqaures
  for i in range(8):
    for j in range(8):
      if (Board[i][j].status != NONE_ENUM):
        Board[i][j].status = NONE_ENUM
        drawSquare(i,j)
        
# returns the 
def movePiece(x, y):
  global Board
  # cycle over all sqaures
  for i in range(8):
    for j in range(8):
      if (Board[i][j].status == SELECTED_ENUM):
        # move this piece
        Board[x][y].piece = Board[i][j].piece
        Board[i][j].piece = None
        clearHighlighting()
  
def squareClicked(i, j):
  global Board
  if (Board[i][j].status == SELECTED_ENUM):
    # square already selected, deselect
    Board[i][j].status = NONE_ENUM
  elif (Board[i][j].status == INRANGE_ENUM):
    # moves the selected piece to this square
    movePiece(i,j)
  elif (Board[i][j].piece != None and
    Board[i][j].piece.iColour == 1):
    # deselect any old squares
    clearHighlighting()
    # select this one
    Board[i][j].status = SELECTED_ENUM
    
    # get the list of moves
    for coord in Board[i][j].piece.getMoves(i, j, Board):
      x = coord[0]
      y = coord[1]
      if (Board[x][y].piece == None):
        Board[x][y].status = INRANGE_ENUM
      else:
        Board[x][y].status = THREATENDED_ENUM
      drawSquare(x,y)
  
  drawSquare(i, j)
  
def initBoard():
  global Board

  # load the images
  p.LoadPieceImages()
  # init the board
  Board = [[None for x in range(8)] for y in range(8)]
  resetBoard()