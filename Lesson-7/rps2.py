import random
import sys
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


playagain = True

while playagain:

    # PRINT(RPS(2))
    # PRINT(RPS.ROCK)
    # PRINT(RPS['ROCK'])
    # PRINT(RPS.ROCK.VALUE)
    # sys.exit()

    playerchoice = input(
        "\nEnter...\n1 for Rock,\n2 for  Paper, or \n3 for Srcrissors:\n\n")
    player = int(playerchoice)
    if player < 1 or player > 3:
        sys.exit("You must enter 1,2,3.")

    computerchoice = random.choice("123")
    computer = int(computerchoice)

    print("\nYou choose " + str(RPS(player)).replace('RPS.', ''))
    print("Python choose " + str(RPS(computer)).replace('RPS.', ''))

    if player == 1 and computer == 3:
        print("\nYou win🎈")
    elif player == 2 and computer == 1:
        print("\nYou win🎈")
    elif player == 3 and computer == 2:
        print("\nYou win🎈")
    elif player == computer:
        print("\nTie game!🤣")
    else:
        print("\nPython wins!🔪")

    playagain = input("\nPlay again\nY for Yes or \nQ to Quit \n\n")

    if (playagain.lower() == 'y'):
        continue
    else:
        print("\nEnd game🙋‍♀️🙋‍♀️🙋‍♀️")
        print("Thank you or playing!\n")
        playagain = False

sys.exit("Bye! 👋")
