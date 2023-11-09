import argparse
import sys
import random


def guess_number(name='Player1'):
    game_count = 0
    player_wins = 0
    win_percent = 0

    def play_guess_number():
        nonlocal name
        nonlocal player_wins
        nonlocal win_percent
        nonlocal game_count
        playerchoice = input(
            f"{name}, guess which number I'm thinking of... 1, 2, or 3.")
        if playerchoice not in ["1", "2", "3"]:
            print(f"{name}, please enter 1,2,3.")
            return play_guess_number()
        player = int(playerchoice)
        botchoice = random.choice("123")
        bot = int(botchoice)

        print(f"\n{name}, you choose {player}.")
        print(f"I was thinking about the number {bot}.")

        def decide_winner(player, bot):
            nonlocal name
            nonlocal player_wins
            if (player == bot):
                player_wins += 1
                return (f"\n🎉🎉{name} ,You win")
            else:
                return (f"\n😭{name} ,Sorry you lose")

        game_result = decide_winner(player, bot)
        print(game_result)

        game_count += 1
        win_percent = f"{player_wins/game_count:.2%}"
        print(f"\nGame count: {game_count}")
        print(f"\n{name}'s wins: {player_wins}")
        print(f"\nYour winning percentage: {win_percent}")

        print(f"\nPlay again, {name}?")
        while True:
            playagain = input("\nY for Yes or \nQ to Quit \n\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
        if (playagain.lower() == 'y'):
            return play_guess_number()
        else:
            print("\nEnd game🙋‍♀️🙋‍♀️🙋‍♀️")
            print("Thank you or playing!\n")
            sys.exit(f"Bye {name}!!!!!!")

    return play_guess_number


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Give Name of player"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to play"
    )

    args = parser.parse_args()
    game = guess_number(args.name)
    game()
