from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAState import LinesOfActionState
#from game.LoA.LoAAction import Cell

class HumanLinesOfActionPlayer(LinesOfActionPlayer):

    def __init__(self, name):
        super().__init__(name)
        
    def get_action(self, state: LinesOfActionState):
        state.display()
        while True:
            try:
                print("Qual a peça que deseja mover?")
                actual_col = int(input(f"Player {state.get_acting_player()}, choose a column: "))
                actual_row = int(input(f"Player {state.get_acting_player()}, choose a row: "))
                if state.get_piece(actual_row, actual_col):
                    print("Qual a posição para a qual deseja mover?")
                    col = int(input(f"Player {state.get_acting_player()}, choose a column: "))
                    row = int(input(f"Player {state.get_acting_player()}, choose a row: "))
                    if (actual_row, actual_col) != (row, col):
                        state.remove_piece(actual_row, actual_col)
                    return LinesOfActionAction(col, row) #Cell(actual_col, actual_row))
                else:
                    print("There is no piece of yours in that position. Please choose a valid move.")
            except Exception:
                continue

    def event_action(self, pos: int, action, new_state: LinesOfActionState):
        # ignore
        pass

    def event_end_game(self, final_state: LinesOfActionState):
        # ignore
        pass
