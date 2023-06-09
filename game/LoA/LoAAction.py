class LinesOfActionAction:
    """
    a Lines of Action action is simple - it only takes the value of the column to play
    """
    __col: int
    __row: int 
    __old_col: int
    __old_row: int

    def __init__(self, col: int, row: int, old_col: int, old_row: int):
        self.__col = col
        self.__row = row        
        self.__old_col = old_col
        self.__old_row = old_row
        
    def get_col(self):
        return self.__col

    def get_row(self):
        return self.__row
      
    def get_old_col(self):
        return self.__old_col
    
    def get_old_row(self):
        return self.__old_row
    
 