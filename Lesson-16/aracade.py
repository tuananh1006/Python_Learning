import argparse
import sys
import guess_number
from guess_number import game
from rps8 import rock_paper_scissors


def Arcade(name="Player01"):
    def play_Arcade():
        nonlocal name
        print(f"{name}, welcome to Arcade! 👽")
        print(f"Please choose a game:")
        print(f"1 = Rock Paper Scrissors")
        print(f"2 = Guess my number")
        print(f"\n Or press x to exit the arcade")

        player_decide = input("\n")
        if player_decide.lower() == "x":
            sys.exit("Bye bye!! I will miss you😖")
        elif int(player_decide) not in [1, 2, 3]:
            print(f"\n {name} ,you must press 1,2 or x")
            return play_Arcade()
        else:
            player = int(player_decide)
            if (player == 1):
                rock_paper_scissors()
            elif (player == 2):
                game_guess_number()

        return play_Arcade()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Add name player"
    )
    parser.add_argument(
        "-n", "--n", metavar="name",
        required=True, help="Give a name player"
    )
    parser.parse_args()
