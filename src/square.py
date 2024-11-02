class Square:
   
    def __init__(self,row=None,col=None,piece=None):
        self.row=row
        self.col=col
        self.piece=piece

    def has_piece(self):
        return self.piece!=None
       