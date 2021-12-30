import random
from collections import Counter
from banker import Banker

# num_of_dice = 6
# rounds = 0

class Gamelogic:
  
  def __init__(self):
    self.num_of_dice = 6
    self.rounds = 0
    self.saved_dice = ''
    self.dice_list = []
    self.banker = Banker()
    
  def play_game(self): 
    print('Welcome to Game of Greed')
    print('(y)es to play or (n)o to decline')
    answer = input('> ')
    if answer == 'y':
      self.start_new_round()
    
    print('Enter dice to keep, or (q)uit:')
    self.saved_dice = input('> ')
    if self.saved_dice == 'q':
     print('Thanks for playing.')
    else:
      print('seriously, this hurts')
      print(self.dice_list)
      self.dice_list = self.string_to_integer(self.saved_dice)
      print(self.dice_list)
      for dice in self.dice_list:
        print('this is hell')
        if self.saved_dice == self.dice_list[dice]:
          self.banker.shelf = self.calculate_score(self.saved_dice)
          unbanked_points = self.banker.shelf
          print(f'You have {unbanked_points} unbanked points')
    
    print('(r)oll again, (b)ank your points or (q)uit:')
    answer_after_roll = input('> ')
    if answer_after_roll == 'r':
     self.start_new_round()
    
    elif answer_after_roll == 'b':
      print('Please make it stop')
      self.banker.bank()
      
    else:
      print('Thanks for playing.')
    
  def start_new_round(self):
    roll_str = ''
    self.rounds += 1
    print(f'Starting round {self.rounds}')
    how_many_dice = self.number_of_rolled_dice()
    roll_results = self.roll_dice(how_many_dice)
    for num in roll_results:
      roll_str += str(num) + ' '
    print(f'*** {roll_results}***')
  
  def number_of_rolled_dice(self):
    
    rolled_dice = self.num_of_dice - len(self.string_to_integer(self.saved_dice))
    return rolled_dice
    
  def string_to_integer(self, str):
    saved_dice_list = []
    for char in str:
      try:
        integer = int(char)
        saved_dice_list.append(integer)
      except:
        continue
    return saved_dice_list
  
  @staticmethod
  def roll_dice(rolled_dice):
    dice_list = []
    for _ in range(rolled_dice):
      dice_list.append(random.randint(1,6))
    return tuple(dice_list)

  @staticmethod
  def calculate_score(dice):
    print(Counter(dice))
    sorted_dice = Counter(dice)
    points = 0
    print(len(sorted_dice))
    print(sorted_dice.values())
    # {1: 1, 5: 1}  
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
  play_game = Gamelogic()
  play_game.play_game()
