from game.LoA.players.LoAHuman import HumanLinesOfActionPlayer
from game.LoA.players.LoAMinimax import MinimaxLinesOfActionPlayer
from game.LoA.players.LoARandom import RandomLinesOfActionPlayer
from game.LoA.players.LoAGreedy import GreedyLinesOfActionPlayer
from game.LoA.LoASimulator import LinesOfActionSimulator
from game.LoA.players.LoAMonteCarlo import MonteCarloLinesOfActionPlayer
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
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Bem-vindo ao Lines of Action!")
        print("\nEscolha uma opção:")
        print("1 - Informações do jogo ")
        print("2 - Human vs Human")
        print("3 - Human vs Random")
        print("4 - Human vs Minimax")
        print("5 - Human vs Greedy")
        print("6 - Human vs Monte Carlo")
        print("7 - Sair")

        choice = input("\nDigite o número da opção escolhida: ")
        if choice == "1":
            os.system('cls' if os.name == 'nt' else 'clear')
            print("Regras do jogo:")
            print("- Em cada volta, o jogador tem que mover uma peça, um certo número de casas em linha reta. O número de casas que pode movimentar é exatamente igual ao número de peças, independentemente da sua cor, que existem na linha de movimento.")
            print("- O jogador pode saltar por cima das próprias peças.")
            print("- O jogador não pode saltar por cima das peças do adversário, mas pode captura-las, se a sua peça parar sobre a peça do adversário.")
            print("- O objetivo do jogo é colocar todas as peças que possui ligadas. As ligações entre peças podem ser verticais, horizontais ou diagonais. O primeiro jogador a consegui-lo é o vencedor. ")
            print("- Se um jogador ficar reduzido, por capturas, a uma peça, esse jogador é o vencedor.")
            print("- Se ao fim de 60 jogadas não existir um vencedor, é declarado um empate.")
            print("")
            input("Pressione Enter para voltar ao menu...")
            continue
        elif choice == "2":
            os.system('cls' if os.name == 'nt' else 'clear')
            sim_name = "LinesOfAction - Humano vs Humano"
            player1 = HumanLinesOfActionPlayer("Player1")
            player2 = HumanLinesOfActionPlayer("Player2")
            break
        elif choice == "3":
            os.system('cls' if os.name == 'nt' else 'clear')
            sim_name = "LinesOfAction - Human vs Random"
            player1 = HumanLinesOfActionPlayer("Player1")
            player2 = RandomLinesOfActionPlayer("Random2")
            break
        elif choice == "4":
            os.system('cls' if os.name == 'nt' else 'clear')
            sim_name = "LinesOfAction - Human vs Minimax"
            player1 = HumanLinesOfActionPlayer("Player1")
            player2 = MinimaxLinesOfActionPlayer("Minimax2")
            break
        elif choice == '5':
            os.system('cls' if os.name == 'nt' else 'clear')
            sim_name = "LinesOfAction - Human vs Greedy"
            player1 = HumanLinesOfActionPlayer("Player1")
            player2 = GreedyLinesOfActionPlayer("Greedy2")
            break
        elif choice == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            sim_name = "LinesOfAction - Human vs Monte Carlo"
            player1 = HumanLinesOfActionPlayer("Player1")
            player2 = MonteCarloLinesOfActionPlayer("MonteCarlo2")
            break
        elif choice == "7":
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
