from game.LoA.players.LoAHuman import HumanLinesOfActionPlayer
from game.LoA.players.LoAMinimax import MinimaxLinesOfActionPlayer
from game.LoA.players.LoARandom import RandomLinesOfActionPlayer
from game.LoA.players.LoAGreedy import GreedyLinesOfActionPlayer
from game.LoA.LoASimulator import LinesOfActionSimulator
from game.game_simulator import GameSimulator

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 1

    LoA_simulations = [
        {
            "name": "LinesOfAction - Human vs Human",
            "player1": HumanLinesOfActionPlayer("Player1"),
            "player2": HumanLinesOfActionPlayer("Player2")
        },
        #{   
        #   "name": "LinesOfAction - Human vs Random",
        #    "player1": HumanLinesOfActionPlayer("Player1"),
        #    "player2": RandomLinesOfActionPlayer("Random2")   
        #},
       """  {
            "name": "LinesOfAction - Human vs Minimax",
            "player1": HumanLinesOfActionPlayer("Player1"),
            "player2": MinimaxLinesOfActionPlayer("Minimax2")
            
        } """
    ]


    for sim in LoA_simulations:
        run_simulation(sim["name"], LinesOfActionSimulator(sim["player1"], sim["player2"]), num_iterations)

  


if __name__ == "__main__":
    main()
