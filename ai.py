import enumerations as e

# a class to hold potential moves and their scores
class EvaluatedMove():
  def __init__(self, x, y, movex, movey, Board):
    self.score = 0
    self.x = x
    self.y = y
    self.movex = movex
    self.movey = movey
    self.evaluate(movex, movey, Board)
    
  def evaluate(self, movex, movey, Board):
    if (Board[movex][movey].piece != None):
      # this move takes a piece
      # find out what piece and score accordingly
      if (Board[movex][movey].piece.iPiece == e.PAWN_ENUM):
        self.score += 10
      elif (Board[movex][movey].piece.iPiece == e.KNIGHT_ENUM):
        self.score += 30
      elif (Board[movex][movey].piece.iPiece == e.BISHOP_ENUM):
        self.score += 30
      elif (Board[movex][movey].piece.iPiece == e.ROOK_ENUM):
        self.score += 50
      elif (Board[movex][movey].piece.iPiece == e.QUEEN_ENUM):
        self.score += 90
      elif (Board[movex][movey].piece.iPiece == e.KING_ENUM):
        self.score += 9999
        
    # evaluate based on the move position
    self.score += movey
    # y = -|x| /\
    self.score += -abs(movex-4)

# take turn as the black player
# note this can return None
def getBestMove(Board):
  # hold a list of evaluated moves
  Moves = []
  iBestIndex = -1
  # cycle over all black pieces
  for i in range(8):
    for j in range(8):
      if (Board[i][j].piece != None and 
          Board[i][j].piece.iColour == e.BLACK_ENUM):
        # cycle over available moves
        for coord in Board[i][j].piece.getMoves(i, j, Board):
          newMove = EvaluatedMove(i,j,coord[0],coord[1],Board)
          Moves.append(newMove)
          if (iBestIndex == -1 or
              Moves[iBestIndex].score < newMove.score):
            iBestIndex = len(Moves) - 1
  
  # now we have all the evaluated moves
  # for now, return the one with the best score
  if (iBestIndex >= 0):
    return Moves[iBestIndex]
  else:
    return None