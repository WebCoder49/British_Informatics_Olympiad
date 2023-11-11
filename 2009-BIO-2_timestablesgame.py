# Puzzle Game as a useful times tables game
import os
import random
import time
from copy import deepcopy

class Puzzle:
    def __init__(self, pattern:list):
        self.above = deepcopy(pattern)
        self.size = len(pattern)
        self.above_used = [0 for _ in range(self.size)] # Each col.'s number above fallen
        self.grid = pattern # Playing on grid; 2d list
        self.blocks_only = "" # String rep.

    def move(self):
        in_block = [[False for _ in range(self.size)] for _ in range(self.size)] # True if in block

        score = 1
        has_blocks = False
        # Find blocks to remove
        for y, row in enumerate(self.grid):
            for x, piece in enumerate(row):
                # print((x, y))
                # Get size
                size = self.size_of_block(in_block, x, y, piece)
                if size > 1:
                    has_blocks = True
                    score *= size # Block (0 means other block; 1 means no block)
                elif size == 1:
                    # A block of size 1 is not a block
                    in_block[y][x] = False
        # print(in_block)

        self.blocks_only = self.__repr__(in_block)

        # Remove blocks; fill in
        for x in range(self.size):
            piece_y = 3
            for y in range(self.size-1, -1, -1):
                # Process col. up grid
                while piece_y >= 0 and in_block[piece_y][x]:
                    # No longer present; "drop down"
                    piece_y -= 1
                # Place
                if piece_y >= 0:
                    self.grid[y][x] = self.grid[piece_y][x]
                else:
                    # From above
                    above_y = (- self.above_used[x] + piece_y) % self.size # Repeated pattern
                    # print(x, above_y, self.above, self.above[above_y][x])
                    self.grid[y][x] = self.above[above_y][x]
                piece_y -= 1

            self.above_used[x] -= (piece_y+1) # y will be neg or 0; last not used

        return score

    def size_of_block(self, in_block:list, x:int, y:int, piece:str):
        """Recursively DFS a block and return its size after adding it to in_block"""
        if in_block[y][x]: return 0 # Already visited
        # print(x, y, self.grid, in_block[y][x])

        in_block[y][x] = True
        size = 1 # This piece

        for x_adj, y_adj in [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]:
            if x_adj < 0 or y_adj < 0 or x_adj >= self.size or y_adj >= self.size: continue  # Out of range
            # print(">", x_adj, y_adj, self.grid[y_adj][x_adj], piece)
            if self.grid[y_adj][x_adj] == piece:
                # In block
                size += self.size_of_block(in_block, x_adj, y_adj, self.grid[y_adj][x_adj])

        return size

    def colour_char(self, char:str):
        if char == "R": return "\x1b[30;41mR \x1b[0m"
        if char == "G": return "\x1b[30;42mG \x1b[0m"
        if char == "B": return "\x1b[30;44mB \x1b[0m"
        if char == "Y": return "\x1b[30;43mY \x1b[0m"
        if char == "M": return "\x1b[30;45mM \x1b[0m"
        if char == "C": return "\x1b[30;46mC \x1b[0m"
        if char == "D": return "\x1b[37;40mD \x1b[0m"
        if char == "L": return "\x1b[30;47mL \x1b[0m"
        if char == " ": return "\x1b[0m  \x1b[0m"
        return char

    def __repr__(self, show_matrix:list=None):
        if show_matrix is not None:
            # Create new grid
            grid = deepcopy(self.grid)
            for y, row in enumerate(show_matrix):
                for x, show in enumerate(row):
                    if not show: grid[y][x] = " "
            return "\n".join(map(
                lambda row: "".join(list(map(self.colour_char, row))
                                    ), grid))
        else:
            # Display whole grid
            return "\n".join(map(
                lambda row: "".join(list(map(self.colour_char, row))
                                 ), self.grid))

grid = []
for y in range(5):
    row = []
    for x in range(5):
        row.append(random.choice("RGBDL"))
        # row.append(random.choice("RGBYMCDL"))
    grid.append(row)

puzzle = Puzzle(grid)

score = 0
# Input loop
while True:
    os.system("cls")
    print("TOTAL SCORE:", score)
    before_move = str(puzzle)
    print(before_move)
    print()
    this_score = puzzle.move()
    if(this_score == 1):
        print("Done!")
        break
    else:
        guessed_score = int(input("What's the score for this?"))
        for i in range(3):
            os.system("cls")
            print("TOTAL SCORE:", score)
            print(puzzle.blocks_only)
            time.sleep(0.2)
            os.system("cls")
            print("TOTAL SCORE:", score)
            print(before_move)
            time.sleep(0.2)
        if(guessed_score == this_score):
            score += this_score
        else:
            print("You've lost your streak! The correct answer was", this_score)
            score = 0