import random
from collections import Counter
from banker import Banker
import sys


# num_of_dice = 6
# rounds = 0

class Gamelogic:
  
  def __init__(self):
    self.num_of_dice = 6
    self.rounds = 0
    self.saved_dice = ''
    self.dice_list = []
    self.banker = Banker()
    self.roll_results = []
    
  def play_game(self, roller=None): 
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
      print(f'Thanks for playing. You have {self.banker.balance} points')
      sys.exit(0)
      
    else:
      print('seriously, this hurts')
      print(self.dice_list)
      self.dice_list = self.string_to_integer(self.saved_dice)
      print(self.dice_list)
      # Made this to verify the dice choices. Our other version was banking points inside of the for loop.
      if self.verify_dice_choices() == True:
        self.unbanked_points(self.dice_list)
    
    print('(r)oll again, (b)ank your points or (q)uit:')
    answer_after_roll = input('> ')
    if answer_after_roll == 'r':
     self.start_new_round()
    
    elif answer_after_roll == 'b':
      print('Please make it stop')
      self.banker.bank()
      
    else:
      print('Thanks for playing.')

  # Verifies players dice choices and makes sure that they are in the roll results.
  def verify_dice_choices(self):
    verified_dice = False
    for dice in range(1, len(self.roll_results)):
      print(f'dice {dice}')
      print(f'roll results {self.roll_results}')
      if self.roll_results[dice] in self.dice_list:
        verified_dice = True
      else:
        print('Please enter a valid choice of dice')
    return verified_dice
    
  # displays unabnked points to player
  def unbanked_points(self, num):
    self.banker.shelf = self.calculate_score(num)
    unbanked_points = self.banker.shelf
    print(f'You have {unbanked_points} unbanked points')
    
  # Starts a new round by incrementing rounds and rolling new dice
  def start_new_round(self):
    roll_str = ''
    self.rounds += 1
    print(f'Starting round {self.rounds}')
    how_many_dice = self.number_of_rolled_dice()
    self.roll_results = self.roll_dice(how_many_dice)
    for num in self.roll_results:
      roll_str += str(num) + ' '
    print(f'*** {self.roll_results}***')
    return self.roll_results
  
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
  
  # Rolls dice and adds them to dice list
  @staticmethod
  def roll_dice(rolled_dice):
    dice_list = []
    for _ in range(rolled_dice):
      dice_list.append(random.randint(1,6))
    print(f"Rolling {len(dice_list)} dice...")
    return tuple(dice_list)

  # calculates score of players saved dice.
  @staticmethod
  def calculate_score(dice):
    print(Counter(dice))
    sorted_dice = Counter(dice)
    points = 0
    print(len(sorted_dice))
    print(sorted_dice.values()) 
    if len(sorted_dice) == 6:
      points += 1500    
    elif len(sorted_dice) == 3 and set(sorted_dice.values()) == set((2, 2, 2)):
      print('Why have you forsaken us')
      points += 1500  
    else: 
      for key, count in sorted_dice.items():
        if count >= 3:
          if key == 1:
            points += (count - 2) * 1000
          else:
            points += (count - 2) * key * 100
        else:
          if key == 5:
            points += 50 * count
          if key == 1:
            points += 100 * count

    print("return", points)
    return points

if __name__ == '__main__':
  farkle = Gamelogic()
  farkle.play_game()
