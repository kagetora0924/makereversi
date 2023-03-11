import Board
class Game():
    gameover = False
    def __init__(self):
        game_board = Board()
        while(not gameover):
            is_valid = False
            game_board.show()
            while(not is_valid):
                move_made = input()
                is_valid = game_board.valid_move_check(move_made)
                if(not is_valid):
                    print("This is not a valid move")
            game_board.play(move_made)
    