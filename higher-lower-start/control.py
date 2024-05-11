import random

from art import logo, vs
from game_data import data

SCORE = 0

# def game_start():
#   print(logo)


def game_update():
  is_playable = True
  my_input = input("Who has more followers? Type 'A" or 'B': )  
  a, b = diff_check_of_b()
  answer = answer_func(a,b)

  while is_playable:
    print(logo)
    print(f'Compare A: {a["name"]}, {a["description"]}, from {a["country"]}')
    print()
    print()
    print(vs)
    print(f'Against B: {b["name"]}, {b["description"]}, from {b["country"]}')
    my_input
    if my_input == answer:
      # if it's right      
      return True 

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

def used_data_index_list():
  return True