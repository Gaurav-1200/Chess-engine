from const import *
from square import Square
from piece import *
from move import Move
import copy 
class Board:
    def __init__(self):
        self.squares=[[0,0,0,0,0,0,0,0] for i in range(COLS)]
        self._create()
        self._add_pieces('white')
        self._add_pieces('black')
        self.last_move = None


    def knight_moves(self,row,col,piece):
        dx=[-2, -1, 1,  2,  2,  1,  -1, -2]
        dy=[1,  2,  2,  1,  -1, -2, -2, -1]
        # possible_moves =[(row + dx[i],col+dy[i]) for i in range(8) if (row+dx[i]>=0 and row+dx[i]<8 and col+dy[i]>=0 and col+dy[i]<8)]
        possible_moves =[(row + dx[i],col+dy[i]) for i in range(8) if isValidPos(row+dx[i],col+dy[i])]
        for possible_move in possible_moves:
            if self.squares[possible_move[0]][possible_move[1]].is_empty_or_rival_piece(piece.color):  ##check
                #Create square for move
                initial = Square(row,col,piece)
                final_piece = self.squares[possible_move[0]][possible_move[1]].piece 
                final = Square(possible_move[0],possible_move[1],final_piece)

                #create Move
                move = Move(initial=initial,final=final)
                piece.add_move(move)
        print(possible_moves)
        
    def pawn_moves(self, row, col, piece):
        steps = 1 if piece.moved else 2

        #vertical mvmnt
        start =  row + piece.dir
        end = row + ((steps+1) *  piece.dir)
        for possible_move_row in range(start,end,piece.dir):  #as range is [)
            if isValidPos(possible_move_row,col):
                if(self.squares[possible_move_row][col].is_empty()):
                    #Create square for move
                    initial = Square(row,col,piece)
                    final = Square(possible_move_row,col)

                    #create Move
                    move = Move(initial=initial,final=final)
                    piece.add_move(move)
                else :   #blocked
                    break
            else:  #blocked
                break 
        
        #diagonal mvmnt
        possible_move_row = row + piece.dir
        possible_move_cols = [col-1, col+1]

        for possible_move_col in possible_move_cols:
            if isValidPos(possible_move_row, possible_move_col):
                if(self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color)):
                    #Create square for move
                    initial = Square(row,col,piece)
                    final_piece = self.squares[possible_move_row][possible_move_col].piece 
                    final = Square(possible_move_row,possible_move_col,final_piece)

                    #create Move
                    move = Move(initial=initial,final=final)
                    piece.add_move(move)
                else:
                    break
            else : break
        
        #en_passant moves
        r = 3 if piece.color == 'white' else 5
        finalRow = 2 if piece.color == 'white' else 6

        #left en_passant
        if isValidPos(row,col-1) and r==row:
            if(self.squares[row][col-1].has_rival_piece(piece.color)):
                p = self.squares[row][col-1].piece
                if isinstance(p, Pawn):
                    if p.en_passant:
                        initial = Square(row, col)
                        final = Square(finalRow,col-1,p)
                        move = Move(initial,final)
                        piece.add_move(move)
        #right en_passant
        if isValidPos(row,col+1) and r==row:
            if(self.squares[row][col+1].has_rival_piece(piece.color)):
                p = self.squares[row][col+1].piece
                if isinstance(p, Pawn):
                    if p.en_passant:
                        initial = Square(row, col)
                        final = Square(finalRow,col+1,p)
                        move = Move(initial,final)
                        piece.add_move(move)
    


        
    def straight_line_moves(self, row, col, piece,increments):
        for incr in increments:
            row_incr, col_incr = incr
            possible_move_row =  row + row_incr
            possible_move_col =  col + col_incr

            while(1):
                if isValidPos(possible_move_row, possible_move_col):
                    initial = Square(row,col,piece)
                    final_piece = self.squares[possible_move_row][possible_move_col].piece
                    final = Square(possible_move_row,possible_move_col,final_piece)

                    #create Move
                    move = Move(initial=initial,final=final)
                    if(self.squares[possible_move_row][possible_move_col].is_empty()):
                        piece.add_move(move)
                        
                    elif(self.squares[possible_move_row][possible_move_col].has_rival_piece(piece.color)):
                        piece.add_move(move)
                        break
                    elif(self.squares[possible_move_row][possible_move_col].has_team_piece(piece.color)):
                        break
                else:
                    break
                possible_move_row = possible_move_row + row_incr
                possible_move_col = possible_move_col + col_incr
                    
    def king_moves(self,row,col,piece):
        dx = [0,1,1,1,0,-1,-1,-1]
        dy = [1,1,0,-1,-1,-1,0,1]

        possible_moves =[(row + dx[i],col+dy[i]) for i in range(8) if isValidPos(row+dx[i],col+dy[i])]
        for possible_move in possible_moves:
            if self.squares[possible_move[0]][possible_move[1]].is_empty_or_rival_piece(piece.color):  ##check
                #Create square for move
                initial = Square(row,col,piece)
                final = Square(possible_move[0],possible_move[1],piece)

                #create Move
                move = Move(initial=initial,final=final)
                piece.add_move(move)
        
        #Castling Moves
        if piece.moved == False:
            #King Castle
            right_rook = self.squares[row][7].piece
            if isinstance(right_rook, Rook):
                if right_rook.moved == False:
                    for c in range(5,7):
                        if self.squares[row][c].has_piece():   #Castling not possible, pieces in b/w
                            break
                        if c==6: #last col, valid castling
                            piece.right_rook = right_rook
                            #rook Move
                            initial = Square(row,7)
                            final = Square(row,5)
                            move = Move(initial, final)
                            right_rook.add_move(move)
                            #king move
                            initial = Square(row,col)
                            final =Square(row,6)
                            move = Move(initial,final)
                            piece.add_move(move)

            #Queen Castle
            left_rook = self.squares[row][0].piece
            if isinstance(left_rook, Rook):
                if left_rook.moved == False:
                    for c in range(1,4):
                        if self.squares[row][c].has_piece():   #Castling not possible, pieces in b/w
                            break
                        if c==3: #last col, valid castling
                            piece.left_rook = left_rook
                            #rook Move
                            initial = Square(row,0)
                            final = Square(row,3)
                            move = Move(initial, final)
                            left_rook.add_move(move)
                            #king move
                            initial = Square(row,col)
                            final =Square(row,2)
                            move = Move(initial,final)
                            piece.add_move(move)

    def calc_moves(self,piece, row, col):
        '''
            Calculates all the possible moves of an specific piece on a specific position
        '''
        # self.knight_moves(row,col,piece)
        if piece.name == PAWN:
            self.pawn_moves(row,col,piece)
        elif piece.name == KNIGHT:
            self.knight_moves(row,col,piece)
        elif piece.name == BISHOP:
            self.straight_line_moves(row,col,piece,[(-1,1),(-1,-1),(1,1),(1,-1)])
        elif piece.name == ROOK:
            self.straight_line_moves(row,col,piece,[(-1,0),(0,1),(1,0),(0,-1)])
        elif piece.name == QUEEN:
            self.straight_line_moves(row,col,piece,[(-1,0),(0,1),(1,0),(0,-1),(-1,1),(-1,-1),(1,1),(1,-1)])
        elif piece.name == KING:
            self.king_moves(row,col,piece)

    def check_promotion(self,piece,finalPos):
        if finalPos.row ==0 or finalPos.row == 7:
            self.squares[finalPos.row][finalPos.col].piece = Queen(piece.color)

    def castling(self,initial, final):
        return abs(initial.col - final.col) == 2
    
    def set_true_en_passant(self, piece):
        if not isinstance(piece, Pawn):
            return
        
        for row in range(ROWS):
            for col in range(COLS):
                if isinstance(self.squares[row][col].piece, Pawn):
                    self.squares[row][col].piece.en_passant = False   #Remaing Pawn ka False

        piece.en_passant = True   #last wale ka sirf true;
    
    def in_check(self,piece,move):
        temp_piece = copy.deepcopy(piece)
        temp_board = copy.deepcopy(self)
        temp_board.move(temp_piece,move)

        for row in range(ROWS):
            for col in range(COLS):
                if temp_board.squares[row][col].has_rival_piece(temp_piece.color):
                    rival_piece = temp_board.squares[row][col].piece
                    temp_board.calc_moves(rival_piece,row,col)
                    for mv in rival_piece.moves:
                        if isinstance(mv.final.piece,King):
                            return True
        
        return False

    def move(self,piece,move):
        initial = move.initial
        final = move.final

        en_passant_empty = self.squares[final.row][final.col].is_empty()

        #update board
        self.squares[initial.row][initial.col].piece = None
        self.squares[final.row][final.col].piece = piece

        if piece.name==PAWN:
            #en_passant_Capture
            diff = final.col -initial.col  #left -1, right +1 , straight = 0
            if diff !=0 and en_passant_empty:
                self.squares[initial.row][initial.col + diff].piece = None
                self.squares[final.row][final.col].piece = piece
            
            #pawn promotion
            else:
                self.check_promotion(piece,final)

        #King Castling
        if piece.name==KING:
            if self.castling(initial,final):
                rook = piece.left_rook if piece.left_rook != None else piece.right_rook
                self.move(rook,rook.moves[-1])

        piece.moved = True
        piece.clear_moves()

        self.last_move = move

    def valid_moves(self,piece,move):
        return move in piece.moves
    

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