import pygame
import sys
from game import Game
from piece import Piece

from const import *

class Main:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode( (WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
    
    def mainloop(self):
        screen =self.screen
        game= self.game
        board = self.game.board
        dragger =self.game.dragger

        # p=Piece(name=KNIGHT,color='white',value=1)
        # board.calc_moves(row=6,col=6,piece=p)
        while True:
            game.show_bg(screen)
            game.show_moves(screen)
            game.show_pieces(screen)

            if dragger.dragging:
                dragger.update_blit(screen)

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:  #click
                    print("6666666666666666666666")
                    dragger.update_mouse(event.pos)
                    clicked_row = dragger.mouseY // SQSIZE
                    clicked_col = dragger.mouseX // SQSIZE
                    if board.squares[clicked_row][clicked_col].has_piece():
                        piece = board.squares[clicked_row][clicked_col].piece
                        board.calc_moves(piece,clicked_row,clicked_col)
                        dragger.save_initial(event.pos)
                        dragger.drag_piece(piece)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)


                elif event.type == pygame.MOUSEMOTION: #move
                    if dragger.dragging:
                        print("888888888888888888888")
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_moves(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                        
                elif event.type == pygame.MOUSEBUTTONUP:  #release
                    dragger.undrag_piece()
                elif event.type== pygame.QUIT:  #quit
                    pygame.quit()
                    sys.exit()

            pygame.display.update()


main =  Main()
main.mainloop()