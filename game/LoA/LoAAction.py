class LinesOfActionAction:
    """
    a Lines of Action action is simple - it only takes the value of the column to play
    """
    __col: int
    __row: int 

    def __init__(self, col: int, row: int):
        self.__col = col
        self.__row = row        
        
    def get_col(self):
        return self.__col

    def get_row(self):
        return self.__row
    
"""     class Cell():
  __col: int
  __row: int

  def __init(self, col: int, row: int):
    self.__col = col
    self.__row = row

  def get_col(self):
    return self.__col

  def get_row(self):
    return self.__row

class LinesOfActionAction():
  __old: Cell
  __new: Cell

  def __init__(self, old: Cell, new: Cell):
    self.__old = old
    self.__new = new

  def get_old_position(self):
    return self.__old

  def get_new_position(self):
    return self.__new """