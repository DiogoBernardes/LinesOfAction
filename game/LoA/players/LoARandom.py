from random import randint

from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAState import LinesOfActionState
from game.state import State


class RandomLinesOfActionPlayer(LinesOfActionPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: LinesOfActionState):
        
        #obter as posições de todas as peças do jogador atual
        player_positions = []
        for row in range(state.get_num_rows()):
            for col in range(state.get_num_cols()):
                if state.get_piece_p1(row,col):
                    player_positions.append((row, col))

        # escolher uma das peças aleatoriamente
        if player_positions:
            random_index = randint(0, len(player_positions) - 1)
            old_row, old_col = player_positions[random_index]
        else:
            old_row, old_col = None, None

        # gerar uma nova posição aleatória
        new_row, new_col = randint(0, state.get_num_rows() - 1), randint(0, state.get_num_cols() - 1)
        print(f"Player {state.get_acting_player()} movimentou a peça {old_col,old_row} para a posição {new_col,new_row}")
        # criar e retornar a ação correspondente
        return LinesOfActionAction(new_col, new_row, old_col, old_row)
        

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
