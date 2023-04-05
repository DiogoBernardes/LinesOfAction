from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAState import LinesOfActionState
from game.game_simulator import GameSimulator


class LinesOfActionSimulator(GameSimulator):

    def __init__(self, player1: LinesOfActionPlayer, player2: LinesOfActionPlayer, size: int=8):
        super(LinesOfActionSimulator, self).__init__([player1, player2])
        """
        the number of rows and cols from the connect4 grid
        """
        self.__size = size

    def init_game(self):
        return LinesOfActionState(self.__size)

    def before_end_game(self, state: LinesOfActionState):
        # ignored for this simulator
        pass

    def end_game(self, state: LinesOfActionState):
        # ignored for this simulator
        pass
