import math
from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAResult import LinesOfActionResult
from game.LoA.LoAState import LinesOfActionState
from game.state import State


class MinimaxLinesOfActionPlayer(LinesOfActionPlayer):

    def __init__(self, name):
        super().__init__(name)

    '''
    This heuristic will simply count the maximum number of consecutive pieces that the player has
    It's not a great heuristic as it doesn't take into consideration a defensive approach
    '''
    #Verifica o quão perto o jogador atual está de vencer o jogo 
    def __heuristic(self, state: LinesOfActionState):
        #Obtém o estado atual do tabuleiro
        grid = state.get_grid()
        #Obtem a sequencia mais longa encontrada
        longest = 0

        # check each line of grid
        for row in range(0, state.get_num_rows()):
            #inicializa a contagem da sequência
            seq = 0
            #percorre cada coluna da linha atual
            for col in range(0, state.get_num_cols()):
                # Se a posição atual estiver ocupada pelo jogador atual, incrementa a contagem da sequência atual
                if grid[row][col] == self.get_current_pos():
                    seq += 1
                # Se a posição atual não estiver ocupada pelo jogador atual, verifica se a sequência atual é maior do que a sequência mais longa 
                # encontrada até agora e redefine a contagem da sequência atual como 0
                else:
                    if seq > longest:
                        longest = seq
                    seq = 0
            # Verifica se a sequência atual é maior do que a sequência mais longa encontrada até agora
            if seq > longest:
                longest = seq

        # check each column of grid
        for col in range(0, state.get_num_cols()):
            seq = 0
            #Percorre cada linha da coluna atual
            for row in range(0, state.get_num_rows()):
                #se estiver ocupada pelo jogador atual incrementa a contagem da sequencia
                if grid[row][col] == self.get_current_pos():
                    seq += 1
                else:
                    if seq > longest:
                        longest = seq
                    seq = 0

            if seq > longest:
                longest = seq

        # check each upward diagonal
        for row in range(2, state.get_num_rows()):
            for col in range(0, state.get_num_cols() - 3):
                seq1 = (1 if grid[row][col] == self.get_current_pos() else 0) + \
                       (1 if grid[row - 1][col + 1] == self.get_current_pos() else 0)

                seq2 = (1 if grid[row - 1][col + 1] == self.get_current_pos() else 0) + \
                       (1 if grid[row - 2][col + 2] == self.get_current_pos() else 0)

                if seq1 > longest:
                    longest = seq1

                if seq2 > longest:
                    longest = seq2

        # check each downward diagonal
        for row in range(0, state.get_num_rows() - 2):
            for col in range(0, state.get_num_cols() - 2):
                seq1 = (1 if grid[row][col] == self.get_current_pos() else 0) + \
                       (1 if grid[row + 1][col + 1] == self.get_current_pos() else 0) 
                       
                seq2 = (1 if grid[row + 1][col + 1] == self.get_current_pos() else 0) + \
                       (1 if grid[row + 2][col + 2] == self.get_current_pos() else 0) 

                if seq1 > longest:
                    longest = seq1

                if seq2 > longest:
                    longest = seq2

        return longest

    """Implementation of minimax search (recursive, with alpha/beta pruning) :param state: the state for which the 
    search should be made :param depth: maximum depth of the search :param alpha: to optimize the search :param beta: 
    to optimize the search :param is_initial_node: if true, the function will return the action with max ev, 
    otherwise it return the max ev (ev = expected value) """

    def minimax(self, state: LinesOfActionState, depth: int, alpha: int = -math.inf, beta: int = math.inf,
                is_initial_node: bool = True):
        # first we check if we are in a terminal node (victory, draw or loose)
        if state.is_finished():
            return {
                LinesOfActionResult.WIN: 4,
                LinesOfActionResult.LOOSE: -4,
                LinesOfActionResult.DRAW: 0
            }[state.get_result(self.get_current_pos())]

        # if we reached the maximum depth, we will return the value of the heuristic
        if depth == 0:
            return self.__heuristic(state)

        # if we are the acting player
        if self.get_current_pos() == state.get_acting_player():
            # very small integer
            value = -math.inf
            selected_pos = -1

            for pos in range(0, state.get_num_cols()):
                for posJ in range(0, state.get_num_rows()):
                    action = LinesOfActionAction(pos,posJ)
                    if state.validate_action(action):
                        previous_a = value
                        next_state = state.clone()
                        next_state.play(action)
                        value = max(value, self.minimax(next_state, depth - 1, alpha, beta, False))
                        alpha = max(alpha, value)

                        if value >= previous_a:
                            selected_pos = pos
                        if alpha >= beta:
                            break

            if is_initial_node:
                return selected_pos
            return value
        # if it is the opponent's turn
        else:
            # very big integer
            value = math.inf
            for pos in range(0, state.get_num_cols()):
                for posJ in range(0, state.get_num_rows()):
                    action = LinesOfActionAction(pos,posJ)
                    if state.validate_action(action):
                        next_state = state.clone()
                        next_state.play(action)
                        value = min(value, self.minimax(next_state, depth - 1, alpha, beta, False))
                        beta = min(beta, value)
                        if beta <= alpha:
                            break
            return value


    def get_action(self, state: LinesOfActionState):
        return LinesOfActionAction(self.minimax(state, 5), self.minimax(state, 5))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
