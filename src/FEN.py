from const import *
from board import Board
from square import Square
from piece import Piece


class FEN:
    def __init__(self):
        print("FEN INITED-------------------")
        # self.board = board

    def convertBoardtoCharBd(self,board):
        charBd = [0,0,0,0,0,0,0,0]
        for i in range(ROWS):
            row=[0]*8
            for j in range(COLS):
                if board.squares[i][j].piece is not None:
                    row[j]= board.squares[i][j].piece.name[0].upper() if board.squares[i][j].piece.color=='white' else board.squares[i][j].piece.name[0].lower()
                else:
                    row[j]='.'
            charBd[i]=row
        return charBd

    def convertBoardtoFEN(self,board,next_player):
        print("We Came here ####################")
        charBd = self.convertBoardtoCharBd(board)
        fen = []

        #Get Pieces
        for row in charBd:
            empty_count = 0
            fen_row = ""
            for cell in row:
                if cell == '.':
                    empty_count += 1
                else:
                    if empty_count > 0:
                        fen_row += str(empty_count)
                        empty_count = 0
                    fen_row += cell
            if empty_count > 0:
                fen_row += str(empty_count)
            fen.append(fen_row)

        fen_string = '/'.join(fen)
        
        #check for en-passant
        EnPassant = None
        last_moved_piece = None
        # print("---------->",board.last_move)
        # if(board.last_move != None):
        fx, fy = board.last_move.final.row, board.last_move.final.col
        last_moved_piece = board.squares[fx][fy].piece 
        if(last_moved_piece != None and last_moved_piece.name == PAWN and last_moved_piece.en_passant == True):
            fx  = fx + 1 if last_moved_piece.color == 'white' else fx - 1
            ch = chr(ord('a') + fx)
            EnPassant = str(ch)+str(fy)

        #Get active color
        fen_string += ' '
        fen_string += 'w' if next_player == 'white' else 'b'

        fen_string += ' '
        fen_string += 'kq' if board.hasBlackCastled == False else "--"
        fen_string += 'KQ' if board.hasWhiteCastled == False else "--"

        fen_string += ' '
        fen_string += '-' if EnPassant==None else EnPassant

        fen_string += ' '
        fen_string += str(board.numHalfMoves) if board.numHalfMoves<=0 else "0"

        fen_string += ' '
        fen_string += str(board.numTotalMoves) if board.numTotalMoves>0 else "1"

        print("FEN STRING IS ",fen_string)

        return fen_string


