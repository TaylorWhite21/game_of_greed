import sys

from game_of_greed.game_logic import Gamelogic
from game_of_greed.banker import Banker


class Game:
    """Class for Game of Greed application
    """

    def __init__(self, num_rounds=20):

        self.banker = Banker()
        self.num_rounds = num_rounds
        self.rounds = 0

    def play(self, roller=None):

        self.roll_results = roller or Gamelogic.roll_dice

        print("Welcome to Game of Greed")

        print("(y)es to play or (n)o to decline")
        response_at_game_start = input("> ")

        if response_at_game_start == "n":
            print("OK. Maybe another time")
        else:
            for round_num in range(1, self.num_rounds + 1):
                self.start_new_round(round_num)

            self.quit()

    def quit(self):
        print(f"Thanks for playing. You earned {self.banker.balance} points")
        sys.exit()

    def start_new_round(self, round_num):
        num_of_dice = 6
        print(f"Starting round {round_num}")
        round_score = 0

        while True:
            print(f"Rolling {num_of_dice} dice...")

            roll = self.roll_results(num_of_dice)
            roll_string = " ".join([str(value) for value in roll])
            print(f"*** {roll_string} ***")

            preliminary_score = Gamelogic.calculate_score(roll)

            if preliminary_score == 0:
                self.zilch(round_num)
                return

            saved_dice = self.verify_dice_choices(roll, roll_string)

            saved_dice_score = Gamelogic.calculate_score(saved_dice)

            round_score += saved_dice_score

            num_of_dice -= len(saved_dice)

            print(
                f"You have {round_score} unbanked points and {num_of_dice} dice remaining"
            )
            print("(r)oll again, (b)ank your points or (q)uit:")
            roll = input("> ")

            if response == "b":
                self.banker.shelf(round_score)
                banked_points = self.banker.bank()
                self.end_round(round_num, banked_points)
                break
            elif response == "r":
                if num_of_dice == 0:
                    num_of_dice = 6
            elif response == "q":
                self.quit()

    def zilch(self, round_num):
        """Zero scoring dice were rolled so end round with 0 points"""
        print("****************************************")
        print("**        Zilch!!! Round over         **")
        print("****************************************")

        self.end_round(round_num, 0)

    def end_round(self, round_num, banked_points):
        """bank points and finish round"""
        print(f"You banked {banked_points} points in round {round_num}")
        print(f"Total score is {self.banker.balance} points")

    def verify_dice_choices(self, roll, roll_string):

        while True:
            print("Enter dice to keep, or (q)uit:")
            response = input("> ")
            if response == "q":
                self.quit()
                break

            saved_dice = []
            for char in response:
                if char.isnumeric():
                    saved_dice.append(int(char))

            if Gamelogic.verify_dice_choices(roll, saved_dice):
                return saved_dice
            else:
                print("Cheater!!! Or possibly made a typo...")
                print(f"*** {roll_string} ***")


if __name__ == "__main__":
    game = Game()
    game.play()
