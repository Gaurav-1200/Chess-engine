from const import *
from square import Square
from piece import *
from move import Move
class Board:
    def __init__(self):
        self.squares=[[0,0,0,0,0,0,0,0] for i in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')


    def knight_moves(self,row,col,piece):
        dx=[-2, -1, 1,  2,  2,  1,  -1, -2]
        dy=[1,  2,  2,  1,  -1, -2, -2, -1]
        # possible_moves =[(row + dx[i],col+dy[i]) for i in range(8) if (row+dx[i]>=0 and row+dx[i]<8 and col+dy[i]>=0 and col+dy[i]<8)]
        possible_moves =[(row + dx[i],col+dy[i]) for i in range(8) if isValidPos(row+dx[i],col+dy[i])]
        for possible_move in possible_moves:
            if self.squares[possible_move[0]][possible_move[1]].is_empty_or_rival_piece(piece.color):  ##check
                #Create square for move
                initial = Square(row,col,piece)
                final = Square(possible_move[0],possible_move[1],piece)

                #create Move
                move = Move(initial=initial,final=final)
                piece.add_move(move)




            

        print(possible_moves)


    def calc_moves(self,piece, row, col):
        '''
            Calculates all the possible moves of an specific piece on a specific position
        '''
        # self.knight_moves(row,col,piece)
        if piece.name == PAWN:
            pass
        elif piece.name == KNIGHT:
            self.knight_moves(row,col,piece)
        elif piece.name == BISHOP:
            pass
        elif piece.name == ROOK:
            pass
        elif piece.name == QUEEN:
            pass
        elif piece.name == KING:
            pass

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


