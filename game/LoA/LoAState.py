from typing import Optional
import copy 
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

        self.__turns_count = 1

        self.__acting_player = 0
        
        self.__has_winner = False
    
    def check_winner(self) -> bool:
        player_positions = []
        for row in range(self.__size):
            for col in range(self.__size):
                if self.__grid[row][col] == self.__acting_player:
                    player_positions.append((row, col))
         # se o jogador tiver apenas uma peça, ele vence o jogo
        if len(player_positions) == 1:
            return True

        return max(len(self.checkConnected_Horizontal_LR(self.__acting_player)),
                   len(self.checkConnected_Vertical_LR(self.__acting_player)),
                   len(self.checkConnected_Horizontal_RL(self.__acting_player)), 
                   len(self.checkConnected_Vertical_RL(self.__acting_player))) == len(player_positions)

    def checkConnected_Horizontal_LR(self, player):
        count = 0 
        visited = set()
        
        for i in range(self.__size):
            for j in range(self.__size):
                has_adjacent =  False   
                if self.__grid[i][j] == player and (i,j) not in visited:
                    count += 1
                    visited.add((i,j))
                    
                    if i-1 > -1 and self.__grid[i-1][j] == player and (i-1,j) not in visited:
                        has_adjacent = True
                    if j-1 > -1 and self.__grid[i][j-1] == player and (i,j-1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and self.__grid[i+1][j] == player and (i+1,j) not in visited:
                        has_adjacent = True
                    if j+1 < self.__size and self.__grid[i][j+1] == player and (i,j+1) not in visited:
                        has_adjacent = True
                    if i-1 > -1 and j-1 > -1 and self.__grid[i-1][j-1] == player and (i-1,j-1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and j+1 < self.__size and self.__grid[i+1][j+1] == player and (i+1,j+1) not in visited:
                        has_adjacent = True
                    if i-1 > -1 and j+1 < self.__size and self.__grid[i-1][j+1] == player and (i-1,j+1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and j-1 > -1 and self.__grid[i+1][j-1] == player and (i+1,j-1) not in visited:
                        has_adjacent = True
                  
                    if has_adjacent == False:
                       return visited
        return visited
    
    def checkConnected_Horizontal_RL(self, player):
        count = 0 
        visited = set()
        for i in range(self.__size-1, -1, -1):
            for j in range(self.__size):
                has_adjacent =  False  
                if self.__grid[i][j] == player and (i,j) not in visited:
                    count += 1
                    visited.add((i,j))

                    if i-1 > -1 and self.__grid[i-1][j] == player and (i-1,j) not in visited:
                        has_adjacent = True
                    if j-1 > -1 and self.__grid[i][j-1] == player and (i,j-1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and self.__grid[i+1][j] == player and (i+1,j) not in visited:
                        has_adjacent = True
                    if j+1 < self.__size and self.__grid[i][j+1] == player and (i,j+1) not in visited:
                        has_adjacent = True
                    if i-1 > -1 and j-1 > -1 and self.__grid[i-1][j-1] == player and (i-1,j-1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and j+1 < self.__size and self.__grid[i+1][j+1] == player and (i+1,j+1) not in visited:
                        has_adjacent = True
                    if i-1 > -1 and j+1 < self.__size and self.__grid[i-1][j+1] == player and (i-1,j+1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and j-1 > -1 and self.__grid[i+1][j-1] == player and (i+1,j-1) not in visited:
                        has_adjacent = True
                    if has_adjacent == False:
                        return visited
        return visited
    
    def checkConnected_Vertical_LR(self, player):
        count = 0 
        visited = set()
        
        for j in range(self.__size):
            for i in range(self.__size):
                has_adjacent =  False   
                if self.__grid[i][j] == player and (i,j) not in visited:
                    count += 1
                    visited.add((i,j))
                    
                    if i-1 > -1 and self.__grid[i-1][j] == player and (i-1,j) not in visited:
                        has_adjacent = True
                    if j-1 > -1 and self.__grid[i][j-1] == player and (i,j-1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and self.__grid[i+1][j] == player and (i+1,j) not in visited:
                        has_adjacent = True
                    if j+1 < self.__size and self.__grid[i][j+1] == player and (i,j+1) not in visited:
                        has_adjacent = True
                    if i-1 > -1 and j-1 > -1 and self.__grid[i-1][j-1] == player and (i-1,j-1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and j+1 < self.__size and self.__grid[i+1][j+1] == player and (i+1,j+1) not in visited:
                        has_adjacent = True
                    if i-1 > -1 and j+1 < self.__size and self.__grid[i-1][j+1] == player and (i-1,j+1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and j-1 > -1 and self.__grid[i+1][j-1] == player and (i+1,j-1) not in visited:
                        has_adjacent = True
                    if has_adjacent == False:
                        return visited
        return visited
                        
    def checkConnected_Vertical_RL(self,player):
        count = 0 
        visited = set()
        for j in range(self.__size-1, -1, -1):
            for i in range(self.__size):
                has_adjacent =  False  
                if self.__grid[i][j] == player and (i,j) not in visited:
                    count += 1
                    visited.add((i,j))
                    
                    if i-1 > -1 and self.__grid[i-1][j] == player and (i-1,j) not in visited:
                        has_adjacent = True
                    if j-1 > -1 and self.__grid[i][j-1] == player and (i,j-1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and self.__grid[i+1][j] == player and (i+1,j) not in visited:
                        has_adjacent = True
                    if j+1 < self.__size and self.__grid[i][j+1] == player and (i,j+1) not in visited:
                        has_adjacent = True
                    if i-1 > -1 and j-1 > -1 and self.__grid[i-1][j-1] == player and (i-1,j-1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and j+1 < self.__size and self.__grid[i+1][j+1] == player and (i+1,j+1) not in visited:
                        has_adjacent = True
                    if i-1 > -1 and j+1 < self.__size and self.__grid[i-1][j+1] == player and (i-1,j+1) not in visited:
                        has_adjacent = True
                    if i+1 < self.__size and j-1 > -1 and self.__grid[i+1][j-1] == player and (i+1,j-1) not in visited:
                        has_adjacent = True
                    if has_adjacent == False:
                        return visited                
        return visited


    def get_grid(self):
        return self.__grid

    def get_num_players(self):
        return 2

    def validate_action(self, action: LinesOfActionAction) -> bool:
        col = action.get_col()
        row = action.get_row()
        old_col = action.get_old_col()
        old_row = action.get_old_row()
        count_v = 1
        count_h = 1
        count_diag = 1
        start_x = min(old_col, col)
        start_y = min(old_row, row)
        end_x = max(old_col, col)
        end_y = max(old_row, row)

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
            for r in range(start+1, end): #Verificar se há peças a bloquear o caminho na vertical
                if self.__grid[r][col] != LinesOfActionState.EMPTY_CELL and self.__grid[r][col] != self.__acting_player:
                    print("Não pode passar por cima das peças do seu oponente!")
                    return False
            for v in range(0,7): #Verifica o numero de peças existentes na vertical
                if self.__grid[v][col] != LinesOfActionState.EMPTY_CELL:
                    count_v += 1
            print(count_v)
            if diff_y > count_v: #Verifica o numero de posições que a peça pode ser movida na linha vertical
                print(f"\nA peça {old_col,old_row} apenas pode ser movimentada {count_v} posições na linha vertical\n")
                return False
            
        elif diff_y == 0:  # movimento na horizontal
            start = min(old_col, col)
            end = max(old_col, col)
            for c in range(start+1, end): #Verificar se há peças a bloquear o caminho na horizontal
                if  self.__grid[row][c] != LinesOfActionState.EMPTY_CELL and self.__grid[row][c] != self.__acting_player:
                    print("Não pode passar por cima das peças do seu oponente!")
                    return False
            for h in range(0,7): #Verifica o numero de peças existentes na horizontal
                if self.__grid[row][h] != LinesOfActionState.EMPTY_CELL:
                    count_h += 1  
            if diff_x > count_h: #Verifica o numero de posições que a peça pode ser movida na linha horizontal
                print(f"\nA peça {old_col,old_row} apenas pode ser movimentada {count_h} posições na linha horizontal\n")
                return False
            
        elif end_x - start_x == end_y - start_y:  # movimento na diagonal
            for i in range(1, end_x - start_x): #Verificar se há peças a bloquear o caminho na diagonal
                r = start_y + i
                c = start_x + i
                if r < 0 or r >= self.__size and c < 0 or c >= self.__size:
                    if  self.__grid[r][c] != LinesOfActionState.EMPTY_CELL and self.__grid[r][c] != self.__acting_player:
                        print("Não pode passar por cima das peças do seu oponente!")
                        return False
            for d in range(abs(end_x - start_x)): #Verifica o numero de peças existentes na diagonal 
                r = start_y + d
                c = start_x + d
                # valid row
                if r >= self.__size:
                    return False
                if c >= self.__size:
                    return False
                if self.__grid[r][c] != LinesOfActionState.EMPTY_CELL:
                    count_diag += 1
            if end_x - start_x != count_diag:
                print(f"A peça apenas pode ser movimentada {count_diag} posições na linha diagonal")
                return False 
            
        if diff_x != 0 and diff_y != 0 and end_x - start_x != end_y - start_y:
            #print("Os movimentos apenas podem ser realizados na linha horizontal, vertical ou diagonal")
            return False
        
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
        self.__has_winner = self.check_winner()

        # switch to next player
        self.__acting_player = 1 if self.__acting_player == 0 else 0

        self.__turns_count += 1
        

    def __display_cell(self, row, col):
        print ({
            0: 'X',
            1: 'O',
            LinesOfActionState.EMPTY_CELL: ' '
        }[self.__grid[row][col]], end="")

    def __display_numbers(self):
        print("  ", end="")
        for col in range(0, self.__size):
            if col < 10:
                print(' ', end="")
            print(col, end="")
        print("")

    def __display_separator(self):
        print("  ", end="")
        for col in range(0, self.__size):
            print("--", end="")
        print("-")

    def display(self):
        self.__display_numbers()
        self.__display_separator()

        for row in range(0, self.__size):
            print(f'{row} |', end="")
            for col in range(0, self.__size):
                self.__display_cell(row, col)
                print('|', end="")
            print("")
            self.__display_separator()

        self.__display_numbers()
        print("\n")
     
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
        cloned_state.__grid = copy.deepcopy(self.__grid)
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
    
    def get_piece_p2(self,row,col):
        if self.__grid[row][col] == 1:
            return True
        return False
    
    def sim_play(self,action):
        new_state = self.clone()
        new_state.play(action)
        return new_state
    
    def get_possible_moves(self, player):
    # Retorna uma lista de todas as jogadas possíveis para o jogador atual
        moves = []
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__grid[i][j] == player:
                    for x in range(self.__size):
                        for y in range(self.__size):
                            if self.__grid[x][y] != player:
                                moves.append(LinesOfActionAction(y,x,j,i))
        return list(filter(
            lambda action: self.validate_action(action),
            moves
        ))

    
    def connected_components(self, player):
      return max(self.checkConnected_Horizontal_LR(player),
                self.checkConnected_Vertical_LR(player),
                self.checkConnected_Horizontal_RL(player), 
                self.checkConnected_Vertical_RL(player))
    
 