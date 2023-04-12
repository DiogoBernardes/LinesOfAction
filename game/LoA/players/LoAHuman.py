from game.LoA.LoAAction import LinesOfActionAction
from game.LoA.LoAPlayer import LinesOfActionPlayer
from game.LoA.LoAState import LinesOfActionState
import os 
#from game.LoA.LoAAction import Cell

class HumanLinesOfActionPlayer(LinesOfActionPlayer):

    def __init__(self, name):
        super().__init__(name)
        
    def get_action(self, state: LinesOfActionState):
        state.display()
        while True:
            try:
                print("Qual a peça que deseja mover?")
                print()
                old_col = int(input(f"Player {state.get_acting_player()}, choose a column: "))
                old_row = int(input(f"Player {state.get_acting_player()}, choose a row: "))
                if state.get_piece(old_row, old_col):
                    os.system('cls' if os.name == 'nt' else 'clear')
                    state.display()
                    print(f"Qual a posição para a qual deseja mover a peça ({old_col}, {old_row})?")
                    col = int(input(f"Player {state.get_acting_player()}, choose a column: "))
                    row = int(input(f"Player {state.get_acting_player()}, choose a row: "))
                    if state.validate_action:
                        return LinesOfActionAction(col, row,old_col, old_row) 
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
