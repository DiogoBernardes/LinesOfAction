from random import choice
from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAState import LinesOfActionState
from game.state import State


class GreedyLinesOfActionPlayer(LinesOfActionPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: LinesOfActionState):
        grid = state.get_grid()

        selected_col = None
        max_count = 0

        for col in range(0, state.get_num_cols()):
            if not state.validate_action(LinesOfActionAction(col)):
                continue

            count = 0
            for row in range(0, state.get_num_rows()):
                if grid[row][col] == self.get_current_pos():
                    count += 1

            # it swap the column if we exceed the count. if the count of chips is the same, we swap 50% of the times
            if selected_col is None or count > max_count or (count == max_count and choice([False, True])):
                selected_col = col
                max_count = count

        if selected_col is None:
            raise Exception("There is no valid action")

        return LinesOfActionAction(selected_col)

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
