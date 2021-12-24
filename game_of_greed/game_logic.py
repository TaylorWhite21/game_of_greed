import random
from collections import Counter

class Gamelogic:
  
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