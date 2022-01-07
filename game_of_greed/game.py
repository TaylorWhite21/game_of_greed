from game_of_greed.game_logic import Gamelogic
try:
    from banker import Banker
except:
    from game_of_greed.banker import Banker
import sys

class Game:
    def __init__(self):
        self.num_of_dice = 6
        self.rounds = 0
        self.banker = Banker()
        self.roll_results = []
        self.saved_dice = ''
        self.dice_list = []

    def play(self, roller = Gamelogic.roll_dice): 
        self.roller = roller
        print('Welcome to Game of Greed')
        print('(y)es to play or (n)o to decline')
        answer = input('> ')
        if answer == 'y':
          self.start_new_round()
        else:
          print('OK. Maybe another time')

        print('Enter dice to keep, or (q)uit:')
        self.saved_dice = input('> ')
        if self.saved_dice == 'q':
          quit(f'Thanks for playing. You have {self.banker.balance} points')

        else:
          self.dice_list = self.string_to_integer(self.saved_dice)
          # Made this to verify the dice choices. Our other version was banking points inside of the for loop.
          if self.verify_dice_choices() == True:
            self.unbanked_points(self.dice_list)

        print('(r)oll again, (b)ank your points or (q)uit:')
        answer_after_roll = input('> ')
        if answer_after_roll == 'r':
         self.start_new_round()

        elif answer_after_roll == 'b':
          self.banker.bank()

        else:
          print('Thanks for playing.')

      # Verifies players dice choices and makes sure that they are in the roll results.
    def verify_dice_choices(self):
        verified_dice = False
        for dice in range(1, len(self.roll_results)):
          if self.roll_results[dice] in self.dice_list:
            verified_dice = True    
        if verified_dice == False:
            print('Cheater!!! Or possibly a typo...')
        return verified_dice

      # displays unabnked points to player
    def unbanked_points(self, num):
      self.banker.shelf = Gamelogic.calculate_score(num)
      unbanked_points = self.banker.shelf
      print(f'You have {unbanked_points} unbanked points')
      
    # Starts a new round by incrementing rounds and rolling new dice
    def start_new_round(self):
      self.rounds += 1
      self.banker.clear_shelf()
      print(f'Starting round {self.rounds}')
      how_many_dice = self.number_of_rolled_dice()
      self.roll_results = Gamelogic.roll_dice(how_many_dice)
      self.roll_results = self.format_tuple(self.roll_results)
      print(f'*** {self.roll_results} ***')
      return self.roll_results

    # Formats tuple into a string to pass test
    def format_tuple(self, rolled_dice):
        formatted_dice = str(rolled_dice).strip("([])").replace(", ", " ")
        return formatted_dice

    # Calculates how many dice to roll
    def number_of_rolled_dice(self):
    
      rolled_dice = self.num_of_dice - len(self.string_to_integer(self.saved_dice))
      return rolled_dice
      
     # Converts player chosen dice from string to integers 
    def string_to_integer(self, str):
      saved_dice_list = []
      for char in str:
        try:
          integer = int(char)
          saved_dice_list.append(integer)
        except:
          continue
      return saved_dice_list

    def quit(message):
        sys.exit(message)


if __name__ == '__main__':
    game = Game()
    game.play()
