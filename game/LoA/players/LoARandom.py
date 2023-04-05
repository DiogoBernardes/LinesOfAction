from random import randint

from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAState import LinesOfActionState
from game.state import State


class RandomLinesOfActionPlayer(LinesOfActionPlayer):

    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: LinesOfActionState):
        return LinesOfActionAction(randint(0, state.get_num_cols()), randint(0, state.get_num_rows()))

    def event_action(self, pos: int, action, new_state: State):
        # ignore
        pass

    def event_end_game(self, final_state: State):
        # ignore
        pass
