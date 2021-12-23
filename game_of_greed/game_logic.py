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
    # {1: 1, 5: 1}
    
    
    
    if len(sorted_dice) == 6:
      points += 1500
      
    elif len(sorted_dice) == 3 and sorted_dice.values() == 2:
      points += 1500
    
    else: 
      for key, count in sorted_dice.items():
      
      
      
        if count == 3:
          if key == 1:
            print(points)
            points += 1000
            print("after", points)
            print("i am the ones")
          elif key == 2:
            points += 200
            print("i am the twos")
          elif key == 3:
            points += 300
            print("i am the threes")
          elif key == 4:
            points += 400
            print("i am the fours")
          elif key == 5:
            points += 500
            print("i am the fives")
          elif key == 6:
            points += 600
            print("i am the sixes")
          
        elif count == 4:
          print("I shouldnt be in 4s")
          if key == 1:
            points += 2000 
          elif key == 2:
            points += 400
          elif key == 3:
            points += 600
          elif key == 4:
            points += 800
          elif key == 5:
            points += 1000
          elif key == 6:
            points += 1200
          
        elif count == 5:
          print(" I shouldnt be in 5s")
          if key == 1:
            points += 4000 
          elif key == 2:
            points += 600
          elif key == 3:
            points += 1200
          elif key == 4:
            points += 1600
          elif key == 5:
            points += 2000
          elif key == 6:
            points += 2400
          
        elif count == 6:
          print(" I shouldnt be 6s")
          if key == 1:
            points += 8000 
          elif key == 2:
            points += 800
          elif key == 3:
            points += 2400
          elif key == 4:
            points += 3200
          elif key == 5:
            points += 4000
          elif key == 6:
            points += 4800
          
        elif key == 5 and count <= 2:
          print(" I shouldnt be in small fives")
          if count == 1:
            points += 50
          else:
            points += 100
          
        elif key == 1 and count <= 2:
          print(" I shouldnt be small 1s")
          if count == 1:
            points += 100
          else:
            points += 200
          
    print("return", points)
    return points