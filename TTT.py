#1. Import tools
#2. Set up board
#3. print board function
#4. set up monitor and player values
#5. 'what is available" function to set available list
#6. "if available" function to check a single value
#7. "see available" function to print out available list
#8. set up available list
#9. function to change turn from isXTurn to opposite bool
#10. a function t return the player's id based on isXTurn
#11 a function to place pieces on the board based on turn
#12 win function to check out all possible win states.
#13 draw function t check if no one can win
#14 play again checks if the user wants to play again
#15 a game loop

from os import system
import random

#prints empty board
def print_board():
    global board

    system("clear")
    loop = 0
    while loop <3:

      print(board[loop*3] + "|" + board[1+loop*3] + "|" + board[2+loop*3])
      if loop == 0 or loop == 1:
       print("-+-+-")
      loop += 1

#finds open spots on the board and appends them to a
def what_is_available():
  global board
  a = []
  for piece in range(len(board)):
    if board[piece] == " ":
      a.append(piece)
  return a

#tells whether a given spot n is available or not
def if_available(n):
  global board, available
  avail = False
  if n in available:
   avail = True
  return avail

#prints all available spots
def see_available():
  global available
  system("clear")
  print("Available: {}".format(available))

#switches player turns to O's turn
def change_turn():
  global isXTurn
  isXTurn = not isXTurn

#returns whether it's X's turn or O's turn
def whose_turn():
  global isXTurn
  if isXTurn:
    return "x"
  return "o"
#1 recursive function which exits (switches turns) once board space has been written from whose_turn()
#2 get user input
#3 check if the value is within range 0-8 and that spot is available on the board
#4 handle errors or write the indicated board space with the appropriate symbol
def place_piece():
  response = -1
  global board
  t = whose_turn()

  try:
    see_available()
    response = int(input("what position would you like to play (0-8):"))
    if 0 <= response <= 8 and if_available(response):
      board[response] = whose_turn()
    else:
      raise ValueError
  except ValueError:
    print("All moves must be 0-8 and available!")
    place_piece()
#describes all possible win scenarios (row, column, diagonal) and checks whether any have been fulfilled
def win():
  win = False
  t = whose_turn()

  for i in range(3):
    if board[i*3] == t and board[1+i*3] == t and board[2+i*3] == t:
      print("Column Win")
      win = True
      break
    if not win:
      for i in range(3):
        if board[i] == t and board[i+3] == t and board[i+6] == t:
          print("Row Win")
          win = True
          break
    if not win:
      if board[0] == t and board[4] == t and board[8] == t or board[6] == t and board[4] == t and board[2] == t:
        print("Diag Win")
        win = True
    if win:
       print("Win for: {}".format(t))
  return win

#if all spaces are filled and none of the win scenarios were fulfilled, it's a cats game
def is_cats_game():
  count = 0
  while count < 9:
    if board[count] == " ":
      return False
    count += 1
  return True
#ask player if they want to play again, if yes, clear the board and recordedstatemove array, start again
def play_again():

  global board, isXTurn
  stay = False
  response = input("do you want to play again (Y/N):").upper()

  while response != "Y" and response != "N":
    system("clear")
    response = input("do you want to play again (Y/N):").upper()

  if response == "Y":
    stay = True
    board = [" "] * 9
    isXTurn = False
    recordedstatemove={}
  return stay
#check if game is over by checking for win and cats game scenarios. Display winner if one was found. Or display cats game.
def endcheck():
  wins = win()
  cat = is_cats_game()
  who_won = 'x'

  if wins:
    system("clear")
    print_board()
    if isXTurn:
      who_won = 'x'
      print("X Wins!")
    else:
      who_won = 'o'
      print("O Wins!")
    train_ai(who_won)

  if cat:
    print("Cats Game")
  if wins or cat:
    if not play_again():
      print("Good Game")
      system.exit()


""" AI PORTION......
-set up AI variables (statemap, movelist, statelist)
-convert board to string (for storing current state)
-create a function to make a move using the ai's possible moves
-create a function to revisit all past moves in a game and train based on game results
-make all minor changes in functions related to x and o player id
-reset recorded state in playagain()
-report function to display state map
-modify the game loop to call ai functions
-end game call reports
"""
#dictionary that storesn all the game states it's seen so far and their available moves
statemap = {}
#dictionary that records the moves made in each game state 
recordedstatemove={}

#converts board state to a string to be stored in statemap
def board_to_string():
  board_state = ''
  for space in board:
    board_state += space
  return board_state

"""
recursive function
first converts board to string
if the board state has been encountered before, it picks a move at random from the available moves for this state and plays it
note: over time, the better moves will have been reinforced in the statemap, so the ai will be more likely to pick winning moves
if the board state has NOT been encountered before, add it to the statemap and find the available moves
then call. itself again to play a move. Its move on a new statemap will actually be random (equal chance of each possible move)
"""
def ai_move():
  print("AI turn start")
  global statemap, recordedstatemove
  current_state = board_to_string()

  if current_state in statemap:
    print("Has seen current state")
    move_index = random.randint(0, (len(statemap[current_state])-1))
    space = statemap[current_state] [move_index]
    recordedstatemove[current_state] = move_index
    board[space] = 'o'
  else:
    print("Has NOT seen current state")
    statemap[current_state] = what_is_available()
    ai_move()

"""train AI based on game outcome
if the human won, delete each played move from each state in the game
if the AI won, reinforce each played move 3x in its corresponding statemap
"""
def train_ai(winner):
  print(f"over train: {statemap}")
  print(len(statemap))
  if winner=='x':
   for state, played_move in recordedstatemove.items():
    try:
        del statemap[state][played_move]
    except IndexError:
       continue
  else:
    for state, played_move in recordedstatemove.items():
      for i in range(3):
         statemap[state].append(statemap[state] [played_move])
#print current contents of statemap and recordedstatemove
def show_state_map():
  system('clear')
  print('statemap:')
  for game_state, avail_picks in statemap.items():
    print('state: [{}]\tmove: {}'.format(game_state, avail_picks))
  print('\nRecorded state: statemap index')
  for game_state, move in recordedstatemove.items():
    print('state: [{}]\tmove: {}'.format(game_state, move))
#game loop
isXTurn = True
x = "x"
o = "o"
board = [" "] * 9

while True:
  print_board()

  if isXTurn:
    available = what_is_available()
    place_piece()
  else:
    ai_move()
  endcheck()
  change_turn()
  show_state_map()
