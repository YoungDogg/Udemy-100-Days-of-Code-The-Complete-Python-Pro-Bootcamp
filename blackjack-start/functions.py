import random
from art import logo
import os

# to do
# check flow
# after second game, it's drawing two cards to player 

def clear():
  os.system('cls')

def game_init():  
  print(logo)

  hands = {"computer": [], "player": []}
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  # ==========question======================================================================
  # in dictionary, functions used w/o parameters. When are also no-parameter-functions used?
  # ========================================================================================

  return {"hands": hands, "cards": cards}

def game_start(init_dic=game_init()):

  while True:
    hands = init_dic["hands"]
    cards = init_dic["cards"]

    hands["computer"].append(draw_card(cards))
    hands["player"].append(draw_card(cards))
    hands["computer"].append(draw_card(cards))
    hands["player"].append(draw_card(cards))

    computer_sum = card_sum(hands["computer"])
    player_sum = card_sum(hands["player"])

    display_hand_and_sum(hands)

    # computer soft 17    
    hands = soft_17(hands, cards, computer_sum)
    
    computer_sum = card_sum(hands["computer"])
    player_sum = card_sum(hands["player"])
    
    
    if not ask_hit_more_card(cards = cards , hands = hands, computer_sum = computer_sum, player_sum = player_sum):
      exit()
      
  

def draw_card(cards):
  randIndex = random.randint(0, len(cards) - 1)
  return cards[randIndex]

def card_sum(hands):
  sum = 0
  for each_card in hands:
    sum += each_card
  for card in hands:
    if card == 11 and sum > 21:
      sum -= 10  # consider 11 as 1
      break
  return sum

def display_hand_and_sum(hands):  
  print(f'your card {hands["player"]} ---- sum: {card_sum(hands["player"])}')  
  print(f'computer card [{hands["computer"][0]}]')
  print("====================================================================")


def game_again(): # ============= FIX LATER ================
  y_or_n = input("play again? Yes, type y. No, type n: ")
  if y_or_n == 'y':
    clear()    
    return True
    game_start(game_init())  # recursion. error could be occured. Change to a flag
    # Q: why logo not displayed?
    # A: if not calling game_init() as an argument, the "old" game_init() will still be the argument, not the new one.
    
  else:
    exit()

def ask_hit_more_card(computer_sum, player_sum, cards, hands):        
  while True:    
    is_player_hit_card = input("hit one more card? Yes, type y. No, Type n: ")
    if is_player_hit_card =='y':
      hands["player"].append(draw_card(cards))
      display_hand_and_sum(hands)
      player_sum = card_sum(hands["player"])
      # ======================
      #  insert soft rule 17
      # ======================
      is_over_21 = decide_soft_17(computer_sum, player_sum)
      if is_over_21:
        return True
      if player_sum > 21:
        which_one_win(computer_sum, player_sum)
      continue
    if is_player_hit_card == 'n':
      return True
    else:      
      print("type y or n")
    

def which_one_win(computer_sum, player_sum):  
    if computer_sum > 21:
      print("#############player win!!#############")
    elif player_sum > 21:
      print("#############player win!!#############")
    else:
      if computer_sum > player_sum:
        print("#############computer win!!#############")
      elif computer_sum < player_sum:
        print("#############player win!!#############")
      else:
        print("#############draw!!#############")
    

def soft_17(hands, cards, computer_sum):
  # draw more card if computer sum < 17
  while computer_sum < 17:
      hands["computer"].append(draw_card(cards))
      computer_sum = card_sum(hands["computer"])
  
  # if computer sum > 21, game over
  if computer_sum > 21:
    game_over(winner="player", hands=hands) 
  
  return hands


def decide_soft_17(computer_sum, player_sum):
  if computer_sum > 21:

    print('you win')
    return True
  else:
    return False  


def computer_safe_17_rule(computer_sum, player_sum, hands, cards):
  if computer_sum <= 17:
    while computer_sum <= 17:
      hands["computer"].append(draw_card(cards))
      computer_sum = card_sum(hands["computer"])
  
  return {
      "computer_sum": computer_sum,
      "player_sum": player_sum,
      "hands": hands,
      "cards": cards
  }


def game_over(winner, hands):
  display_hand_and_sum(hands)
  print(f'winner: {winner}')
