import pygame, os

# enum defines
# colours 
BLACK_ENUM = 0
WHITE_ENUM = 1
# pieces
PAWN_ENUM = 0
ROOK_ENUM = 1
KNIGHT_ENUM = 2
BISHOP_ENUM = 3
QUEEN_ENUM = 4
KING_ENUM = 5

# array of loaded chess piece images
PieceImages = [[None for x in range(6)] for y in range(2)]

def LoadPieceImages():
  for i in range(2):
    if (i == BLACK_ENUM):
      imageFileName = "dt60.png"
    else:
      imageFileName = "lt60.png"
    PieceImages[i][PAWN_ENUM]   = pygame.image.load(os.path.join("images", "pieces", "Chess_p"+imageFileName))
    PieceImages[i][ROOK_ENUM]   = pygame.image.load(os.path.join("images", "pieces", "Chess_r"+imageFileName))
    PieceImages[i][KNIGHT_ENUM] = pygame.image.load(os.path.join("images", "pieces", "Chess_n"+imageFileName))
    PieceImages[i][BISHOP_ENUM] = pygame.image.load(os.path.join("images", "pieces", "Chess_b"+imageFileName))
    PieceImages[i][QUEEN_ENUM]  = pygame.image.load(os.path.join("images", "pieces", "Chess_q"+imageFileName))    
    PieceImages[i][KING_ENUM]   = pygame.image.load(os.path.join("images", "pieces", "Chess_k"+imageFileName))    

# super class
class Piece:
  def __init__(self, iColour):
    self.iColour = iColour
  
  # removes any moves that target the same colour  
  def trimMoves(self, Moves, Board):
    for m in Moves:
      x = m[0]
      y = m[1]
      if (Board[x][y].piece != None and 
          Board[x][y].piece.iColour == self.iColour):
        Moves.remove(m)
    return Moves    

# subclasses
class Pawn:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = PAWN_ENUM
    self.bMoved = False
    
  def getMoves(self, x, y, Board):
    Moves = []
    if (y > 0 and Board[x][y-1].piece == None):
      Moves.append((x, y-1))
    if (y > 1 and not self.bMoved
      and Board[x][y-2].piece == None):
      Moves.append((x, y-2))
    if (y > 0 and x > 0 and Board[x-1][y-1].piece != None):
      Moves.append((x-1, y-1))
    if (y > 0 and x < 7 and Board[x+1][y-1].piece != None):
      Moves.append((x+1, y-1))
      
    Moves = Piece.trimMoves(self, Moves, Board)
    return Moves
    
class Rook:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = ROOK_ENUM
    
  def getMoves(self, x, y, Board):
    Moves = []
    return Moves
    
class Knight:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = KNIGHT_ENUM
    
  def getMoves(self, x, y, Board):
    Moves = []
    if (y > 1 and x > 0):
      Moves.append((x-1, y-2))
    if (y > 1 and x < 7):
      Moves.append((x+1, y-2))
    if (y < 6 and x > 0):
      Moves.append((x-1, y+2))
    if (y < 6 and x < 7):
      Moves.append((x+1, y+2))
    if (x > 1 and y > 0):
      Moves.append((x-2, y-1))
    if (x > 1 and y < 7):
      Moves.append((x-2, y+1))
    if (x < 6 and y > 0):
      Moves.append((x+2, y-1))
    if (x < 6 and y < 7):
      Moves.append((x+2, y+1))
      
    Moves = Piece.trimMoves(self, Moves, Board)
    return Moves
    
class Bishop:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = BISHOP_ENUM
    
  def getMoves(self, x, y, Board):
    Moves = []
    return Moves
    
class Queen:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = QUEEN_ENUM
    
  def getMoves(self, x, y, Board):
    Moves = []
    return Moves
    
class King:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = KING_ENUM
    
  def getMoves(self, x, y, Board):
    Moves = []
    return Moves