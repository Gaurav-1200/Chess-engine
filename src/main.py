import pygame
import sys
from game import Game
from piece import Piece
from square import Square
from move import Move
from FEN import *

from const import *

class Main:
    def __init__(self):
        pygame.init()
        self.FEN=FEN()
        self.screen = pygame.display.set_mode( (WIDTH,HEIGHT))
        pygame.display.set_caption('Chess')
        self.game = Game()
    
    def mainloop(self):
        screen =self.screen
        game= self.game
        board = self.game.board
        dragger =self.game.dragger
        wasMoveMade = False

        # p=Piece(name=KNIGHT,color='white',value=1)
        # board.calc_moves(row=6,col=6,piece=p)
        while True:
            game.show_bg(screen)
            game.show_last_move(screen)
            game.show_moves(screen)
            game.show_hovered_square(screen)
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
                        #is Valid turn color piece ?
                        if piece.color == game.next_player:
                            board.calc_moves(piece,clicked_row,clicked_col)
                            dragger.save_initial(event.pos)
                            dragger.drag_piece(piece)
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_moves(screen)
                            game.show_hovered_square(screen)
                            game.show_pieces(screen)


                elif event.type == pygame.MOUSEMOTION: #move
                    motion_row = event.pos[1] // SQSIZE
                    motion_col = event.pos[0] //SQSIZE
                    game.set_hover(motion_row,motion_col)
                    if dragger.dragging:
                        print("888888888888888888888")
                        dragger.update_mouse(event.pos)
                        game.show_bg(screen)
                        game.show_last_move(screen)
                        game.show_moves(screen)
                        game.show_hovered_square(screen)
                        game.show_pieces(screen)
                        dragger.update_blit(screen)
                        
                elif event.type == pygame.MOUSEBUTTONUP:  #release
                    if dragger.dragging:
                        dragger.update_mouse(event.pos)
                        released_row = dragger.mouseY // SQSIZE
                        released_col = dragger.mouseX // SQSIZE

                        initial = Square(dragger.initial_row,dragger.initial_col)
                        final =  Square(released_row,released_col)
                        move  = Move(initial,final)

                        if board.valid_moves(dragger.piece,move):
                            board.move(dragger.piece,move)
                            game.show_bg(screen)
                            game.show_last_move(screen)
                            game.show_hovered_square(screen)

                            game.show_pieces(screen)
                            wasMoveMade = True
                            #change player
                            game.next_turn()

                    dragger.undrag_piece()
                elif event.type== pygame.QUIT:  #quit
                    pygame.quit()
                    sys.exit()
                
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        game.reset_game()
                        game= self.game
                        board = self.game.board
                        dragger =self.game.dragger

            pygame.display.update()
            if(wasMoveMade):
                print(self.FEN.convertBoardtoFEN(game.board,game.next_player))
                wasMoveMade = False


main =  Main()
main.mainloop()