from random import randint

t = ['Rock', 'Paper', 'Scissors']
computer = t[randint(0,2)]

player = False

while player == False:
  player = input('Rock, Paper,Scissors?')
  if player == computer:
    print('tie') 
  elif player == 'rock':
    if computer == 'paper':
      print('You Lose',computer,'Covers Player')
    else:
      print('You Win',player,'Smashes',computer)
  elif player == 'Paper':
    if computer == 'Scissors':
      print('You Lose',computer,'Cut',player) 
    else:
      print('You Win',player,'Covers',computer)
  elif player == 'Scissors':
    if computer == 'Rock':
      print('You Lose....',computer,'Batters',player)
    else:
      print('You Win!!', player,'Cuts',computer)
else:
  print('Thats not a valid play, try again!' )
player = False
computer = t[randint(0,2)]







