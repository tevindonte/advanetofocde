
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy as sp

'''
X=loss=0
Y=draw=3
Z=win=6
Rock=1
Scissors=3
Paper=2
Rock = A
Scissors=C
Paper=B
'''

df = pd.read_csv("input2.txt", sep=" ", names=['Player1', 'Player2'])

Player1=df['Player1'].tolist()
Player2=df['Player2'].tolist()
count=0
points=0
extra=0

def part1():
  for x,y in zip(Player1, Player2):
    if x == 'A' and y == 'Z': #loss #Scissors
      count += 1
      points += 0
      extra += 3
    elif x == 'A' and y == 'X': #draw #Rock
      count += 1
      points += 3
      extra += 1
    if x == 'A' and y == 'Y': #win #Paper
      count += 1
      points += 6
      extra += 2
    elif x == 'B' and y == 'X': #loss #Rock
      count += 1
      points += 0
      extra += 1
    elif x == 'B' and y == 'Y': #draw #Paper
      count += 1
      points += 3
      extra += 2
    elif x == 'B' and y == 'Z': #win #Scissors
      count += 1
      points += 6
      extra += 3
    elif x == 'C' and y == 'X': #win #Rock
      count += 1
      points += 6
      extra += 1
    elif x == 'C' and y == 'Y': #loss #Paper
      count += 1
      points += 0
      extra += 2
    else:
      if x == 'C' and y == 'Z': #draw #Scissors
        count += 1
        points += 3
        extra += 3
  total = points + extra
  print(total)

count1=0
points1=0
extra1=0
def part2():
  for x,y in zip(Player1, Player2):
    if x == 'A' and y == 'Y':
      count1 += 1
      points1 += 1
      extra1 += 3
    elif x == 'A' and y == 'X':
      count1 += 1
      points1 += 1
      extra1 += 2
    elif x == 'A' and y == 'Z': 
      count1 += 1
      points1 += 1
      extra1 += 7
    elif x == 'B' and y == 'Y':
      count1 += 1
      points1 += 1
      extra1 += 4
    elif x == 'B' and y == 'X': 
      count1 += 1
      points1 += 1
      extra1 += 0
    elif x == 'B' and y == 'Z':
      count1 += 1
      points1 += 1
      extra1 += 8
    if x == 'C' and y == 'Y':
      count1 += 1
      points1 += 1
      extra1 += 5
    if x == 'C' and y == 'X':
      count1 += 1
      points1 += 1
      extra1 += 1
    if x == 'C' and y == 'Z': 
      count1 += 1
      points1 += 1
      extra1 += 6
  total1=points1+extra1
  print(total1)
