class Board():
    stones = []
    def __init__(self):
        stones = [['-' for i in range(8)] for j in range(8)]
    
    def show(self): #ボードを見せる
        print("-12345678")
        for i in range(0,7):
            print(chr(ord('a') + i), end='')
            for j in range(0,7):
                print(stones[i][j], end=' ')
            print()
    
    def valid_move_check(self, move_made):
        #for a move to be valid following must be met (suppose you play black):
        #0.it has right format(a1,a2,...a8,b1,...h7,h8)
        #1.it's within the board
        #2.there's at least one adjacent white stone
        #3.if you go all the way in the direction of that white stone
        #   you find a black stone
        if(not self.on_board):
            return False

    @property
    def on_board(self, move_made):
        if(len(move_made) != 2):
            return False
        if(not move_made[0] in ['a','b','c','d','e','f','g','h']):
            return False
        if(not move_made[1] in ['1','2','3','4','5','6','7','8']):
            return False
        return True

    @property
    def direction(self, index):
        """
        direction to help make search methods easier.
        012
        3 4
        567
        above shows which index means which direction.
        returns a list of two numbers, -1 or 0 or 1, each indicating
        "i" direction increments and "j" direction increments.
        e.g. direction(0) returns [-1,-1]
        direction(6) returns [1,0]
        direction(4) returns [0,1]
        """


    def search_adjacent_opponent(self, move_made):
        #search for an adjacent opponent's stone and return a list of
        #direction.
    
    def search_sandwiched(self, move_made, direction):
        #search for my stone in the direction of an adjacent opponent's stone.
        #If found, return a list of direction.