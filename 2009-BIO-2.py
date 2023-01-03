# Puzzle Game

# 2022-11-07 Marking (1 right, 0 wrong, * bug):
# 11001100111111111111 20/24
# TODO: EBI: Check inputs/outputs correct

# So far, all of 2009 paper has taken 126m
from copy import deepcopy

class Puzzle:
    def __init__(self, pattern:list):
        self.above = deepcopy(pattern)
        self.above_used = [0, 0, 0, 0] # Each col.'s number above fallen
        self.grid = pattern # Playing on grid; 2d list

    def move(self):
        in_block = [[False for _ in range(4)] for _ in range(4)] # True if in block

        score = 1
        has_blocks = False
        # Find blocks to remove
        for y, row in enumerate(self.grid):
            for x, piece in enumerate(row):
                # print((x, y))
                # Get size
                size = self.size_of_block(in_block, x, y, piece)
                if size > 1:
                    # print((x, y), size)
                    has_blocks = True
                    score *= size # Block (0 means other block; 1 means no block)
                elif size == 1:
                    # A block of size 1 is not a block
                    in_block[y][x] = False
        # print(in_block)

        # Remove blocks; fill in
        for x in range(4):
            piece_y = 3
            for y in range(3, -1, -1):
                # Process col. up grid
                while piece_y >= 0 and in_block[piece_y][x]:
                    # No longer present; "drop down"
                    piece_y -= 1
                # Place
                if piece_y >= 0:
                    self.grid[y][x] = self.grid[piece_y][x]
                else:
                    # From above
                    above_y = (- self.above_used[x] + piece_y) % 4 # Repeated pattern
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
            if x_adj < 0 or y_adj < 0 or x_adj >= 4 or y_adj >= 4: continue  # Out of range
            # print(">", x_adj, y_adj, self.grid[y_adj][x_adj], piece)
            if self.grid[y_adj][x_adj] == piece:
                # In block
                size += self.size_of_block(in_block, x_adj, y_adj, self.grid[y_adj][x_adj])

        return size

    def __repr__(self):
        # Display grid
        return "\n".join(map(lambda row: "".join(row), self.grid))


grid = []
# Input grid
for i in range(4):
    grid.append(list(input().strip()))

puzzle = Puzzle(grid)

score = 0
# Input loop
while True:
    rounds = int(input())
    # print(rounds) - EBI: Check printing all needed and *no more*
    if rounds == 0: break
    if rounds > 0:
        for i in range(rounds):
            this_score = puzzle.move()
            # print(this_score)
            if this_score > 1:
                score += this_score
            else:
                # No blocks to be removed; move does nothing
                print(puzzle)
                print("GAME OVER")
                print(score)
                break
        else:
            # Not game over
            print(puzzle)
            print(score)