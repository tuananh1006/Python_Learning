import random
import sys
from enum import Enum


def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0

    def play_rps():
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
            "\nEnter...\n1 for Rock,\n2 for  Paper, or \n3 for Srcrissors:\n\n")
        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1,2,3.")
            return play_rps()
        player = int(playerchoice)

        computerchoice = random.choice("123")
        computer = int(computerchoice)

        print("\nYou choose " + str(RPS(player)).replace('RPS.', ''))
        print("Python choose " + str(RPS(computer)).replace('RPS.', ''))

        def decide_winner(player, coumpter):
            nonlocal player_wins
            nonlocal python_wins
            if player == 1 and computer == 3:
                player_wins += 1
                return "You win🎈"
            elif player == 2 and computer == 1:
                player_wins += 1
                return "You win🎈"
            elif player == 3 and computer == 2:
                player_wins += 1
                return "You win🎈"
            elif player == computer:
                return "Tie game!🤣"
            else:
                python_wins += 1
                return "Python wins!🔪"

        game_result = decide_winner(player, computer)

        print(game_result)

        nonlocal game_count
        game_count += 1

        print("\nGame count: " + str(game_count))
        print("\nPlayer win: " + str(player_wins))
        print("\nPython win: " + str(python_wins))

        print("\nPlay again?")
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
            sys.exit("Bye!!!!!!!!!")

    return play_rps


play = rps()

play()
