from typing import Optional

from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAResult import LinesOfActionResult
from game.state import State


class LinesOfActionState(State):

    EMPTY_CELL = -1

    def __init__(self, size: int = 8):
        super().__init__()

        if size != 8:
            raise Exception("the number of rows must be 8")
    
        self.__size = size

        """
        the dimensions of the board
        """
        """
        the grid
        """
        #Criar a grelha do jogo
        self.__grid = [[LinesOfActionState.EMPTY_CELL for _ in range(self.__size)] for _ in range(self.__size)]

        # Preencher com "x" na linha 0 e 7 da coluna 1 a 6
        for col in range(1, self.__size - 1):
            self.__grid[0][col] = 0
            self.__grid[7][col] = 0

        # Preencher com "o" na linha 1 a 6 e coluna 0 e 7
        for row in range(1, self.__size - 1):
            self.__grid[row][0] = 1
            self.__grid[row][7] = 1


        """
        counts the number of turns in the current game
        """
        self.__turns_count = 1

        """
        the index of the current acting player
        """
        self.__acting_player = 0

        """
        determine if a winner was found already 
        """
        self.__has_winner = False
        
    def check_winner(self, player):
        # Verificar linhas horizontais
        for row in range(self.__size):
            count = 0
            for col in range(self.__size):
                if self.__grid[row][col] == player:
                    count += 1
            if count == self.__size:
                return True

        # Verificar linhas verticais
        for col in range(self.__size):
            count = 0
            for row in range(self.__size):
                if self.__grid[row][col] == player:
                    count += 1
            if count == self.__size:
                return True

        # Verificar diagonal principal
        count = 0
        for i in range(self.__size):
            if self.__grid[i][i] == player:
                count += 1
        if count == self.__size:
            return True

        # Verificar diagonal secundária
        count = 0
        for i in range(self.__size):
            if self.__grid[i][self.__size - 1 - i] == player:
                count += 1
        if count == self.__size:
            return True

        return False

    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: LinesOfActionAction) -> bool:
        col = action.get_col()
        row = action.get_row()
        old_col = action.get_old_col()
        old_row = action.get_old_row()
        count_v = 0
        count_h = 0
        start_x = 0
        start_y = 0
        end_x = 0
        end_y = 0
        # valid column
        if col < 0 or col >= self.__size:
            return False
        # valid row
        if row < 0 or row >= self.__size:
            return False
        
        # full row
        if self.__grid[row][col] != LinesOfActionState.EMPTY_CELL and self.__grid[row][col] == self.__acting_player:
            print("Essa posição já está ocupada pela sua peça!")
            return False
        
        # Verificar se a peça pertence ao jogador que está a jogar
        if self.__grid[old_row][old_col] != self.__acting_player:
            print("Apenas pode mover as suas peças!")
            return False


        # Verificar se o movimento foi realizado em linha reta
        diff_x = abs(col - old_col)
        diff_y = abs(row - old_row)
    
        # Verificar se há peças a bloquear o caminho do movimento   
        if diff_x == 0:  # movimento na vertical
            start = min(old_row, row)
            end = max(old_row, row)
            for r in range(start+1, end):
                if self.__grid[r][col] != LinesOfActionState.EMPTY_CELL and self.__grid[r][col] != self.__acting_player:
                    print("Não pode passar por cima das peças do seu oponente!")
                    return False
        elif diff_y == 0:  # movimento na horizontal
            start = min(old_col, col)
            end = max(old_col, col)
            for c in range(start+1, end):
                if  self.__grid[row][c] != LinesOfActionState.EMPTY_CELL and self.__grid[row][c] != self.__acting_player:
                    print("Não pode passar por cima das peças do seu oponente!")
                    return False
        else:  # movimento na diagonal
            start_x = min(old_col, col)
            start_y = min(old_row, row)
            end_x = max(old_col, col)
            end_y = max(old_row, row)
        for i in range(1, end_x - start_x):
            r = start_y + i
            c = start_x + i
            if  self.__grid[r][c] != LinesOfActionState.EMPTY_CELL and self.__grid[r][c] != self.__acting_player:
                print("Não pode passar por cima das peças do seu oponente!")
            return False

                              


        """ for old_col in range(self.__grid[row][old_col]):
            if self.__grid[row][old_col] != LinesOfActionState.EMPTY_CELL:
                count_v +=1
        for old_row in range(self.__grid[old_row])[col]:
            if self.__grid[old_row][col] != LinesOfActionState.EMPTY_CELL:
                count_h +=1 """
        return True
    

    def update(self, action: LinesOfActionAction):
        col = action.get_col()
        row = action.get_row()
        old_col = action.get_old_col()
        old_row = action.get_old_row()
    
        # remove the checker from the old position
        self.__grid[old_row][old_col] = -1
    
        # drop the checker
        self.__grid[row][col] = self.__acting_player
        # determine if there is a winner
        self.__has_winner = self.check_winner(self.__acting_player)

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1
        
        

    def __display_cell(self, row, col):
        mapping = {
            0: 'X',
            1: 'O',
            LinesOfActionState.EMPTY_CELL: ' '
        }
        key = self.__grid[row][col]
        print(mapping.get(key, key), end="")

    def __display_numbers(self):
        for col in range(0, self.__size):
                if col < 10:
                    print(' ', end="")
                print(col, end="")

        print("")

    def __display_separator(self):
        for col in range(0, self.__size):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__size):
            print('|', end="")
            for col in range(0, self.__size):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("")

    """ def __is_full(self):
        return self.__turns_count > (self.__size * self.__size)
 """
    def is_finished(self) -> bool:
        return self.__has_winner

    def get_acting_player(self) -> int:
        return self.__acting_player

    def clone(self):
        cloned_state = LinesOfActionState(self.__size)
        cloned_state.__turns_count = self.__turns_count
        cloned_state.__acting_player = self.__acting_player
        cloned_state.__has_winner = self.__has_winner
        for row in range(0, self.__size):
            for col in range(0, self.__size):
                cloned_state.__grid[row][col] = self.__grid[row][col]
        return cloned_state

    def get_result(self, pos) -> Optional[LinesOfActionResult]:
        if self.__has_winner:
            return LinesOfActionResult.LOOSE if pos == self.__acting_player else LinesOfActionResult.WIN
        elif self.__turns_count == 60:
            return LinesOfActionResult.DRAW
        return None

    
    def get_num_rows(self):
        return self.__size

    def get_num_cols(self):
        return self.__size

    def before_results(self):
        pass


    def get_piece(self, row, col):
        if self.__grid[row][col] == self.__acting_player:
            return True
        return False
    
    def get_piece_p1(self,row,col):
        if self.__grid[row][col] == 0:
            return True
        return False
    
