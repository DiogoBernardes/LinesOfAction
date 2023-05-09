from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAState import LinesOfActionState
from game.state import State


class GreedyLinesOfActionPlayer(LinesOfActionPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: LinesOfActionState) -> LinesOfActionAction:
        selected_action = None
        max_score = -float('inf')

        # Obter as jogadas possiveis do jogador atual
        possible_moves = state.get_possible_moves(state.get_acting_player())
        
        for move in possible_moves:
            # Calcular a pontuação para este movimento 
            score = self.calculate_score(state, move) 
            # Caso o movimento tenha uma pontuação maior do que o max_Score, atribui o valor de score ao max_score
            if score > max_score:
                max_score = score
                selected_action = move
        if selected_action is None:
            raise Exception("There is no valid action")
        
        return selected_action



    def calculate_score(self, state: LinesOfActionState, move: LinesOfActionAction):
        #Cria uma cópia do estado atual do jogo e simula uma jogada
        new_state = state.sim_play(move)
        player = new_state.get_acting_player()

        # Se o movimento capturar uma peça do oponente, retorna 3 pontos
        if new_state.get_piece(move.get_row(), move.get_col()) != player:
            return 3

        # Se o movimento se aproximar do centro do tabuleiro, retorna 7pontos
        if move.get_row() == 1 or 2 and 0 <= move.get_col() <= 7:
            return 7
        elif move.get_row() == 3 or 4 and 0 <= move.get_col() <= 7:
            return 7
        elif move.get_row() == 5 or 6 and 0 <= move.get_col() <= 7:
            return 7
        elif move.get_row() == 7 and 0 <= move.get_col() <= 7:
            return 7

        # Se o movimento aproximar a peça de uma outra peça do jogador retorna 10 pontos
        if any(new_state.get_piece(row, col) == player for row in range(8) for col in range(8)):
            return 10
        
        return 1

      

    def event_action(self, pos: int, action: LinesOfActionAction, new_state: LinesOfActionState):
        # ignore
        pass

    def event_end_game(self, final_state: LinesOfActionState):
        # ignore
        pass