from functions import card_sum, game_init, game_over, draw_card, soft_17


hands = {"computer": [7,9], "player": [10,2]}
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
computer_sum = 16

def soft_17(hands, cards, computer_sum):
  # draw more card if computer sum < 17
  while computer_sum < 17:
    #   hands["computer"].append(draw_card(cards))
    print(f'pass bitch')
  
  # if computer sum > 21, game over
  if computer_sum > 21:
    game_over(winner="player", hands=hands)
  
  return hands


soft_17(hands, cards, computer_sum)