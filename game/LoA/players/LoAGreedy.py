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

        # Get the possible moves for the current player
        possible_moves = state.get_possible_moves(state.get_acting_player())
        
        for move in possible_moves:
            # Calculate the score for this move (this logic depends on your game)
            score = self.calculate_score(state, move) #or 0
            # If this move has a higher score than the current max score, select it
            if score > max_score:
                max_score = score
                selected_action = move
        if selected_action is None:
            raise Exception("There is no valid action")

        # Convert the selected move (a tuple) to a LinesOfActionAction and return it
       
        return selected_action



    def calculate_score(self, state: LinesOfActionState, move: LinesOfActionAction):
        # Create a copy of the state and simulate the move
        new_state = state.sim_play(move)

        player = new_state.get_acting_player()

        # If the move captures an opponent piece, give a high score
        if new_state.get_piece(move.get_row(), move.get_col()) != player:
            return 3
        # If the move interconnects the player's pieces, give a high score
        elif new_state.get_piece(move.get_row(), move.get_col()) == player:
            components = new_state.connected_components(player)
            old_component = [c for c in components if (move.get_old_row(), move.get_old_col()) in c]
            new_component = [c for c in components if (move.get_row(), move.get_col()) in c]
            if old_component != new_component:
                if len(old_component) > 0 and len(new_component) > 0:
                    old_component = old_component[0]
                    new_component = new_component[0]
                    # Check if the moved piece connects the first row with the last row
                    if (1 <= move.get_row() <= 2 or 5 <= move.get_row() <= 6) and abs(move.get_row() - 3) < abs(move.get_col() - 3) and any(new_state.get_piece(row, col) == player for row in range(1, 7) for col in range(8)):
                        return 15
                    # Check if the moved piece connects the middle rows
                    elif (move.get_row() == 0 and any(new_state.get_piece(7, col) == player for col in range(8))) or (move.get_row() == 7 and any(new_state.get_piece(0, col) == player for col in range(8))):
                        return 11
                    else:
                        return 10

        # If the move connects the player's piece to an empty cell, give a medium score
        elif new_state.get_piece(move.get_row(), move.get_col()) == -1:
            return 5


    def event_action(self, pos: int, action: LinesOfActionAction, new_state: LinesOfActionState):
        # ignore
        pass

    def event_end_game(self, final_state: LinesOfActionState):
        # ignore
        pass