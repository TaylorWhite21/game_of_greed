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
  def calculate_score(dice_tuple):

    score = 0
    scoring_dice = []
    counts = Counter(tuple_of_dice)

    if tuple_of_dice and set(tuple_of_dice) == set((1, 2, 3, 4, 5, 6)):
        score += 1500
        scoring_dice.extend([*tuple_of_dice])
    elif len(counts) == 3 and set(counts.values()) == set((2,)):
        score += 1500
        scoring_dice.extend([*tuple_of_dice])
    else:
        # Counter([1, 1, 1, 1, 2]) --> {key: count, key: count} --> counts = {1: 4, 2: 1}
        # {1: 4, 2: 1} --> key = 1, count = 4 --> key = 2, count = 1
        for key, count in counts.items():
            if count >= 3:
                if key == 1:
                    score += (count - 2) * 1000
                    scoring_dice.extend([key for _ in range(count)])
                else:
                    score += (count - 2) * key * 100
                    scoring_dice.extend([key for _ in range(count)])
            else:
                if key == 5:
                    score += 50 * count
                    scoring_dice.extend([key for _ in range(count)])
                if key == 1:
                    score += 100 * count
                    scoring_dice.extend([key for _ in range(count)])

    if type_of_return == 'score':
        return score
    elif type_of_return == 'scoring_dice':
        return tuple(scoring_dice)
    


