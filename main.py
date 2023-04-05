from game.LoA.players.LoAHuman import HumanLinesOfActionPlayer
from game.LoA.players.LoAMinimax import MinimaxLinesOfActionPlayer
from game.LoA.players.LoARandom import RandomLinesOfActionPlayer
from game.LoA.players.LoAGreedy import GreedyLinesOfActionPlayer
from game.LoA.LoASimulator import LinesOfActionSimulator
from game.game_simulator import GameSimulator
import os

def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    num_iterations = 1

    while True:
        print("Bem-vindo ao Lines of Action!")
        print("\nEscolha uma opção:")
        print("1 - Human vs Human")
        print("2 - Human vs Random")
        print("3 - Human vs Minimax")
        print("4 - Sair")

        choice = input("\nDigite o número da opção escolhida: ")
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            sim_name = "LinesOfAction - Human vs Human"
            player1 = HumanLinesOfActionPlayer("Player1")
            player2 = HumanLinesOfActionPlayer("Player2")
            break
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            sim_name = "LinesOfAction - Human vs Random"
            player1 = HumanLinesOfActionPlayer("Player1")
            player2 = RandomLinesOfActionPlayer("Random2")
            break
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            sim_name = "LinesOfAction - Human vs Minimax"
            player1 = HumanLinesOfActionPlayer("Player1")
            player2 = MinimaxLinesOfActionPlayer("Minimax2")
            break
        elif choice == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Até logo!")
            return
        else:
            print("Opção inválida.")

    LoA_simulations = [
        {
            "name": sim_name,
            "player1": player1,
            "player2": player2
        }
    ]

    for sim in LoA_simulations:
        run_simulation(sim["name"], LinesOfActionSimulator(sim["player1"], sim["player2"]), num_iterations)

if __name__ == "__main__":
    main()
