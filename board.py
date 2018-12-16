import pygame
import ai
import pieces as p
import enumerations as e

# global constants
SQUARE_SIZE = 60

# global variables
Board = [[]]

class Square:
  piece = None
  status = e.NONE_ENUM

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
def drawSquare(x, y):
  screen = pygame.display.get_surface() 
  # get the offsets
  offsetw = (screen.get_width() - SQUARE_SIZE*8) / 2
  offseth = (screen.get_height() - SQUARE_SIZE*8) / 2
  # get the rectangle
  gridRect = pygame.Rect(x*SQUARE_SIZE+offsetw,
    y*SQUARE_SIZE+offseth,SQUARE_SIZE,SQUARE_SIZE)
  # draw the grid
  if (Board[x][y].status == e.SELECTED_ENUM):
    pygame.draw.rect(screen, (255,255,0), gridRect)
  elif (Board[x][y].status == e.INRANGE_ENUM):
    pygame.draw.rect(screen, (0,255,255), gridRect)
  elif (Board[x][y].status == e.THREATENDED_ENUM):
    pygame.draw.rect(screen, (255,0,0), gridRect)
  elif ((x + y) % 2 == 1):
    pygame.draw.rect(screen, (150,150,150), gridRect)
  else:
    pygame.draw.rect(screen, (255,255,255), gridRect)
  pygame.draw.rect(screen, (0,0,0), gridRect, 1)
  
  if (Board[x][y].piece != None):
    # draw the piece
    colour = Board[x][y].piece.iColour
    piece = Board[x][y].piece.iPiece
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
      if (Board[i][j].status != e.NONE_ENUM):
        Board[i][j].status = e.NONE_ENUM
        drawSquare(i,j)
        
# returns true if a piece was moved
def movePiece(x, y):
  global Board
  # cycle over all sqaures
  for i in range(8):
    for j in range(8):
      if (Board[i][j].status == e.SELECTED_ENUM):
        # move this piece
        Board[x][y].piece = Board[i][j].piece
        Board[i][j].piece = None
        Board[x][y].piece.bMoved = True
        clearHighlighting()
        return True
  return False

# returns true if the click takes a turn
def squareClicked(x, y):
  global Board
  bMoved = False
  
  if (Board[x][y].status == e.SELECTED_ENUM):
    # square already selected, deselect
    Board[x][y].status = e.NONE_ENUM
    clearHighlighting()
  elif (Board[x][y].status == e.INRANGE_ENUM or
        Board[x][y].status == e.THREATENDED_ENUM):
    # moves the selected piece to this square
    bMoved = movePiece(x,y)    
  elif (Board[x][y].piece != None and
    Board[x][y].piece.iColour == 1):
    # deselect any old squares
    clearHighlighting()
    # select this one
    Board[x][y].status = e.SELECTED_ENUM
    
    # get the list of moves
    for coord in Board[x][y].piece.getMoves(x, y, Board):
      xpos = coord[0]
      ypos = coord[1]
      if (Board[xpos][ypos].piece == None):
        Board[xpos][ypos].status = e.INRANGE_ENUM
      else:
        Board[xpos][ypos].status = e.THREATENDED_ENUM
      drawSquare(xpos,ypos)
  
  drawSquare(x, y)
  return bMoved
  
# returns true if the AI was able to play
def takeTurn():
  m = ai.getBestMove(Board)
  if (m == None):
    return False
  Board[m.movex][m.movey].piece = Board[m.x][m.y].piece
  Board[m.x][m.y].piece = None
  drawSquare(m.x, m.y)
  drawSquare(m.movex, m.movey)
  return True
  
def initBoard():
  global Board

  # load the images
  p.loadPieceImages()
  # init the board
  Board = [[None for x in range(8)] for y in range(8)]
  resetBoard()