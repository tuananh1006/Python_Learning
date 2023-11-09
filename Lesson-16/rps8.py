import random
import sys
from enum import Enum
import argparse


def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins

        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3

        # PRINT(RPS(2))
        # PRINT(RPS.ROCK)
        # PRINT(RPS['ROCK'])
        # PRINT(RPS.ROCK.VALUE)
        # sys.exit()

        playerchoice = input(
            f"\n{name}, please enter...\n1 for Rock,\n2 for  Paper, or \n3 for Srcrissors:\n\n")
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1,2,3.")
            return play_rps()
        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print(f"\n{name},you choose {str(RPS(player)).replace('RPS.', '').title}.")
        print(
            f"Python choose  {str(RPS(computer)).replace('RPS.', '').title()}."
        )

        def decide_winner(player, coumpter):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return f"{name},you win🎈"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"{name},You win🎈"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"{name},You win🎈"
            elif player == computer:
                return "Tie game!🤣"
            else:
                python_wins += 1
                return f"Python wins!🔪\nSorry,{name}..😢"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print(f"\nGame count: { game_count} ")
        print(f"\nPlayer win: {player_wins} ")
        print(f"\nPython win: {python_wins} ")

        print(f"\nPlay again, {name}?")
        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if (playagain.lower() == 'y'):
            return play_rps()
        else:
            print("\nEnd game🙋‍♀️🙋‍♀️🙋‍♀️")
            print("Thank you or playing!\n")
            sys.exit(f"Bye {name}!!!!!!")

    return play_rps


if __name__ == "__main__":

    parser = argparse.ArgumentParser(
        description="Provies a personalized game experience"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person playing the game"
    )

    args = parser.parse_args()

    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
