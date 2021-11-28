# Loops
class Board:

    # Directions from tiles for each colour
    adjacent = {
        0: { # Colour 0 - red (solid)
            1: ((0, -1), (0, 1)), # Each item: Change in x, change in y
            2: ((-1, 0), (1, 0)),
            3: ((0, -1), (-1, 0)),
            4: ((0, -1), (1, 0)),
            5: ((0, 1), (1, 0)),
            6: ((0, 1), (-1, 0)),
        },
        1: {  # Colour 1 - green (dashed)
            2: ((0, -1), (0, 1)),  # Each item: Change in x, change in y
            1: ((-1, 0), (1, 0)),
            5: ((0, -1), (-1, 0)),
            6: ((0, -1), (1, 0)),
            3: ((0, 1), (1, 0)),
            4: ((0, 1), (-1, 0)),
        }
    }

    def __init__(self, grid):
        self.grid = grid # 2D array
        self.height = len(self.grid) # Number of rows
        self.width = len(self.grid[0])

    def loops(self, colour):

        self.visited = set() # Already checked tiles - reset for colour
        loop_tiles = 0

        for y in range(self.height):
            for x in range(self.width):
                if (x, y) in self.visited:
                    print("Ignored: ", x, y)
                    continue
                else:
                    # Check from x, y
                    loop_tiles += self.find_loop(x, y, colour)
                    print("Found: ", x, y, loop_tiles, self.visited)

        return loop_tiles

    def find_loop(self, x, y, colour):
        # Find length of loop
        tile_count = 1
        # First coords
        self.visited.add((x, y))
        first_x = x
        first_y = y

        current_tile = (x, y)

        next_tile = self.find_next_tile(x, y, colour, first_x, first_y) # First x and y is where going back to will cause a closed loop

        while(next_tile != None):
            self.visited.add(current_tile)
            previous_tile = current_tile
            current_tile = next_tile
            # Find next tile
            tile_count += 1
            # results = self.find_next_tile(next_tile[0], next_tile[1], colour, first_x, first_y, direction)
            next_tile = self.find_next_tile(current_tile[0], current_tile[1], colour, first_x, first_y, previous_tile)
            if(next_tile == "loop"):
                return tile_count

        return 0 # Loop not closed

    def find_next_tile(self, x, y, colour, first_x, first_y, prev_tile=None):
        tile_id = self.grid[y][x]
        possible_dirs = self.adjacent[colour][tile_id]

        if prev_tile == None or (prev_tile[0]-x, prev_tile[1]-y) in possible_dirs: # If links back to previous tile
            # Not possible if not linked to previous square
            for dir in possible_dirs:

                # x and y of destination
                dest_x = dir[0] + x
                dest_y = dir[1] + y

                if(prev_tile != None):
                    if((dest_x, dest_y) == prev_tile):
                        # Going to previous - not allowed
                        continue

                print("   To", dest_x, dest_y, "From", x, y, "Start", first_x, first_y)

                if(dest_x >= self.width or dest_x < 0 or dest_y >= self.height or dest_y < 0):
                    continue # Out of board
                elif(dest_x == first_x and dest_y == first_y):
                    # Closed loop
                    if((x-first_x, y-first_y) in self.adjacent[colour][self.grid[first_y][first_x]]):
                        # Line attaching first tile to last tile
                        return "loop" # closed loop
                    else:
                         print("NOT C", self.adjacent[colour][self.grid[first_y][first_x]], x, y)
                         continue
                elif ((dest_x, dest_y) in self.visited):
                    continue  # Going back on visited square
                else:
                    print("   Y")
                    return (dest_x, dest_y)

        return None # No possible next step found



def input_grid():
    size = int(input("Size: "))
    grid = []

    for i in range(size):
        # Convert string input to list of ints and append to grid
        grid.append(
            list(
                map(
                    lambda tile: int(tile), # Items to ints
                    input("Row {}: ".format(i))[0:size]) # To array
            )
        )

    return grid


while input("> ") != "q":
    board = Board(input_grid())
    print(board.loops(0), board.loops(1))