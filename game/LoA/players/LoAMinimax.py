import math
from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAResult import LinesOfActionResult
from game.LoA.LoAState import LinesOfActionState
from game.state import State


def is_in_danger(state, piece):
    """Returns True if the given piece is in danger of being captured on the next turn."""
    # Check if the piece is on the edge of the board
    if state.is_edge(piece):
        return False

    # Check if any of the adjacent squares are empty
    for neighbor in state.get_neighbors(piece):
        if state.is_empty(neighbor):
            return False

    # Check if any of the adjacent squares contain an opponent's piece
    for neighbor in state.get_neighbors(piece):
        if state.is_opponent(neighbor, state.get_player(piece)):
            return True

    return False

class MinimaxLinesOfActionPlayer(LinesOfActionPlayer):

    def __init__(self, name):
        super().__init__(name)


  
    def __heuristic(self, state: LinesOfActionState, piece_do_jogador: int):
            connected_pieces = 0
            connected_pieces= state.connected_components(state.get_acting_player())

            if(state.get_acting_player()):
                opponent=0
            else:
                opponent=1
            opponent_danger = 0
            opponent = is_in_danger(state,piece_do_jogador)

            heuristic_value = 0.6 * connected_pieces - 0.4 * opponent_danger

            return heuristic_value

   
    def minimax(self, state: LinesOfActionState, depth: int, alpha: int = -math.inf, beta: int = math.inf,
                is_initial_node: bool = True):
        if state.is_finished():
            return {
                LinesOfActionResult.WIN: 4,
                LinesOfActionResult.LOOSE: -4,
                LinesOfActionResult.DRAW: 0
            }[state.get_result(self.get_current_pos())]

        if depth == 0:
            return self.__heuristic(state)

        if self.get_current_pos() == state.get_acting_player():
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
        else:
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