from random import choice
from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAResult import LinesOfActionResult
from game.LoA.LoAState import LinesOfActionState


class MonteCarloLinesOfActionPlayer(LinesOfActionPlayer):
    def __init__(self, name):
        super().__init__(name)

    def get_action(self, state: LinesOfActionState):
        selected_action = None
        max_score = -1
        count = 1
        
        actions = state.get_possible_moves(state.get_acting_player())
        loop = len(actions) 
        for check_action in actions:
            new_state = state.sim_play(check_action)
            score = self.monte_carlo(new_state)
            if score > max_score:
                max_score = score
                selected_action = check_action
            print(f"CALCULAR JOGADA: {count}/{loop} | SCORE: {score}/{max_score}")
            count +=1
        return selected_action

    def monte_carlo(self, state: LinesOfActionState):
        wins = 0
        losses = 0
        draws = 0

        for i in range(100):
            cloned_state = state.clone()
            while not cloned_state.is_finished():
                possible_moves = cloned_state.get_possible_moves(cloned_state.get_acting_player)
                if len(possible_moves) == 0:
                    draws += 1
                    break
                action = choice(possible_moves)
                cloned_state.play(action)

            result = cloned_state.get_result(self.get_current_pos())
            if result == LinesOfActionResult.WIN:
                wins += 1
            elif result == LinesOfActionResult.LOOSE:
                losses += 1
            elif result == LinesOfActionResult.DRAW:
                draws += 1

        return (wins + draws * 0.25) / (wins + losses + draws)

    def event_action(self, pos: int, action: LinesOfActionAction, new_state: LinesOfActionState):
        # ignore
        pass

    def event_end_game(self, final_state: LinesOfActionState):
        # ignore
        pass