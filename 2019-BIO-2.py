# Question 2: Trail
import random


class Trail:

    trail = []

    def __init__(self, trail_len):
        self.trail_len = trail_len

    def move(self, coords):
        # Add coords to trail then move
        self.trail.append(coords)

        while(len(self.trail) > self.trail_len):
            # Remove oldest square
            self.trail.pop(0)

        print(self.trail)

    def is_blocked(self, coords):
        return coords in self.trail

class Explorer:
    coords = (0, 0)
    direction = 2  # 0 = Up, 1 = Right, 2 = Down, 3 = Left

    def __init__(self, trail_len, instructions):
        self.trail_len = trail_len
        self.instructions = instructions

        self.trail = Trail()

    def final_coordinates(self, n_of_moves):
        for i in range(n_of_moves):
            if(self.move()): # Cannot move
                break

    def next_square(self, coords, direction):
        if(self.direction == 0): # Up
            coords[1] -= 1

    def move(self):
        next_square = self.next_square(self.coords, self.direction)