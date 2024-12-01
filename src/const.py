WIDTH = 800
HEIGHT = 800

ROWS =8
COLS =8
SQSIZE = WIDTH // COLS

PAWN ="pawn"
KNIGHT ="knight"
ROOK ="rook"
QUEEN ="queen"
BISHOP = "bishop"
KING ="king"

def isValidPos(x,y):
    x = int(x)
    y = int(y)
    return not(x<0 or y<0 or x>=ROWS or y>=COLS)
