import random
from collections import Counter
try:
    from banker import Banker
except:
    from game_of_greed.banker import Banker

class Gamelogic:
  
  def __init__(self):
    self.banker = Banker()
  
  # Rolls dice and adds them to dice list
  # @staticmethod
  def roll_dice(rolled_dice):
    dice_list = []
    for _ in range(rolled_dice):
      dice_list.append(random.randint(1,6))
    print(f"Rolling {len(dice_list)} dice...")
    return tuple(dice_list)

  # calculates score of players saved dice.
  # @staticmethod
  def calculate_score(dice):
    sorted_dice = Counter(dice)
    points = 0 
    if len(sorted_dice) == 6:
      points += 1500    
    elif len(sorted_dice) == 3 and set(sorted_dice.values()) == set((2, 2, 2)):
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

  # Borrowed from given code
  @staticmethod
  def verify_dice_choices(roll, keepers):
    keeper_counter = Counter(keepers)
    roll_counter = Counter(roll)
    result = keeper_counter - roll_counter
    return not result

  @staticmethod
  def get_scorers(dice):
      # version_3
      all_dice_score = Gamelogic.calculate_score(dice)
      if all_dice_score == 0:
          return tuple()
      scorers = []
      for i, val in enumerate(dice):
          sub_roll = dice[:i] + dice[i + 1 :]
          sub_score = Gamelogic.calculate_score(sub_roll)
          if sub_score != all_dice_score:
              scorers.append(val)
      return tuple(scorers)
