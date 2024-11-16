class Square:
   
    def __init__(self,row=None,col=None,piece=None):
        self.row=row
        self.col=col
        self.piece=piece

    def __eq__(self,other):
        return self.row == other.row and self.col == other.col 

    def has_piece(self):
        return self.piece!=None
    
    def is_empty(self):
        return self.piece == None
    
    def has_rival_piece(self,color):
        return self.has_piece() and  self.piece.color != color
    
    def has_team_piece(self,color):
        return self.has_piece() and  self.piece.color == color
    
    def is_empty_or_rival_piece(self,color):
        return self.is_empty() or self.has_rival_piece(color)
       