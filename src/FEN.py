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
        
        #Get active color
        fen_string += ' '
        fen_string += 'w' if next_player == 'white' else 'b'

        fen_string += ' '
        fen_string += 'kq' if board.hasBlackCastled == False else "--"
        fen_string += 'KQ' if board.hasWhiteCastled == False else "--"

        fen_string += ' '
        fen_string += str(board.numHalfMoves)

        fen_string += ' '
        fen_string += str(board.numTotalMoves)

        print("FEN STRING IS ",fen_string)

        return fen_string


