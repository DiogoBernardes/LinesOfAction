from abc import ABC

from game.LoA.LoAResult import LinesOfActionResult
from game.player import Player


class LinesOfActionPlayer(Player, ABC):

    def __init__(self, name):
        super().__init__(name)

        """
        stats is a dictionary that will store the number of times each result occurred
        """
        self.__stats = {}
        for LoAres in LinesOfActionResult:
            self.__stats[LoAres] = 0

        """
        here we are storing the number of games
        """
        self.__num_games = 0

    def print_stats(self):
        num_wins = self.__stats[LinesOfActionResult.WIN]
        if num_wins >0:
            print(
                f"Player {self.get_name()}: {num_wins}/{self.__num_games} wins ({num_wins * 100.0 / self.__num_games} win "
                f"rate)")
            
        num_draws = self.__stats[LinesOfActionResult.DRAW]
        if num_draws >0:
            print("Its a draw")

    def event_new_game(self):
        self.__num_games += 1

    def event_result(self, pos: int, result: LinesOfActionResult):
        if pos == self.get_current_pos():
            self.__stats[result] += 1
