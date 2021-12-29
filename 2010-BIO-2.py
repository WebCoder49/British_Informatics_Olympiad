# Die Tipping
import copy


class Die:
    faces = { # Axis direction; neg. then pos. - default orientation - store all faces as multiple orientations with same top
        "x": (3, 4),
        "y": (5, 2),
        "z": (6, 1),
    }
    def turn(self, orbit_axis, clockwise): # As viewed from neg end of orbital axis:
        # Get axes to change - orbit axis "stays still"
        AXIS_NAMES = ["x", "y", "z"]
        orbit_axis_index = AXIS_NAMES.index(orbit_axis)
        axis_a_id, axis_b_id = tuple(AXIS_NAMES[orbit_axis_index+1:] + AXIS_NAMES[:orbit_axis_index]) # View from neg of orbital - up then right (90deg clockwise)
        """
        ^ = a
        |_
        o_|____> = b"""
        # Axis going up then axis going right as viewed from neg end of orbital
        axis_a = self.faces[axis_a_id]
        axis_b = self.faces[axis_b_id]
        if(not clockwise):
            # Invert a as anticlockwise
            axis_a = (axis_a[1], axis_a[0])
        else:
            # Invert b as clockwise
            axis_b = (axis_b[1], axis_b[0])
        # Save axes swapped
        self.faces[axis_a_id] = axis_b
        self.faces[axis_b_id] = axis_a

    def tip(self, direction):
        # Turn a certain direction on a 2D board - 0-thru-3 means up-clockwise-left

        # Up/down so tip x axis
        if(direction == 0):
            # Up
            self.turn("x", False)
        elif(direction == 2):
            # Down
            self.turn("x", True)
        # Right/left so tip y axis
        elif (direction == 3):
            # Left
            self.turn("y", False)
        elif (direction == 1):
            # Right
            self.turn("y", True)

    def top(self):
        # Positive z-axis
        return self.faces["z"][1]


class Grid:
    def __init__(self, centre):
        self.die = Die()

        self.grid = [] # 11 rows of 11 ones
        for y in range(11):
            self.grid.append(list((1, )*11))
        self.width = 11
        self.height = 11

        # Replace centre of grid coordinate by coordinate - centre size 3by3
        for cy in range(3):
            for cx in range(3):
                self.grid[cy+4][cx+4] = copy.deepcopy(centre[cy][cx]) # Offset of 4 so at centre (5 either side of centre 1, minus 1 each side to make 3)

        # Start at centre
        self.x = 5
        self.y = 5
        self.heading = 0  # Default = up

    def move(self):
        # Change value of current square
        which_move = self.change_square()
        if(which_move == 1 or which_move == 6):
            # Move according to heading
            self.move_raw()
        elif(which_move == 2):
            self.heading = (self.heading + 1) % 4
            self.move_raw() # +90deg
        elif (which_move == 3 or which_move == 4):
            self.heading = (self.heading + 2) % 4
            self.move_raw()  # +180deg
        elif (which_move == 5):
            self.heading = (self.heading - 1) % 4
            self.move_raw()  # -90deg

    def move_raw(self):
        self.die.tip(self.heading)

        # 0 or 2 = up or down
        if(self.heading == 0):
            self.y -= 1
        elif(self.heading == 2):
            self.y += 1
        # 1 or 3 = right or left
        if (self.heading == 3):
            self.x -= 1
        elif (self.heading == 1):
            self.x += 1

        self.y %= self.height
        self.x %= self.width

    def change_square(self):
        value = self.grid[self.y][self.x]
        # Add die and make <= to 6
        value += self.die.top()
        if value > 6: value -= 6 # Not mod as no 0
        # Save value back to grid and return
        self.grid[self.y][self.x] = value
        return value

    def three_by_three(self):
        grid = []
        # Return 3by3 grid section around current pos
        for y in range(self.y-1, self.y+2): # Before, this and after
            if(y < 0 or y >= self.height):
                row = ["x", "x", "x"]
            else:
                row = []
                for x in range(self.x - 1, self.x + 2):  # Before, this and after
                    if (x < 0 or x >= self.width):
                        row.append("x")
                    else:
                        row.append(self.grid[y][x])
            grid.append(row)

        return grid


def input_grid(rows, cast):
    grid = []
    for i in range(rows):
        row = list(map(cast, input().split()))
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(map(str, row))) # Turn each square into a str and join w/ spaces

grid = Grid(input_grid(3, int))

exit = False
while(not exit):
    moves = int(input())
    if(moves == 0):
        exit = True
    else:
        for i in range(moves):
            grid.move()
        print_grid(grid.three_by_three())
input()