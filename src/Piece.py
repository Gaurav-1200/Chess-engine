import os
from const import *
class Piece:
    def __init__(self,name,color,value,texture=None,texture_rect=None):
        self.name=name
        self.color=color

        value_sign = 1 if color == 'white' else -1
        self.value=value*value_sign

        self.moves=[]
        self.moved=False

        self.texture=texture
        self.set_texture()
        self.texture_rect =texture_rect

    def set_texture(self,size=80):
        self.texture= os.path.join(
            f'assets/images/imgs-{size}px/{self.color}_{self.name}.png'
        )

    def  add_moves(self,move):
        self.moves.append(move)

class Pawn(Piece):
    def __init__(self,color):
        self.dir = -1 if color=='white' else 1
        super().__init__(PAWN,color,1.0)


class Knight(Piece):
    def __init__(self,color):
        super().__init__(KNIGHT,color,3.0)

class Rook(Piece):
    def __init__(self,color):
        super().__init__(ROOK,color,5.0)

class Bishop(Piece):
    def __init__(self,color):
        super().__init__(BISHOP,color,3.001)

class Queen(Piece):
    def __init__(self,color):
        super().__init__(QUEEN,color,9.0)

class King(Piece):
    def __init__(self,color):
        super().__init__(KING,color,10000.0)