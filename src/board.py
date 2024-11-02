from const import *
from square import Square
from Piece import *
class Board:
    def __init__(self):
        self.squares=[[0,0,0,0,0,0,0,0] for i in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')

    def _create(self):
        for i in range(ROWS):
            for j in range(COLS):
                self.squares[i][j]=Square(i,j)
        


    def _add_pieces(self,color):
        row_pawn, row_other = (6,7) if color == 'white' else (1,0)

        #Pawn
        for col in range(COLS):
            self.squares[row_pawn][col] = Square(row_pawn,col,Pawn(color))
        
        #Knights
        for col in (1,6):
            self.squares[row_other][col]= Square(row_other,col,Knight(color))
        
        #Bishops
        for col in (2,5):
            self.squares[row_other][col]= Square(row_other,col,Bishop(color))

        #Queens
        for col in [3]:
            self.squares[row_other][col]= Square(row_other,col,Queen(color))
        
        #Rook
        for col in (0,7):
            self.squares[row_other][col]= Square(row_other,col,Rook(color))
        
        #King
        for col in [4]:
            self.squares[row_other][col]= Square(row_other,col,King(color))

b= Board()
b._create()
