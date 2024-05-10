import random

from art import logo
from game_data import data

SCORE = 0

def game_start():
  print(logo)

def game_update():
  my_input = ""
  a= ""
  b= ""
  answer = answer_func(a,b)
  
def answer_func(a, b):
  if a > b:    
    return a
  else:
    return b  

def used_data_index_list():
  return True