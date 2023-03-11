#import game
#import board
#import ComputerPlayer

print("This is reversi game made by Kevin")
print("press 'Enter' to start")
enter_pressed = False
while(not enter_pressed):
    if(input() == ""):
        enter_pressed = True

reversi_game = Game()
"""
print("press 'b' to play as black, 'w' to play as white")
bw_pressed = False
turn = ""
while(not bw_pressed):
    pressed = input()
    if(pressed == 'b' or pressed == 'w'):
        bw_pressed = True
        turn = pressed


if(turn == 'b'):
    reversi_game = Game(black)
else:
    reversi_game = Game(white)
"""