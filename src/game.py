import pygame
from board import Board
from dragger import Dragger
from const import *

class Game:
    def __init__(self):
        self.board= Board()
        self.dragger= Dragger()
        self.next_player = 'white'
        self.hovered_square = None

    def show_bg(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if((row+col)%2==0):
                    color = (234 ,235,200) #light green
                else:
                    color =( 119,154,88) #dark green

                rect =(col*SQSIZE,row*SQSIZE,SQSIZE,SQSIZE)
                pygame.draw.rect(surface,color,rect)

    def show_pieces(self,surface):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board.squares[row][col].has_piece():
                    piece =  self.board.squares[row][col].piece
                    if piece is not self.dragger.piece:
                        piece.set_texture(size=80)
                        #render all except the one you are dragging
                        img = pygame.image.load(piece.texture)
                        img_center = col*SQSIZE + SQSIZE  // 2, row*SQSIZE + SQSIZE // 2
                        piece.texture_rect = img.get_rect(center = img_center)
                        surface.blit(img,piece.texture_rect)

    def show_moves(self,surface):
        if self.dragger.dragging:
            piece= self.dragger.piece

            for move in piece.moves:
                #color
                color = '#C86464' if ((move.final.row + move.final.col) %2 ==0) else '#C84646'
                #rect
                rect = (move.final.col*SQSIZE, move.final.row*SQSIZE,SQSIZE,SQSIZE)
                #blit
                pygame.draw.rect(surface,color,rect)

            # possible_moves =self.board.calc_moves(piece=piece,row=self.dragger.initial_row,col=self.dragger.initial_col)
    def show_last_move(self,surface):
        if self.board.last_move:
            initial = self.board.last_move.initial
            final = self.board.last_move.final
            # piece = self.board.last_move.piece
            
            for pos in [initial,final]:
                #color
                color = (244,247,116) if ((pos.row + pos.col) %2 ==0) else (172,195,51)
                #rect
                rect = (pos.col*SQSIZE, pos.row*SQSIZE,SQSIZE,SQSIZE)
                #blit
                pygame.draw.rect(surface,color,rect)
            
    def show_hovered_square(self,surface):
        if self.hovered_square:
            #color
            color = (180,180,180) 
            #rect
            rect = (self.hovered_square.col*SQSIZE, self.hovered_square.row*SQSIZE,SQSIZE,SQSIZE)
            #blit
            pygame.draw.rect(surface,color,rect,width=3)


    def next_turn(self):
        self.board.numTotalMoves += 1
        self.board.numHalfMoves += 1
        self.next_player = 'white' if self.next_player == 'black' else 'black'
        return self.next_player
    
    def set_hover(self,row,col):
        self.hovered_square = self.board.squares[row][col]

    def reset_game(self):
        self.__init__()