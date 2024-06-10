import random

from art import logo, vs
from game_data import data
from clear import clear_screen

SCORE = 0

# def game_start():
#   print(logo)


def game_update():
  is_playable = True  
  is_correct = False

  while is_playable:
    a, b = diff_check_of_b()
    answer = answer_func(a,b)
    print(logo)
    print(f'Compare A: {a["name"]}, {a["description"]}, from {a["country"]}')
    if is_correct:
      print(f"You're right! Current score: {SCORE}")    
    print()
    print()
    print(vs)
    print(f'Against B: {b["name"]}, {b["description"]}, from {b["country"]}')
    my_input = input("Who has more followers? Type 'A' or 'B': ")

    my_input = answer
    if my_input == answer:
      clear_screen()
      is_correct = True
      SCORE += 1

    else:
      is_playable = False
      clear_screen()
      print(logo)
      print(f"Sorry, that's wrong. Final socre: {SCORE}")


def diff_check_of_b():
  a = data[random.randint(0, len(data))]
  b = data[random.randint(0, len(data))]
  while a == b:
    b = data[random.randint(0, len(data))]
  return a, b

def answer_func(a, b):
  if a["follower_count"] > b["follower_count"]:    
    return a
  else:
    return b  

