# Dots and Boxes

class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.size = width * height

        # Create arrays for vertical and horizontal lines
        vertical_lines = []
        for x in range(width):
            column = []
            for y in range(height-1):
                column.append(False)
            vertical_lines.append(column)

        horizontal_lines = []
        for y in range(height):
            row = []
            for x in range(width-1):
                row.append(False)
            horizontal_lines.append(row)

        self.horizontal_lines = horizontal_lines
        self.vertical_lines = vertical_lines

        # Create arrays for boxes won
        boxes_won = []
        for y in range(height-1):
            row = []
            for x in range(width-1):
                row.append(0)
            boxes_won.append(row)
        self.boxes_won = boxes_won

    def display_boxes_won(self):
        chars = ["*","X","O"]
        for row in self.boxes_won:
            row_str = ""
            for col in row:
                row_str += chars[col]
            print(row_str)

    def draw_line(self, player, position, direction):
        # Turn position into x, y
        x = position % self.width
        y = position // self.width

        # Get x, y of line
        if(direction == 0):
            # Upwards
            if(y == 0):
                return False # impossible
            else:
                y -= 1
        elif (direction == 2):
            # Down
            if (y == (self.height-1)):
                return False  # impossible
            # Don't need to change y
        elif (direction == 3):
            # Left
            if (x == 0):
                return False  # impossible
            else:
                x -= 1
        elif (direction == 1):
            # Right
            if (x == (self.width - 1)):
                return False  # impossible
            # Don't need to change x

        if(direction & 1 == 0):
            # Even - vertical lines
            if(self.vertical_lines[x][y]): return False # Already taken
            self.vertical_lines[x][y] = True

            if(x != (self.width - 1) and y != 0):
                if(self.horizontal_lines[y][x] and self.horizontal_lines[y+1][x] and self.vertical_lines[x+1][y]):
                    # Box to right
                    print(player, x, y, "right", self.horizontal_lines, self.vertical_lines)
                    self.boxes_won[y][x] = player

            if(x != 0 and y != (self.height - 1)):
                if (self.horizontal_lines[y][x-1] and self.horizontal_lines[y + 1][x-1] and self.vertical_lines[x - 1][y]):
                    # Box to left
                    print(player, x, y, "left", self.horizontal_lines, self.vertical_lines)
                    self.boxes_won[y][x-1] = player
        else:
            # Odd - horizontal lines
            if (self.horizontal_lines[y][x]): return False  # Already taken
            self.horizontal_lines[y][x] = True

            if (y != (self.height - 1) and x != (self.width - 1)):
                if (self.vertical_lines[x][y] and self.vertical_lines[x + 1][y] and self.horizontal_lines[y + 1][x]):
                    # Box below
                    print(player, x, y, "below", self.horizontal_lines, self.vertical_lines)
                    self.boxes_won[y][x] = player

            if (y != 0 and x != (self.width - 1)):
                if (self.vertical_lines[x][y - 1] and self.vertical_lines[x + 1][y - 1] and self.horizontal_lines[y - 1][x]):
                    # Box above
                    print(player, x, y, "above", self.horizontal_lines, self.vertical_lines)
                    self.boxes_won[y - 1][x] = player

        return True

class Player:
    def __init__(self, id, position, modifier, anticlockwise):
        self.position = position-1 # zero-indexed
        self.modifier = modifier
        self.anticlockwise = anticlockwise
        self.id = id

    def turn(self, grid):
        # Increase pos by modifier
        self.position += self.modifier
        self.position = self.position % grid.size

        for i in range(grid.size): # Keep trying for every position in grid if not successful
            if(self.anticlockwise):
                for direction in range(0, -4, -1):
                    if(grid.draw_line(self.id, self.position, direction%4)):
                        print(self.id, self.position, "urdl"[direction])
                        return  # Successful
            else:
                for direction in range(4):
                    if(grid.draw_line(self.id, self.position, direction)):
                        print(self.id, self.position, "urdl"[direction])
                        return  # Successful

            # Not successful - increment
            self.position += 1
            self.position = self.position % grid.size

class Game:
    def __init__(self, grid, turns, *players): # Player classes w/ pos and mod
        self.grid = grid

        if(turns > 60):
            self.turns = 60
        elif(turns < 1):
            self.turns = 1
        else:
            self.turns = turns

        self.players = players
        self.player_n = len(players)

    def play(self):
        for i in range(self.turns):
            self.players[i % self.player_n].turn(self.grid)


grid = Grid(6, 6)
player_1 = Player(1, int(input("Player 1 Pos: ")), int(input("Player 1 Mod: ")), False)
player_2 = Player(2, int(input("Player 2 Pos: ")), int(input("Player 2 Mod: ")), True)
game = Game(grid, int(input("No. of Turns: ")), player_1, player_2)

game.play()
grid.display_boxes_won()

# Still bugs