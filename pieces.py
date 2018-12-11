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

# subclasses
class Pawn:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = PAWN_ENUM
    
class Rook:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = ROOK_ENUM
    
class Knight:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = KNIGHT_ENUM
    
class Bishop:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = BISHOP_ENUM
    
class Queen:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = QUEEN_ENUM
    
class King:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = KING_ENUM