import pygame, os
import enumerations as e

# array of loaded chess piece images
PieceImages = [[None for x in range(6)] for y in range(2)]

def loadPieceImages():
  for i in range(2):
    if (i == e.BLACK_ENUM):
      imageFileName = "dt60.png"
    else:
      imageFileName = "lt60.png"
    PieceImages[i][e.PAWN_ENUM]   = pygame.image.load(os.path.join("images", "pieces", "Chess_p"+imageFileName))
    PieceImages[i][e.ROOK_ENUM]   = pygame.image.load(os.path.join("images", "pieces", "Chess_r"+imageFileName))
    PieceImages[i][e.KNIGHT_ENUM] = pygame.image.load(os.path.join("images", "pieces", "Chess_n"+imageFileName))
    PieceImages[i][e.BISHOP_ENUM] = pygame.image.load(os.path.join("images", "pieces", "Chess_b"+imageFileName))
    PieceImages[i][e.QUEEN_ENUM]  = pygame.image.load(os.path.join("images", "pieces", "Chess_q"+imageFileName))    
    PieceImages[i][e.KING_ENUM]   = pygame.image.load(os.path.join("images", "pieces", "Chess_k"+imageFileName))    

# super class
class Piece:
  def __init__(self, iColour):
    self.iColour = iColour
    self.bMoved = False
  
  # removes any moves that target the same colour  
  def trimMoves(self, Moves, Board):
    Moves = [m for m in Moves if (Board[m[0]][m[1]].piece == None or 
      Board[m[0]][m[1]].piece.iColour != self.iColour)]
    return Moves    

# subclasses
class Pawn:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = e.PAWN_ENUM
    
  def getMoves(self, x, y, Board):
    Moves = []
    if (self.iColour == e.WHITE_ENUM):
      if (y > 0 and Board[x][y-1].piece == None):
        Moves.append((x, y-1))
      if (y > 1 and not self.bMoved
        and Board[x][y-2].piece == None):
        Moves.append((x, y-2))
      # taking pieces
      if (y > 0 and x > 0 and Board[x-1][y-1].piece != None):
        Moves.append((x-1, y-1))
      if (y > 0 and x < 7 and Board[x+1][y-1].piece != None):
        Moves.append((x+1, y-1))
    else:
      if (y < 7 and Board[x][y+1].piece == None):
        Moves.append((x, y+1))
      if (y < 6 and not self.bMoved
        and Board[x][y+2].piece == None):
        Moves.append((x, y+2))
      # taking pieces
      if (y < 7 and x > 0 and Board[x-1][y+1].piece != None):
        Moves.append((x-1, y+1))
      if (y < 7 and x < 7 and Board[x+1][y+1].piece != None):
        Moves.append((x+1, y+1))
      
    Moves = Piece.trimMoves(self, Moves, Board)
    return Moves
    
class Rook:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = e.ROOK_ENUM
    
  def getMoves(self, x, y, Board):
    Moves = []
    for i in range(x+1, 8):
      Moves.append((i, y))
      if (Board[i][y].piece != None):
        break
    for i in range(x-1, -1, -1):
      Moves.append((i, y))
      if (Board[i][y].piece != None):
        break
    for i in range(y+1, 8):
      Moves.append((x, i))
      if (Board[x][i].piece != None):
        break
    for i in range(y-1, -1, -1):
      Moves.append((x, i))
      if (Board[x][i].piece != None):
        break
    
    Moves = Piece.trimMoves(self, Moves, Board)
    return Moves
    
class Knight:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = e.KNIGHT_ENUM
    
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
    self.iPiece = e.BISHOP_ENUM
    
  def getMoves(self, x, y, Board):
    Moves = []
    offset = 1
    while (x-offset >= 0 and y-offset >= 0):
      Moves.append((x-offset, y-offset))
      if (Board[x-offset][y-offset].piece != None):
        break;
      offset += 1
    offset = 1
    while (x-offset >= 0 and y+offset <= 7):
      Moves.append((x-offset, y+offset))
      if (Board[x-offset][y+offset].piece != None):
        break;
      offset += 1
    offset = 1
    while (x+offset <= 7 and y-offset >= 0):
      Moves.append((x+offset, y-offset))
      if (Board[x+offset][y-offset].piece != None):
        break;
      offset += 1
    offset = 1
    while (x+offset <= 7 and y+offset <= 7):
      Moves.append((x+offset, y+offset))
      if (Board[x+offset][y+offset].piece != None):
        break;
      offset += 1
    
    Moves = Piece.trimMoves(self, Moves, Board)
    return Moves
    
class Queen:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = e.QUEEN_ENUM
    
  def getMoves(self, x, y, Board):
    # combo of rook and bishop moves
    Moves = Rook.getMoves(self, x, y, Board)
    Moves.extend(Bishop.getMoves(self, x, y, Board))
    return Moves
    
class King:
  def __init__(self, iColour):
    Piece.__init__(self, iColour)
    self.iPiece = e.KING_ENUM
    
  def getMoves(self, x, y, Board):
    Moves = []
    for i in range (-1, 2):
      for j in range (-1, 2):
        if ((i == 0 and j == 0) or
            x+i > 7 or x+i < 0 or
            y+j > 7 or y+j < 0):
          continue
        Moves.append((x+i, y+j))
    Moves = Piece.trimMoves(self, Moves, Board)
    return Moves